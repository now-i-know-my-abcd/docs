library(tidyverse)
library(GGally)

set.seed(17)

abcd_smri_colnames <- read_rds(here::here("data", "abcd_smri_colnames.rds")) %>% 
  .[1:5]

data <- crossing(src_subject_id = 1:1000,
         var = abcd_smri_colnames) %>% 
  mutate(value = rnorm(n())) %>% 
  pivot_wider(id_cols = src_subject_id,
              names_from = var,
              values_from = value)

r_ggally_pairs <- data %>% 
  select(-src_subject_id) %>% 
  GGally::ggpairs(lower = list(continuous = wrap("points", size = 0.5, alpha = 0.1)))

r_ggally_pairs

ggsave(here::here("docs", "figs", "r_ggally_pairs.png"),
       r_ggally_pairs,
       device = "png",
       width = 5,
       height = 5,
       units = "in")
