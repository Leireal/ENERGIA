import numpy as np
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt

#LIMPIEZA
ruta_csv ='ENERGIA\global_data.csv'
df_energy = pd.read_csv(ruta_csv)

#df_energy=pd.read_csv ("global_data.csv")
df_energy_2=df_energy

df_energy_2.columns = [
    col.replace('$', 'dolar')
       .replace('%', 'perc')
    
    for col in df_energy_2.columns
]

df_energy_2["Density(P/Km2)"] = df_energy_2["Density(P/Km2)"].str.replace(",", "", regex=False)

df_energy_2 = df_energy_2[df_energy_2["Entity"] != "French Guiana"]#Elimino este pais porque tiene todo NaN
df_energy_2 = df_energy_2[df_energy['Year'] != 2020]#Elimino todas las lineas del año 2000 porque muchos datos son NaN

df_energy_2.loc[df_energy_2["Access to electricity (perc of population)"].isna(), "Access to electricity (perc of population)"] = 0
df_energy_2.loc[df_energy_2["Electricity from nuclear (TWh)"].isna(), "Electricity from nuclear (TWh)"] = 0

df_energy_2.loc[df_energy_2["Financial flows to developing countries (US dolar)"].isna(), "Financial flows to developing countries (US dolar)"] = 0

df_energy_2['gdp_per_capita'] = (
    df_energy_2.groupby('Entity', group_keys=False)['gdp_per_capita']
    .apply(lambda x: x.bfill())
)

print(df_energy_2['gdp_per_capita'].isna().sum())
df_energy_2.to_csv('primera_limpieza.csv', index=False)


ruta_csv_2 ='ENERGIA\primera_limpieza.csv'
#ruta_csv_2 ='../ENERGIA/primera_limpieza.csv'
df_limpio = pd.read_csv(ruta_csv_2)

#PROGRAMA

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

#HIPOTESIS_1 

print("HIPOTESIS 1: Los países con mayor intensidad energética tienen un menor grado de eficiencia económica.")
time.sleep(2)
print(" ")
print(" ")

df_energy_3 = df_limpio.dropna(subset=['gdp_per_capita'])#Elimino los paises que tienen Nulo gpd per capita

df_energy_3[df_energy_3["Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)"].isna()]["Entity"].drop_duplicates()

df_energy_4 = df_energy_3[df_energy_3['Entity'] != 'New Caledonia']
df_energy_4[df_energy_4["Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)"].isna()]["Entity"].drop_duplicates()

df_energy_4['Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)'] = df_energy_4.groupby('Entity')['Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)'].transform(lambda x: x.fillna(x.mean()))
df_energy_4[df_energy_4["Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)"].isna()]["Entity"].drop_duplicates()

import warnings
warnings.filterwarnings("ignore")

import os

#path=input("introduce el path:")
#name=input("nombre carpeta:")
#os.chdir(path)
#os.mkdir(name)

imagen_h1_1 = sns.lmplot(
    x="gdp_per_capita",
    y="Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)",
    data=df_energy_4,
    hue="Year",
    fit_reg=False,
    height=6
   )

plt.xlim(0, 140000)
plt.ylim(0, 35)
plt.title("INTENSIDAD ENERGÉTICA VS PIB PER CÁPITA", fontsize=14)
plt.xlabel("PIB per cápita (USD PPP 2017)")
plt.ylabel("Intensidad energética (MJ/USD PPP 2017)")
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h1_1")
#plt.savefig(r"path\name\grafico_h1_1.png")
print("")
print("")
print("Se ha cargado el grafico_h1_1")
time.sleep(5)
#plt.show()
print("La hipótesis 1 se confirma: cuanta menor renta per capita tiene un pais, mayor intensidad energética, esto es, se necesita más energía para producir lo mismo.")

print("_________________________________________________________________________")

#HIPOTESIS_2
print(" ")
time.sleep(2)
print("HIPOTESIS 2: Los países que generan más electricidad a partir de combustibles fósiles tienden a tener mayores emisiones de CO₂.")
time.sleep(2)
print(" ")
print(" ")
df_energy_5_5=df_energy_4.copy()
df_energy_5_5['Value_co2_emissions_kt_by_country'] = df_energy_5_5.groupby('Entity')['Value_co2_emissions_kt_by_country'].transform(lambda x: x.fillna(x.mean()))
df_energy_5_5 = df_energy_5_5.dropna(subset=['Value_co2_emissions_kt_by_country'])

