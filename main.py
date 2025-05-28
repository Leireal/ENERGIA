import numpy as np
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt

#ruta_csv ='ENERGIA\global_data.csv'
#df_energy = pd.read_csv(ruta_csv)


ruta_csv_2 ='ENERGIA\primera_limpieza.csv'
df_limpio = pd.read_csv(ruta_csv_2)

print(" ")
print(" ")
print("BIENVENIDO AL PROYECTO ENERGIA")
print(" ")
print("Los paises de los que se obtiene la información son", len(df_limpio['Entity'].unique()))
print(" ")
print("Veamos las hipotesis y los resultados")
print(" ")
print(" ")
time.sleep(2)
print("HIPOTESIS 1: Los países con mayor intensidad energética tienen un menor grado de eficiencia económica.")
time.sleep(2)
print(" ")
print(" ")
#df_limpio=pd.read_csv ("primera_limpieza.csv")
#df_limpio.info()
df_energy_3 = df_limpio.dropna(subset=['gdp_per_capita'])#Elimino los paises que tienen Nulo gpd per capita
#df_limpio.isnull().sum()
#df_energy_3.isnull().sum()
df_energy_3[df_energy_3["Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)"].isna()]["Entity"].drop_duplicates()
#df_energy_3[df_energy_3['Entity'] == 'South Sudan'][['Entity', 'Year', 'Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)']]
#df_energy_3[df_energy_3['Entity'] == 'Eritrea'][['Entity', 'Year', 'Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)']]#Lo relleno con la media
#Tengo que quitar new caledonia que esta todo a Nan y ver que hago con Eritrea que tiene 2 y South Sudan 4
df_energy_4 = df_energy_3[df_energy_3['Entity'] != 'New Caledonia']
df_energy_4[df_energy_4["Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)"].isna()]["Entity"].drop_duplicates()
#voy a rellenar lo de estos dos paises con la media de tos los años 
df_energy_4['Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)'] = df_energy_4.groupby('Entity')['Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)'].transform(lambda x: x.fillna(x.mean()))
df_energy_4[df_energy_4["Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)"].isna()]["Entity"].drop_duplicates()
#df_energy_4.isnull().sum()
#df_energy_4.info()

sns.lmplot(x="gdp_per_capita", y="Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)", data=df_energy_3,fit_reg=False)
#plt.xlim(0, 10000)
plt.show()