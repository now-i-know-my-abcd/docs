paths <- list.files(here::here("R"), recursive = TRUE, full.names = TRUE)

for (path in paths) {
  source(path)
}
