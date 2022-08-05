## setup ----

require(tidyverse)

## read in summary of abcd puberty data ----

abcd_pds_summary_real <- read_rds(here::here("data", "pds_summary.rds")) %>% 
  as_tibble(.name_repair = "universal") %>% 
  select(colname = ...2, value = n) %>% 
  mutate(across(everything(), str_trim, side = "both")) %>% 
  group_by(colname) %>% 
  mutate(id_temp = 1:n()) %>% 
  ungroup() %>% 
  pivot_wider(names_from = colname, values_from = value) %>% 
  select(-id_temp)

## parse summary stats for numeric cols

abcd_pds_summary_num <- abcd_pds_summary_real %>% 
  select(where(function (x) startsWith(x[1], "Min."))) %>% 
  pivot_longer(cols = everything(), names_to = "colname", values_to = "value") %>% 
  separate(value, into = c("stat", "value"), sep = ":") %>% 
  mutate(stat = str_trim(stat, side = "right"),
         # NA values will get coerced to NA bc they're strings, but that's fine here
         value = as.numeric(value)) %>% 
  filter(!is.na(stat)) %>% 
  mutate(stat = dplyr::recode(stat,
                              Min. = "min",
                              `1st Qu.` = "q25",
                              Median = "median",
                              Mean = "mean",
                              `3rd Qu.` = "q75",
                              Max. = "max",
                              `NA's` = "n_na")) %>% 
  pivot_wider(id_cols = colname, names_from = stat, values_from = value) %>% 
  mutate(n_na = coalesce(n_na, 0))

## parse summary stats for character cols ----

abcd_pds_summary_char <- abcd_pds_summary_real %>% 
  select(where(function (x) !startsWith(x[1], "Min."))) %>% 
  pivot_longer(cols = everything(), names_to = "colname", values_to = "value") %>% 
  filter(!is.na(value)) %>% 
  separate(value, into = c("level", "value"), sep = ":") %>% 
  mutate(value = str_trim(value, side = "right"),
         value = as.numeric(value))


