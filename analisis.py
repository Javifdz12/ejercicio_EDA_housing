import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file=pd.read_csv("USA_Housing.csv",sep=",")

print(file.head(),
file.columns,
file.describe())

for columna in file.columns:
    if columna!="Address":
        sns.boxplot(x=file[columna])
        plt.show()
    else:
        sns.histplot(x=file[columna])

file=file.dropna().head

