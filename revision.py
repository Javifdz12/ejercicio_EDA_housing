import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

"""for i in file2.columns:
    x=file2[i].mean()
    y=file2[i].std()
    a=x-y
    b=x+y
    file2[i]=file2[i].loc[a<file2[i]<b]"""

file2=file.dropna()
