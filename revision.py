import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

file=pd.read_csv("USA_Housing.csv",sep=",")

print(file.head(),
file.columns,
file.describe())

for nombre_columna in file.columns:
    if nombre_columna!="Address":
        sns.boxplot(x=file[nombre_columna])
        plt.show()
    else:
        pass


file2=file.dropna()
file2=file2.drop(["Address"],axis=1)

#normalizacion del file2
file2_norm=(file2-file2.min())/(file2.max()-file2.min())
print(file2_norm.describe())

#CLUSTERING

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
file2["CLUSTERS"]=clustering.labels_
print(file2.head())

#observamos si se han echo bien los clusters
pca=PCA(n_components=2)
pca_file2=pca.fit_transform(file2_norm)
pca_file2_df=pd.DataFrame(pca_file2,columns=["Componente1","Componente2"])
pca_file2_df=pd.concat([pca_file2_df,file2["CLUSTERS"]],axis=1)
print(pca_file2_df.head())

fig=plt.figure(figsize=(6,6))
a=fig.add_subplot(1,1,1)
a.set_ylabel("Componente2",fontsize=15)
a.set_xlabel("Componente1",fontsize=15)
colores=np.array(["blue","green","yellow","red"])
a.scatter(x=pca_file2_df.Componente1,y=pca_file2_df.Componente2,c=colores[pca_file2_df.CLUSTERS],s=50)
plt.show()
#parece que se han formado bien ya que no hay practicamente mezclas entre colores

