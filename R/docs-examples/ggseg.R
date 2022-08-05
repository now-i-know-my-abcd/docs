library(tidyverse)
library(ggseg)
library(ggsegGordon)

r_ggseg_brain <- gordon %>% 
  as_tibble() %>% 
  # So stats don't get generated for those midline panels of callosal nothingness
  mutate(sim_stat = if_else(!is.na(annot), runif(n(), -1, 1), NA_real_)) %>% 
  ggplot() + 
  geom_brain(atlas = gordon, 
             mapping = aes(fill = sim_stat), 
             position = position_brain(hemi ~ side)) + 
  scale_fill_gradient2(low = "#68BCD6",
                       high = "#CE84AD") +
  labs(fill = "simulated\nstatistic")

r_ggseg_brain

ggsave(here::here("docs", "figs", "r_ggseg_brain.png"),
       r_ggseg_brain,
       device = "png",
       width = 5,
       height = 3,
       units = "in")
