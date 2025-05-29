# ENERGÍA EN EL MUNDO


![torre](https://github.com/user-attachments/assets/101e80d8-93bc-4ba3-8d0b-994313ebc04d)
![molinos](https://github.com/user-attachments/assets/0ecdc803-f33d-4bd7-ab08-f3b41d4cb3cd)


## 🌍 Introducción

Actualmente, los países enfrentan una presión creciente por reducir sus emisiones de gases de efecto invernadero. Sin embargo, mientras algunos países han avanzado en la transición hacia energías limpias, otros continúan generando grandes cantidades de electricidad a partir de fuentes fósiles. Para compensar sus altos niveles de emisiones, muchos recurren a la compra de créditos de carbono, una herramienta del mercado climático que les permite financiar reducciones de emisiones en otros lugares del mundo.

Este proyecto analiza un conjunto de datos energéticos, medioambientales y económicos a nivel mundial, con el objetivo de identificar qué países tienen altos niveles de generación energética y emisiones de CO₂, y cómo se relacionan con prácticas como la compra de créditos de carbono. Entre los indicadores analizados se encuentran:

- Acceso a electricidad y combustibles limpios

- Capacidad instalada de energía renovable

- Consumo de energía primaria y su intensidad

- Generación eléctrica por fuente (fósil, nuclear, renovable)

- Emisiones anuales de CO₂

- PIB per cápita y crecimiento económico


El análisis busca destacar la paradoja de los países que, a pesar de contar con recursos y tecnología para reducir emisiones, optan por compensarlas económicamente en lugar de reducirlas directamente. Esto abre el debate sobre la eficacia y la equidad de los mercados de carbono, y plantea interrogantes clave sobre la justicia climática y el verdadero compromiso de las economías más contaminantes.

A través de visualizaciones y comparaciones regionales, este proyecto pretende ofrecer una mirada crítica a los patrones de consumo energético, las responsabilidades históricas de emisiones, y el papel que juegan los créditos de carbono en las estrategias de sostenibilidad internacional.

Para más información sobre el mercado de CAP AND TRADE consultad: https://www.c2es.org/content/cap-and-trade-basics/



## 🧠 HIPOTESIS

Las hipotesis planteadas en este proyecto son las siguientes:

1- Los países con mayor intensidad energética tienen un menor grado de eficiencia económica.
Relación entre “Energy intensity level of primary energy” y “gdp_per_capita”.

2- Los países que generan más electricidad a partir de combustibles fósiles tienden a tener mayores emisiones de CO₂.
Relación entre “Electricity from fossil fuels” y “Value_co2_emissions_kt_by_country”.

3- El acceso a combustibles limpios para cocinar está positivamente correlacionado con el nivel de desarrollo económico.
Relación entre “Access to clean fuels for cooking” y “gdp_per_capita”.

4- Los países con mayor participación de energía renovable en el consumo final tienen una menor intensidad energética.
Relación entre “Renewable energy share in the total final energy consumption” y “Energy intensity level of primary energy”.

5- Los paises más ricos son los que compran mas creditos de carbono. Y los mas porbres los que los venden.

6- Los paises ricos emiten más CO2 que lo compensan con la copra de creditos de carbono.


Backup:

7- Los países con mayor acceso a la electricidad tienen un PIB per cápita más alto.
Relación entre “Access to electricity” y “gdp_per_capita”.

8- El incremento en la generación de electricidad a partir de fuentes renovables reduce las emisiones de CO₂.
Relación entre “Electricity from renewables” y “Value_co2_emissions_kt_by_country”.


## 🧑‍💻📊DATOS OBTENIDOS

Se ha obtenido un archivo de nombre global_data.csv en Kaggle que contiene la siguiente información por pais y año:

| Nº | Nombre original (en inglés)                                      | Traducción al español                                              |
| -- | ---------------------------------------------------------------- | ------------------------------------------------------------------ |
| 0  | Entity                                                           | País o entidad                                                     |
| 1  | Year                                                             | Año                                                                |
| 2  | Access to electricity (% of population)                          | Acceso a la electricidad (% de la población)                       |
| 3  | Access to clean fuels for cooking                                | Acceso a combustibles limpios para cocinar                         |
| 4  | Renewable-electricity-generating-capacity-per-capita             | Capacidad per cápita de generación de electricidad renovable       |
| 5  | Financial flows to developing countries (US \$)                  | Flujos financieros a países en desarrollo (US \$)                  |
| 6  | Renewable energy share in the total final energy consumption (%) | Porcentaje de energía renovable en el consumo final de energía (%) |
| 7  | Electricity from fossil fuels (TWh)                              | Electricidad generada a partir de combustibles fósiles (TWh)       |
| 8  | Electricity from nuclear (TWh)                                   | Electricidad generada por energía nuclear (TWh)                    |
| 9  | Electricity from renewables (TWh)                                | Electricidad generada por fuentes renovables (TWh)                 |
| 10 | Low-carbon electricity (% electricity)                           | Electricidad de bajas emisiones de carbono (% del total)           |
| 11 | Primary energy consumption per capita (kWh/person)               | Consumo de energía primaria per cápita (kWh/persona)               |
| 12 | Energy intensity level of primary energy (MJ/\$2017 PPP GDP)     | Intensidad energética de la energía primaria (MJ/\$ PIB PPA 2017)  |
| 13 | Value\_co2\_emissions\_kt\_by\_country                           | Emisiones de CO₂ por país (miles de toneladas)                     |
| 14 | Renewables (% equivalent primary energy)                         | Renovables (% equivalente de energía primaria)                     |
| 15 | gdp\_growth                                                      | Crecimiento del PIB                                                |
| 16 | gdp\_per\_capita                                                 | PIB per cápita                                                     |
| 17 | Density\n(P/Km2)                                                 | Densidad de población (personas/km²)                               |
| 18 | Land Area(Km2)                                                   | Superficie terrestre (km²)                                         |
| 19 | Latitude                                                         | Latitud                                                            |
| 20 | Longitude                                                        | Longitud                                                           |

Los datos van del año 2000 al 2020 e incluyen la información de 176 paises, de diferentes continentes y variado PIB.


## 💭📈RESUMEN DE GLOBAL DATA CSV


El análisis busca destacar la paradoja de los países que, a pesar de contar con recursos y tecnología para reducir emisiones, optan por compensarlas económicamente en lugar de reducirlas directamente. Esto abre el debate sobre la eficacia y la equidad de los mercados de carbono, y plantea interrogantes clave sobre la justicia climática y el verdadero compromiso de las economías más contaminantes.

A través de visualizaciones y comparaciones regionales, este proyecto pretende ofrecer una mirada crítica a los patrones de consumo energético, las responsabilidades históricas de emisiones, y el papel que juegan los créditos de carbono en las estrategias de sostenibilidad internacional.

El archivo tiene 21 columnas y 364 filas. Hay informacion de 176 paises desde el año 2000 al año 2020.

En un primer analisis visual entre otros se determina que:
- Existen una cantidad sustancial de celdas con valor NaN.
- Además se ve que la variable Density es un Object y solo tendria que ser numerica.

Tras realizar una revisión de los valores faltantes (NaN) en la tabla, se ha identificado la necesidad de eliminar algunos registros y omitir otros. No se ha llevado a cabo el proceso de limpieza de datos hasta el momento.


## 🧹LIMPIEZA DE DATOS🧽🧼

Ver el archivo "primera_limpieza.ipynb" donde se realiza la limpieza de los datos y se obtiene el archivo primera_limpieza.csv. 

Despues de esta limpieza no se han eliminado todos los NaN para intentar eliminar el menor numero de columas y filas posible. Pero si se ha preparado para poder trabajar con distintos dataframes dependiendo de la hipótesis.



## 🤓ANÁLISIS DE HIPÓTESIS CON DATOS
## HIPOTESIS_1

La hipótesis 1 se confirma: cuanta menor renta per capita tiene un pais, mayor intensidad energética, esto es, se necesita más energía para producir lo mismo.

¿Por qué ocurre esto?
1. Estructura económica más intensiva en energía
    Países con menor renta suelen depender más de sectores como:

    - Agricultura extensiva
    - Industria pesada
    - Minería

    Estos sectores consumen mucha energía y generan menos valor agregado por unidad de energía.

2. Tecnología menos eficiente
    - Maquinaria antigua
    - Infraestructura energética ineficiente

  ## HIPOTESIS_2
  La hipótesis 2 se confirma: Los países que generan más electricidad a partir de combustibles fósiles tienden a tener mayores emisiones de CO₂.

Así mismo se detecta que desde el año 2000 al 2019 las emisone de CO2 se han ido reduciendo.

¿Por qué ocurre esto?

Cuando se queman carbón, petróleo o gas natural para generar electricidad, se libera dióxido de carbono (CO₂), un gas de efecto invernadero.

Cuanto mayor sea la proporción de electricidad generada con combustibles fósiles, mayor será la intensidad de emisiones por kWh generado.

El carbón es el combustible más contaminante
Las plantas eléctricas a carbón emiten aproximadamente dos veces más CO₂ por unidad de energía que las de gas natural, y mucho más que las fuentes renovables (que casi no emiten).

📊 Ejemplo real:

India y China → alto porcentaje de generación con carbón → altas emisiones de CO₂ por kWh.

Francia → usa mucha energía nuclear → bajas emisiones relativas.

Islandia o Noruega → energía casi 100% renovable (hidroeléctrica y geotérmica) → emisiones muy bajas del sector eléctrico.

 ## HIPOTESIS_3

 La hipótesis 3 se confirma: El acceso a combustibles limpios para cocinar está positivamente correlacionado con el nivel de desarrollo económico.
Se detecta que a partir de un PIB per capita de 15000$ aproximadamente toda la población tiene acceso a combustibles limpios para cocinar.
Por el contrario, en países con PIB per cápita bajo, el acceso a combustibles limpios para cocinar es limitado, y una gran parte de la población depende de biomasa tradicional (como leña o carbón).

📊 ¿Por qué sucede esto?
- Infraestructura: países con más ingresos tienen redes de gas, electricidad y distribución de combustibles modernos.

- Poder adquisitivo: las familias con bajo poder adquisitivo no pueden costear cocinas modernas y combustibles como gas licuado o electricidad.

## HIPOTESIS_4

La hipótesis 4 no se confirma: 

La relación entre la participación de energías renovables y la intensidad energética no es lineal.

- Los países con baja participación en energías renovables (menos del 10%) suelen tener alta intensidad energética, lo que indica que requieren más energía para generar una unidad de PIB.

- Los países con una participación intermedia de energías renovables (entre el 10% y el 80%) presentan la menor intensidad energética, lo que sugiere un uso más eficiente de los recursos energéticos.

- Por otro lado, algunos países con alta participación en energías renovables (más del 80%) también muestran una elevada intensidad energética, posiblemente porque sus economías dependen de sectores primarios o de baja productividad energética.


📊 ¿Por qué sucede esto?
- Países muy dependientes de energías fósiles no han desarrollado eficiencia energética.

- Países con alta participación renovable pueden tener estructuras económicas basadas en agricultura o industrias menos eficientes.

- Los países intermedios combinan tecnologías limpias con eficiencia productiva y mayor diversificación económica.

- Menor acceso a tecnologías de bajo consumo energético

3. Pérdidas en la conversión y distribución
    - Redes eléctricas menos modernas → más pérdidas en transmisión
    - Uso de fuentes menos eficientes como biomasa tradicional

4. Poca diversificación económica
    Menos sectores de servicios, que suelen ser más eficientes en términos energéticos

📊 Ejemplo real:
    - País de renta alta (como Alemania): puede necesitar 3 MJ para generar 1 dólar del PIB
    - País de renta baja (como Níger): puede necesitar 20 MJ para generar 1 dólar del PIB

## HIPOTESIS_5

La hipótesis 5 se confirma: 

Los paises más ricos son los que compran mas creditos de carbono. Y los mas pobres los que los venden.

En los mercados de carbono, los países con mayores ingresos tienden a ser compradores netos de créditos de carbono, mientras que los países con menores ingresos suelen ser vendedores netos.

Esto se debe a que los países más ricos, al tener mayores emisiones históricas y actuales, necesitan compensar sus emisiones para cumplir con sus metas climáticas. En cambio, muchos países en desarrollo cuentan con proyectos de reducción de emisiones (como reforestación o energías limpias) que pueden generar créditos de carbono y venderlos en el mercado internacional.

🔍 ¿Por qué sucede esto?

- Los países desarrollados emiten más CO₂ per cápita y están sometidos a metas más estrictas en acuerdos como el Acuerdo de París.

- Los países ricos tienen más capacidad para pagar por créditos de carbono en lugar de reducir sus propias emisiones directamente.

- Muchos países en desarrollo tienen grandes áreas forestales, suelos fértiles y potencial para proyectos de conservación o energías limpias que generan créditos de carbono (por ejemplo, REDD+).

- Otros paises simplemente son muy pobres y venden sus creditos de carbono para financierse.


## HIPOTESIS_6
La hipótesis 6 se confirma:  Los paises ricos emiten más CO2 que lo compensan con la compra de creditos de carbono.
Los países más ricos suelen ser responsables de mayores emisiones de CO₂, debido a su alto consumo energético y niveles de industrialización. Para cumplir con sus compromisos climáticos, muchos de ellos recurren a la compra de créditos de carbono como mecanismo de compensación.

🔍 ¿Por qué sucede esto?
- Altas emisiones: Países con grandes sectores industriales, transporte intensivo y alto consumo energético.

- Responsabilidad internacional: Están sujetos a mayores compromisos bajo el Acuerdo de París u otros marcos climáticos.

- Capacidad económica: Tienen los recursos para financiar proyectos de mitigación en otros países a través del mercado de carbono.



