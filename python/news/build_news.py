"""Generate docs/news.md: recent ABCD papers, preprints, and Bluesky posts.

Run from the repo root before `jupyter-book build docs`:

    python python/news/build_news.py

Sources (all free, no API key needed):
  - Europe PMC: journal articles + preprints (bioRxiv, medRxiv, PsyArXiv, ...)
  - OpenAlex: fills in works Europe PMC missed (deduplicated by DOI/title)
  - Bluesky: the official @theabcdstudy account (RSS) and #ABCDStudy posts

Optional env vars:
  NEWS_DAYS            look-back window in days (default 30)
  BSKY_HANDLE          Bluesky handle + app password; if set, hashtag search is
  BSKY_APP_PASSWORD    authenticated (more reliable from GitHub Actions)

Only the Python standard library is used. Every source fails soft: if one is
down, the page is still written with whatever was retrieved, so the site
build never breaks because of this script.
"""

import datetime as dt
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

QUERY_PHRASE = "Adolescent Brain Cognitive Development"
BSKY_ACCOUNT = "theabcdstudy.bsky.social"
BSKY_HASHTAG = "#ABCDStudy"
USER_AGENT = "now-i-know-my-abcd-news/1.0 (+https://github.com/now-i-know-my-abcd/docs)"

OUT_PATH = Path(__file__).resolve().parents[2] / "docs" / "news.md"
DAYS = int(os.environ.get("NEWS_DAYS", "30"))
TODAY = dt.date.today()
SINCE = TODAY - dt.timedelta(days=DAYS)

problems = []  # sources that failed, reported on the page