imagen_h2_1 = sns.lmplot(
    x="Electricity from fossil fuels (TWh)",
    y="Value_co2_emissions_kt_by_country",
    data=df_energy_4,
    hue="Year",
    #fit_reg=False,
    height=6
   )
plt.xlim(0, 6000)
plt.ylim(0, 12000000)
plt.title("EMISIONES DE CO2 VS ELECTRICIDAD COMBUSTIBLES FOSILES", fontsize=14)
plt.xlabel("Electricidad combustibles fósiles (TWh)")
plt.ylabel("Emisiones de CO2 por pais (kt)")
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h2_1")
print("")
print("")
print("Se ha cargado el grafico_h2_1")
time.sleep(5)
#plt.show()
print("La hipótesis 2 se confirma: Los países que generan más electricidad a partir de combustibles fósiles tienden a tener mayores emisiones de CO₂.")

print("_________________________________________________________________________")

#HIPOTESIS_3
print(" ")
time.sleep(2)
print("HIPOTESIS 3: El acceso a combustibles limpios para cocinar está positivamente correlacionado con el nivel de desarrollo económico.")
time.sleep(2)
print(" ")
print(" ")
df_energy_7 = df_energy_3.dropna(subset=['Access to clean fuels for cooking'])

imagen_h3_1 = sns.lmplot(
    x="gdp_per_capita",
    y="Access to clean fuels for cooking",
    data=df_energy_7,
    hue="Year",
    fit_reg=False,
    height=6
   )

plt.xlim(0, 25000)
#plt.ylim(0, 12000000)
plt.title("% ACCESO A COMBUSTIBLES LIMPIOS PARA COCINAR VS PIB PER CAPITA", fontsize=14)
plt.xlabel("PIB per capita")
plt.ylabel("% Acceso a combustibles limpios para cocinar")
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h3_1")
print("")
print("")
print("Se ha cargado el grafico_h3_1")
time.sleep(5)
#plt.show()
print("La hipótesis 3 se confirma: El acceso a combustibles limpios para cocinar está positivamente correlacionado con el nivel de desarrollo económico.")

print("_________________________________________________________________________")

#HIPOTESIS_4

#Elimino las lineas con valores NaN
df_energy_8 = df_energy_3.dropna(subset=['Renewable energy share in the total final energy consumption (perc)'])
#Sustituyo los valores NAn por los del año anterior
df_energy_8['Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)'] = (
    df_energy_8.groupby('Entity', group_keys=False)['Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)']
    .apply(lambda x: x.ffill())
)
#Elimino el resto de lines que tienen NaN
df_energy_8 = df_energy_3.dropna(subset=['Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)'])

imagen_h4_1 = sns.lmplot(
    x="Renewable energy share in the total final energy consumption (perc)",
    y="Energy intensity level of primary energy (MJ/dolar2017 PPP GDP)",
    data=df_energy_8,
    hue="Year",
    fit_reg=False,
    height=6
   )

#plt.xlim(0, 25000)
#plt.ylim(0, 12000000)
plt.title("INTENSIDAD ENERGÉTICA VS ENERGIAS RENOVABLES EN EL CONSUMO FINAL", fontsize=14)
plt.xlabel("%_Energias renovables en el consumo final")
plt.ylabel("Intensidad energética")
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h4_1")
print("")
print("")
print("Se ha cargado el grafico_h4_1")
time.sleep(5)
#plt.show()
print("La hipótesis 4 no se confirma: La relación entre la participación de energías renovables y la intensidad energética no es lineal.")

print("_________________________________________________________________________")

#HIPOTESIS_5
imagen_h5_1 = sns.lmplot(
    x="gdp_per_capita",
    y="Financial flows to developing countries (US dolar)",
    data=df_energy_3,
    hue="Year",
    fit_reg=False,
    height=6
   )

