# %%
import pandas as pd
# %%
pd.set_option("display.max_rows", None, "display.max_columns", None)
# %%
df = pd.read_csv('datasets/KJSCE2018_III-COMP-ND2020.csv')
# %%
df2 = df.copy()
# %%
df2 = df2[df2["K.J.Somaiya College of Engineering, Mumbai - 77, .-."].notnull()]

# %%
df2 = df2[df2["K.J.Somaiya College of Engineering, Mumbai - 77, .-."].str.len() < 30]
# %%
df2.shape
# %%
df2.head(137)
# %%
df2.to_csv('datasets/processed.csv')
# %%
