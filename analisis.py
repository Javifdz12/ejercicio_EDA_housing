from revision import file2
import seaborn as sns
import matplotlib.pyplot as plt

sns.lmplot(y="Price", x ="Avg. Area House Age",data=file2)
plt.show()
#segun la grafica a medida que aumenta la edad de las casas, su precio aumenta lo que me parece bastante interesante ya que eso significa que el area de las casas esta cogiendo valos con el tiempo
sns.lmplot(y="Avg. Area Income",x="Avg. Area House Age",data=file2)
plt.show()
#segun la grafica a medida que aumenta la edad de las areas, los ingresos de las areas disminuyen muy levemente ,por tanto no hay ninguna relacion entre edad de las areas e ingresos del area, es decir no se influyen entre ellos(que aumente la edad del area no quiere decir que obtengas ni mas ni menos ingresos por el area)
sns.lmplot(y="Price", x ="Avg. Area Number of Bedrooms",data=file2)
plt.show()
#segun la grafica a medida que aumenta el numero de dormitorios de las casas, aumenta muy levemente su precio por tanto,practicamente no hay ninguna relacion entre el precio de las casa y su numero de habitaciones
sns.lmplot(y="Price", x ="Avg. Area Number of Rooms",data=file2)
plt.show()
#segun la grafica a medida que aumenta el numero de habitaciones de las casas, aumenta su precio
sns.lmplot(y="Price", x ="Avg. Area Income",data=file2)
plt.show()
#segun la grafica claramente a medida que aumentan ingresos de area de las casas, aumenta su precio
sns.lmplot(y="Price", x ="Area Population",data=file2)
plt.show()
#segun la grafica a medida que aumenta la poblacion del area, aumenta el precio
sns.lmplot(y="Avg. Area Income",x="Avg. Area Number of Bedrooms",data=file2)
plt.show()
#segun la grafica no hay ninguna relacion entre numero de dormitorios e ingresos del area
sns.lmplot(y="Avg. Area Income", x ="Avg. Area Number of Rooms",data=file2)
plt.show()
#segun la grafica a medida que aumenta el numero de habitaciones de las areas, los ingresos de las area disminuyen muy levemente por tanto practicamente no hay relacion entre ingresos del area y numero de habitaciones