def fetch(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": USER_AGENT, **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def fetch_json(url, **kwargs):
    return json.loads(fetch(url, **kwargs))


def clean(text):
    """Strip HTML tags/entities and collapse whitespace."""
    text = re.sub(r"<[^>]+>", "", html.unescape(text or ""))
    return re.sub(r"\s+", " ", text).strip()


def md_escape(text):
    """Escape characters MyST/Markdown would otherwise interpret."""
    return re.sub(r"([\\`*_{}\[\]<>()#+!|~$])", r"\\\1", clean(text))


def norm_title(title):
    return re.sub(r"[^a-z0-9]", "", clean(title).lower())


# ---------------------------------------------------------------- papers

def europe_pmc():
    query = (
        f'TITLE_ABS:"{QUERY_PHRASE}" '
        f"AND FIRST_PDATE:[{SINCE.isoformat()} TO {TODAY.isoformat()}]"
    )
    works, cursor = [], "*"
    while True:
        params = urllib.parse.urlencode({
            "query": query, "format": "json", "resultType": "core",
            "pageSize": 100, "cursorMark": cursor,
        })
        data = fetch_json(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?{params}")
        for r in data["resultList"]["result"]:
            is_preprint = r.get("source") == "PPR"
            venue = ((r.get("bookOrReportDetails") or {}).get("publisher") if is_preprint
                     else (r.get("journalInfo") or {}).get("journal", {}).get("title"))
            doi = (r.get("doi") or "").lower()
            link = (f"https://doi.org/{doi}" if doi
                    else f"https://europepmc.org/article/{r.get('source')}/{r.get('id')}")
            works.append({
                "title": r.get("title", ""),
                "authors": r.get("authorString", ""),
                "venue": venue or r.get("journalTitle") or "",
                "date": r.get("firstPublicationDate", ""),
                "doi": doi, "link": link, "preprint": is_preprint,
            })
        next_cursor = data.get("nextCursorMark")
        if not next_cursor or next_cursor == cursor or not data["resultList"]["result"]:
            return works
        cursor = next_cursor


def openalex():
    params = urllib.parse.urlencode({
        "filter": (f'title_and_abstract.search:"{QUERY_PHRASE}",'
                   f"from_publication_date:{SINCE.isoformat()},"
                   f"to_publication_date:{TODAY.isoformat()},"
                   # skip conference abstracts, peer-review reports, errata, etc.
                   "type:article|preprint|review"),
        "per-page": 200,
        "select": "title,doi,publication_date,authorships,primary_location,type",
    })
    data = fetch_json(f"https://api.openalex.org/works?{params}")
    works = []
    for r in data.get("results", []):
        authors = [a["author"]["display_name"] for a in r.get("authorships", [])[:6]]
        if len(r.get("authorships", [])) > 6:
            authors.append("et al.")
        source = ((r.get("primary_location") or {}).get("source") or {})
        doi = (r.get("doi") or "").replace("https://doi.org/", "").lower()
        works.append({
            "title": r.get("title") or "",
            "authors": ", ".join(authors),
            "venue": source.get("display_name") or "",
            "date": r.get("publication_date") or "",
            "doi": doi,
            "link": r.get("doi") or (r.get("primary_location") or {}).get("landing_page_url") or "",
            "preprint": r.get("type") == "preprint" or source.get("type") == "repository",
        })
    return works


def collect_papers():
    seen_doi, seen_title, papers = set(), set(), []
    for name, source in (("Europe PMC", europe_pmc), ("OpenAlex", openalex)):
        try:
            results = source()
        except Exception as exc:  # noqa: BLE001 - fail soft, report on page
            problems.append(f"{name} ({type(exc).__name__})")
            print(f"warning: {name} failed: {exc}", file=sys.stderr)
            continue
        for w in results:
            key_t = norm_title(w["title"])
            if not key_t or (w["doi"] and w["doi"] in seen_doi) or key_t in seen_title:
                continue
            seen_title.add(key_t)
            if w["doi"]:
                seen_doi.add(w["doi"])
            papers.append(w)
    papers.sort(key=lambda w: w["date"], reverse=True)
    return papers


# ---------------------------------------------------------------- bluesky

def bsky_account_rss():
    root = ET.fromstring(fetch(f"https://bsky.app/profile/{BSKY_ACCOUNT}/rss"))
    posts = []
    for item in root.iter("item"):
        when = dt.datetime.strptime(item.findtext("pubDate", ""), "%d %b %Y %H:%M %z")
        if when.date() >= SINCE:
            posts.append({"author": BSKY_ACCOUNT, "text": item.findtext("description", ""),
                          "date": when.date().isoformat(), "link": item.findtext("link", "")})
    return posts


def bsky_hashtag():
    handle, password = os.environ.get("BSKY_HANDLE"), os.environ.get("BSKY_APP_PASSWORD")
    # searchPosts rejects `since` without auth, so filter by date below instead
    params = urllib.parse.urlencode({"q": BSKY_HASHTAG, "limit": 100, "sort": "latest"})
    if handle and password:
        session = fetch_json(
            "https://bsky.social/xrpc/com.atproto.server.createSession",
            data=json.dumps({"identifier": handle, "password": password}).encode(),
            headers={"Content-Type": "application/json"},
        )
        data = fetch_json(f"https://bsky.social/xrpc/app.bsky.feed.searchPosts?{params}",
                          headers={"Authorization": f"Bearer {session['accessJwt']}"})
    else:
        data = fetch_json(f"https://api.bsky.app/xrpc/app.bsky.feed.searchPosts?{params}")
    posts = []
    for p in data.get("posts", []):
        if p["record"].get("createdAt", "")[:10] < SINCE.isoformat():
            continue
        handle_p = p["author"]["handle"]
        rkey = p["uri"].rsplit("/", 1)[-1]
        posts.append({"author": handle_p, "text": p["record"].get("text", ""),
                      "date": p["record"].get("createdAt", "")[:10],
                      "link": f"https://bsky.app/profile/{handle_p}/post/{rkey}"})
    return posts


def collect_posts():
    posts, seen = [], set()
    for name, source in (("Bluesky @" + BSKY_ACCOUNT, bsky_account_rss),
                         ("Bluesky " + BSKY_HASHTAG, bsky_hashtag)):
        try:
            results = source()
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{name} ({type(exc).__name__})")
            print(f"warning: {name} failed: {exc}", file=sys.stderr)
            continue
        for p in results:
            if p["link"] not in seen:
                seen.add(p["link"])
                posts.append(p)
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


# ---------------------------------------------------------------- render

def render_paper(w):
    venue = f" *{md_escape(w['venue'])}*." if w["venue"] else ""
    authors = md_escape(w["authors"]).rstrip(".")
    if len(authors) > 200:
        authors = authors[:200].rsplit(",", 1)[0] + ", et al"
    return f"- **[{md_escape(w['title'])}]({w['link']})** {authors}.{venue} ({w['date']})"


def render_post(p):
    text = md_escape(p["text"])
    if len(text) > 300:
        text = text[:300].rsplit(" ", 1)[0] + "…"
    return f"- **@{md_escape(p['author'])}** ({p['date']}): {text} [View post]({p['link']})"


def main():
    papers = collect_papers()
    posts = collect_posts()
    journal = [w for w in papers if not w["preprint"]]
    preprints = [w for w in papers if w["preprint"]]

    lines = [
        "# ABCD news & new papers",
        "",
        f"*Automatically updated weekly. Last updated: {TODAY:%B %d, %Y}. "
        f"Showing the past {DAYS} days.*",
        "",
        "```{note}",
        "This page is generated automatically and is **not reviewed or endorsed**. Papers are "
        f'matched on the phrase "{QUERY_PHRASE}" in their title or abstract via '
        "[Europe PMC](https://europepmc.org/) and [OpenAlex](https://openalex.org/); posts come "
        f"from [@{BSKY_ACCOUNT}](https://bsky.app/profile/{BSKY_ACCOUNT}) and "
        f"[{BSKY_HASHTAG}](https://bsky.app/hashtag/ABCDStudy) on Bluesky. Preprints have not "
        "been peer reviewed. Spot something wrong or missing? "
        "[Open an issue](https://github.com/now-i-know-my-abcd/docs/issues).",
        "```",
        "",
    ]
    if problems:
        lines += ["```{warning}",
                  "Some sources could not be reached during the last update: "
                  + ", ".join(problems) + ". This list may be incomplete.",
                  "```", ""]

    sections = [
        (f"New journal articles ({len(journal)})", journal, render_paper),
        (f"New preprints ({len(preprints)})", preprints, render_paper),
        (f"On Bluesky ({len(posts)})", posts, render_post),
    ]
    for heading, items, render in sections:
        lines += [f"## {heading}", ""]
        lines += [render(i) for i in items] if items else ["*Nothing new in this period.*"]
        lines.append("")

    lines += [
        "## Follow along",
        "",
        "- [The ABCD Study on Bluesky](https://bsky.app/profile/theabcdstudy.bsky.social) "
        "([RSS](https://bsky.app/profile/theabcdstudy.bsky.social/rss))",
        "- [Official ABCD publications list](https://abcdstudy.org/publications/)",
        "- [ABCD documentation changelog](https://docs.abcdstudy.org/latest/info/changelog.html) "
        "and [DEAP updates](https://docs.deapscience.com/info/updates.html)",
        "- Set up your own [Google Scholar alert]"
        f"(https://scholar.google.com/scholar_alerts?view_op=create_alert_options&hl=en&alert_query=%22{urllib.parse.quote(QUERY_PHRASE)}%22) "
        "for the study name",
        "",
    ]
    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT_PATH} ({len(journal)} articles, {len(preprints)} preprints, "
          f"{len(posts)} posts; failed sources: {problems or 'none'})")


if __name__ == "__main__":
    main()
