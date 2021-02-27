# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from collections import defaultdict
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
labels = kmeans.labels_

# %%
clusters = pd.DataFrame({"clusters": labels})
new_df = pd.concat([clusters, df], axis=1)
# %%
new_df.head()
# %%
new_df["K.J.Somaiya College of Engineering, Mumbai - 77, .-."] = new_df[
    "K.J.Somaiya College of Engineering, Mumbai - 77, .-."].apply(str)
new_df["Unnamed: 1"] = new_df["Unnamed: 1"].apply(str)

# %%
name_list = list()
for index, row in new_df.iterrows():
    name_list.append(
        row["K.J.Somaiya College of Engineering, Mumbai - 77, .-."]+" "+row["Unnamed: 1"])
# %%
cluster_dict = defaultdict(list)
for index, cluster_num in enumerate(labels):
    cluster_dict[cluster_num].append(name_list[index])
# %%
cluster_dict = dict(cluster_dict)
cluster_dict = dict(sorted(cluster_dict.items(), key=lambda x: x[0]))
# %%
print(cluster_dict)
# %%
