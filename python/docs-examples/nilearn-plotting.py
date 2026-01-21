# %%
# Retrieve destrieux parcellation in fsaverage5 space from nilearn
from nilearn import datasets, plotting, surface
import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt
from seaborn import diverging_palette

random.seed(17)

destrieux_atlas = datasets.fetch_atlas_surf_destrieux()

# The parcellation is already loaded into memory
parcellation = destrieux_atlas['map_left']

# Retrieve fsaverage5 surface dataset for the plotting background. It contains
# the surface template as pial and inflated version and a sulcal depth maps
# which is used for shading
fsaverage = datasets.fetch_surf_fsaverage()


# %%

# Display Destrieux parcellation on fsaverage5 pial surface using nilearn
plotting.plot_surf_roi(fsaverage['infl_left'], roi_map=parcellation,
                       hemi='left', view='ventral',
                       bg_map=fsaverage['sulc_left'], bg_on_data=True)

# %%
destrieux_df_left = pd.DataFrame({'roi_val': destrieux_atlas.map_left})
destrieux_df_right = pd.DataFrame({'roi_val': destrieux_atlas.map_right})

destrieux_df_left['roi_label'] = [destrieux_atlas.labels[i] for i in destrieux_df_left['roi_val']]
destrieux_df_right['roi_label'] = [destrieux_atlas.labels[i] for i in destrieux_df_right['roi_val']]

sim_stats = [random.uniform(-100, 100) for i in range(len(destrieux_atlas.labels))]

destrieux_df_left['sim_stat'] = [sim_stats[i] for i in destrieux_df_left['roi_val']]
destrieux_df_right['sim_stat'] = [sim_stats[i] for i in destrieux_df_right['roi_val']]


# %%
def plot_my_surf_stat_map(hemi, view, axes = None):
    if hemi == 'left':
        this_atlas_df = destrieux_df_left
    else:
        this_atlas_df = destrieux_df_right
    plotting.plot_surf_stat_map(fsaverage['infl_' + hemi],
                                stat_map=np.array(this_atlas_df['sim_stat'], dtype = np.int32),
                                hemi=hemi, view=view,
                                cmap = diverging_palette(194, 327, s = 50, l = 64, as_cmap = True),
                                bg_map=fsaverage['sulc_left'], bg_on_data=True,
                                axes = axes)

# %%
plot_my_surf_stat_map('left', 'lateral')
plt.savefig('../../docs/figs/py_nilearn_leftlateral.png')

plot_my_surf_stat_map('right', 'lateral')
plt.savefig('../../docs/figs/py_nilearn_rightlateral.png')