#plt.xlim(0, 25000)
#plt.ylim(0, 12000000)
plt.title("FLUJOS FINANCIEROS A PAISES EN DESARRROLLO VS PIB PER CÁPITA (US$)", fontsize=14)
plt.xlabel("PIB per capita (US$)")
plt.ylabel("Flujos financieros a paises en desarrollo (US$)")
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h5_1")
print("")
print("")
print("Se ha cargado el grafico_h5_1")
time.sleep(5)
#plt.show()
print("La hipótesis 5 se confirma: Los paises más ricos son los que compran mas creditos de carbono. Y los mas pobres los que los venden.")
print("Se generan otros gráficos aclaratorios")

#graficos de tarta
#incluye todos los años del estudio
flows_por_pais = df_energy_3.groupby("Entity")["Financial flows to developing countries (US dolar)"].sum()
flows_por_pais = flows_por_pais[flows_por_pais > 0]
flows_por_pais = flows_por_pais.sort_values(ascending=False)
flows_top25 = flows_por_pais.head(25)
plt.figure(figsize=(8, 8))
plt.pie(flows_top25, labels=flows_top25.index, autopct='%1.1f%%', startangle=140)
plt.title("Top 25 países por dinero recibido_25 años")
plt.axis('equal') 
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h5_2")
print("")
print("")
print("Se ha cargado el grafico_h5_2")
time.sleep(5)
#plt.show()

#incluye todos los años del estudio
flows_por_pais = df_energy_3.groupby("Entity")["gdp_per_capita"].sum()
flows_por_pais = flows_por_pais.sort_values(ascending=True)
flows_top25 = flows_por_pais.head(25)

plt.figure(figsize=(8, 8))
plt.pie(flows_top25, labels=flows_top25.index, autopct='%1.1f%%', startangle=140)
plt.title("Top 25 países con menor PIB_20 años")
plt.axis('equal')  
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h5_3")
print("")
print("")
print("Se ha cargado el grafico_h5_3")
time.sleep(5)
#plt.show()

#incluye solo el año 2019
df_2019 = df_energy_3[df_energy_3["Year"] == 2019]

flows_por_pais = df_2019.groupby("Entity")["Financial flows to developing countries (US dolar)"].sum()
flows_por_pais = flows_por_pais.sort_values(ascending=False)
flows_top25 = flows_por_pais.head(25)

plt.figure(figsize=(8, 8))
plt.pie(flows_top25, labels=flows_top25.index, autopct='%1.1f%%', startangle=140)
plt.title("Top 25 países que más flujos financieros recibieron (2019)")
plt.axis('equal')  
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h5_4")
print("")
print("")
print("Se ha cargado el grafico_h5_4")
time.sleep(5)
#plt.show()

#incluye solo el año 2019
df_2019 = df_energy_3[df_energy_3["Year"] == 2019]
flows_por_pais = df_2019.groupby("Entity")["gdp_per_capita"].sum()
flows_por_pais = flows_por_pais.sort_values(ascending=True)
flows_top25 = flows_por_pais.head(25)

plt.figure(figsize=(8, 8))
plt.pie(flows_top25, labels=flows_top25.index, autopct='%1.1f%%', startangle=140)
plt.title("Top 25 países con menor PIB per cápita (2019)")
plt.axis('equal')  
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h5_5")
print("")
print("")
print("Se ha cargado el grafico_h5_5")
time.sleep(5)
#plt.show()

print("_________________________________________________________________________")

#HIPOTESIS_6
imagen_h6_1 = sns.lmplot(
    x="Value_co2_emissions_kt_by_country",
    y="Financial flows to developing countries (US dolar)",
    data=df_energy_3,
    hue="Year",
    fit_reg=False,
    height=6
   )

#plt.xlim(0, 25000)
#plt.ylim(0, 12000000)
plt.title("FLUJOS FINANCIEROS A PAISES EN DESARRROLLO VS EMISIONES DE CO2 POR PAIS", fontsize=14)
plt.xlabel("Emisiones de CO2 por pais")
plt.ylabel("Flujos financieros a paises en desarrollo (US$)")
plt.tight_layout()
plt.savefig("ENERGIA\graficos\grafico_h6_1")
print("")
print("")
print("Se ha cargado el grafico_h6_1")
time.sleep(5)
#plt.show()
print("La hipótesis 6 se confirma:  Los paises ricos emiten más CO2 que lo compensan con la compra de creditos de carbono.")

print("_________________________________________________________________________")
print("")
print("Estudio de Energía finalizado")