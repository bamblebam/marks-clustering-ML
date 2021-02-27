# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
# %%
df = pd.read_csv('datasets/processed.csv')
# %%
df.head()
# %%
clustering_cols = [f'Unnamed: {i}' for i in range(3, 33)]
# %%
X = df[clustering_cols]
Y = df.drop(clustering_cols, axis=1)
# %%
kmeans = KMeans(n_clusters=44)
kmeans.fit(X)
# %%
print(kmeans.labels_)

# %%
