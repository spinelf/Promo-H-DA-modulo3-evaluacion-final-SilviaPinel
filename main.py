# Importamos las librerias necesarias para la elaboración del ejercicio

import funciones as func
import pandas as pd 
import numpy as np 

# Ejercicio Final Módulo 3

# para poder visualizar todas las columnas de los DataFrames

pd.set_option('display.max_columns', None)

# Ponemos las referencias de los dos archivos csv que están en el repositorio.

url1_data_customer_flight="https://raw.githubusercontent.com/spinelf/Promo-H-DA-modulo3-evaluacion-final-SilviaPinel/main/Customer%20Flight%20Activity.csv"
url2_data_customer_loyalty="https://raw.githubusercontent.com/spinelf/Promo-H-DA-modulo3-evaluacion-final-SilviaPinel/main/Customer%20Loyalty%20History.csv"

# Leemos los csv y almacenamos los datos en dos dataframes:

data_customer_vuelos = func.cargar_csv(url1_data_customer_flight)

data_customer_fidelidad = func.cargar_csv(url2_data_customer_loyalty)

### Fase 1: Exploración y Limpieza

