# %%
from operator import concat
import pandas as pd
import seaborn as sns
import random
from matplotlib.pyplot import savefig

random.seed(17)

f = open("../../data/abcd_smri_colnames.txt", "r")
abcd_smri_colnames = f.readlines()
abcd_smri_colnames = [colname.strip() for colname in abcd_smri_colnames]

data = pd.DataFrame({'src_subject_id': range(1000)})

# dangit! python indexes exclusively!
for col in abcd_smri_colnames[0:5]:
    data[col] = [random.gauss(0, 1) for i in range(1000)]

data = data.set_index('src_subject_id')

sns.pairplot(data)

savefig('../../docs/figs/py_seaborn_pairs.png')
