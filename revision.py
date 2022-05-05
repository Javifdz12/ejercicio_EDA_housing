import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

file=pd.read_csv("USA_Housing.csv",sep=",")

print(file.head(),
file.columns,
file.describe())

"""for nombre_columna in file.columns:
    if nombre_columna!="Address":
        sns.boxplot(x=file[nombre_columna])
        plt.show()
    else:
        pass"""


file2=file.dropna()
file2=file2.drop(["Address"],axis=1)
#normalizacion del file2
file2_norm=(file2-file2.min())/(file2.max()-file2.min())
print(file2_norm.describe())

#clustering

#eleccion del numero de clusters

wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,max_iter=300)
    kmeans.fit(file2_norm)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.xlabel("Numero de Clusters")
plt.ylabel("WCSS")
plt.show()
#podemos observar que hay una notable reduccion de la caida en 4 clusters

clustering=KMeans(n_clusters=4,max_iter=300)
clustering.fit(file2_norm)




