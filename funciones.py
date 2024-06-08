import pandas as pd 
import numpy as np
from IPython.display import display
# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables

import scipy.stats as stats
from scipy.stats import chi2_contingency, ttest_ind

def cargar_csv(url):
    inst
    df = pd.read_csv(url)
    
    return df

def propiedades(df):
    
    #Vemos las cantidad de filas y columnas del DataFrame Vuelos
    print(f"El Dataframe de tiene {df.shape[0]} filas y {df.shape[1]} columnas")
    
    print("**************************************")
    
    #vemos los duplicados que existen en el Dataframe
    
    print(f"Los duplicados que tenemos en el conjunto de datos son: {df.duplicated().sum()}")
    
    print("**************************************")
    
    print(f"Los valores nulos que tenemos en el conjunto de datos son: {df.isnull().sum()}")
    
    print(f"El Dataframe tiene los siguientes datos:") 
    display(df.info())
    
    print("**************************************")
    
    print("Los valores estadisticos son: ")
    display(df.describe().T)
    
    print("**************************************")
    
def quitar_duplicados(df):
    
    df.drop_duplicates(inplace=True)
    
    #Comprobamos que se han eliminado todos los duplicados
    
    print(f"Ya no quedan mas duplicados: {df.duplicated().sum()}")
    
    return df

def cambiar_valores_NaN (df,columna):
    
    df[columna] = df[columna].fillna(0)
    return df


def ver_duplicados(df):
    
    for col in df.columns:
        
        print(f"Los duplicados de la columna {col} son: {df[col].duplicated().sum()}")
        

def conversion_tipos(df,columna,tipo_destino):
    
   # Convierte la columna al tipo indicado
        df[columna] = df[columna].astype(tipo_destino)
    
        return df[columna]
    
def normalidad(dataframe, columna):
    """
    Evalúa la normalidad de una columna de datos de un DataFrame utilizando la prueba de Shapiro-Wilk.

    Parámetros:
        dataframe (DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en el DataFrame que se va a evaluar para la normalidad.

    Returns:
        None: Imprime un mensaje indicando si los datos siguen o no una distribución normal.
    """

    statistic, p_value = stats.shapiro(dataframe[columna])
    if p_value > 0.05:
        print(f"Para la columna {columna} los datos siguen una distribución normal.")
    else:
        print(f"Para la columna {columna} los datos no siguen una distribución normal.")