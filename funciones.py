import pandas as pd 
import numpy as np
from IPython.display import display
# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables

import scipy.stats as stats
from scipy.stats import chi2_contingency, ttest_ind

def cargar_csv(url):  #Función que nos permite cargar el csv para crear el DataFrame
    
    df = pd.read_csv(url)
    
    return df

def propiedades(df):  
    
    ''' Funcion que nos indica las distintas propiedades del Dataframe que recibe como parámetro. '''
    
    #Vemos las primeras lineas del DataFrame
    
    print(f"Las primeras lineas del DataFrame son:") 
    display(df.head(5))
    
    
    #Vemos las cantidad de filas y columnas del DataFrame Vuelos
    
    print(f"El Dataframe de tiene {df.shape[0]} filas y {df.shape[1]} columnas")
    
    print("***************************************************")
    
    #vemos los duplicados que existen en el Dataframe
    
    print(f"Los duplicados que tenemos en el conjunto de datos son: {df.duplicated().sum()}")
    
    print("**************************************************************")
    
    print(f"Los valores nulos que tenemos en el conjunto de datos son: {df.isnull().sum()}")
    
    print("********************************************************************************")
    
    print(f"Si vemos los nulos en forma de porcentaje:")
    
    # lo primero que vamos a hacer es calcular el porcentaje de nulos que tenemos para cada columna
    
    porc_nulos = (df.isnull().sum() / df.shape[0]) * 100
    
    # lo convertimos a DataFrame
    
    df_nulos = pd.DataFrame(porc_nulos, columns = ["%_nulos"])
    
    #filtramos el DataFrame para quedarnos solo con aquellas columnas que tengan nulos
    
    display(df_nulos[df_nulos["%_nulos"] > 0])
    
    
    print("********************************************************************************")
    
    print(f"El Dataframe tiene los siguientes datos:") 
    display(df.info())
    
    print("********************************************************************************")
    
    print("Los valores estadisticos son: ")
    display(df.describe().T)
    
    print("********************************************************************************")
    
    #Analizamos las columnas del Dataframe Vuelos
    
    print("El listado de columnas es:")
    print("")
    
    display(df.columns)
    
    print("********************************************************************************")
    
    for column in df.columns:     #Nos muestra todas las columnas y los valores unicos de cada una de ellas.
  
        print(f"Columna: {column}")
        print(df[column].unique())

    print("\n--------------------\n")
    
    
def quitar_duplicados(df,sobreescribir):   
    
    ''' Función que nos permite quitar los duplicados en un DataFrame. Nota: Esta función elimina y sobreescribe el Dataframe 
    original si le pasamos el parametro true y devuelve un nuevo DataFrame sino queremoms trabajar sobre el original.
     Parámetros:
          dataframe (DataFrame): El DataFrame que contiene los datos.
          sobreescribir (str): Toma el valor True o False según queremos o no modificar el dataframe original.
    '''
    
    if sobreescribir == True:
        
        df.drop_duplicates(inplace=sobreescribir)
        return df
    
    else:
        df_no_duplicados= df.drop_duplicates(inplace=sobreescribir)
        return df_no_duplicados
    
    #Comprobamos que se han eliminado todos los duplicados
    
    print(f"Ya no quedan mas duplicados: {df.duplicated().sum()}")
    
    return df

def cambiar_valores_NaN (df,columna,valor): 
    
    ''' Función con la que rellenamos los valores NaN de una columna con el valor que queramos, para ello lo pasamos por parámetro.
        Parámetros:
          dataframe (DataFrame): El DataFrame que contiene los datos.
          columna (str): El nombre de la columna en el DataFrame que se va a sustituir.
          valor (str) Valor por el que se van a sustituir los valores NaN'''
    
    df[columna] = df[columna].fillna(valor)
    return df


def ver_duplicados(df):   
    
    '''Esta función nos permite ver los duplicados de un DataFrame.'''
    
    for col in df.columns:
        
        print(f"Los duplicados de la columna {col} son: {df[col].duplicated().sum()}")
        

def conversion_tipos(df,columna,tipo_destino):  
    
    ''' Con esta función convertimos el valor de la columna al tipo que se indican en los parámetros.
    
        Parámetros:
        dataframe (DataFrame): El DataFrame que contiene los datos.
        columna (str): El nombre de la columna en el DataFrame que se va a convertir.
        tipo_destino (str) El tipo de dato al que vamos a convertir la columna'''
    
    # Convierte la columna al tipo indicado
    df[columna] = df[columna].astype(tipo_destino)
    
    return df[columna]

def fusionar_dfs(df1,df2,columna,como):   # Esta función nor permite fusionar dos Dataframe.
    
    return pd.merge(df1, df2, on=columna, how=como)
    
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
        
def homogeneidad (columna1, columna2):
    
    """
    Evalúa la homogeneidad de las varianzas entre grupos para una métrica específica en un DataFrame dado.

    Parámetros:
    - columna1 (str): El nombre de la columna con los datos de un grupo.
    - columna2 (str): El nombre de la columna con los datos del otro grupo de estudio.

    Returns:
    No devuelve nada directamente, pero imprime en la consola si las varianzas son homogéneas o no entre los grupos.
    Se utiliza la prueba de Levene para evaluar la homogeneidad de las varianzas. Si el valor p resultante es mayor que 0.05,
    se concluye que las varianzas son homogéneas; de lo contrario, se concluye que las varianzas no son homogéneas.
    """
     
    statistic, p_value = stats.levene(columna1,columna2)
    if p_value > 0.05:
        print(f"Las varianzas son homogéneas entre grupos.")
    else:
        print(f"Las varianzas no son homogéneas entre grupos.")


# vamos a crear una función para calcular este test y ver si hay diferencias entre los grupos de estudio

def test_man_whitney(columna1,columna2):

    """
    Realiza la prueba de Mann-Whitney U para comparar las medianas de las métricas entre dos grupos en un DataFrame dado.
 
    Parámetros:
    - columna1 (str): El nombre de la columna con los datos de un grupo.
    - columna2 (str): El nombre de la columna con los datos del otro grupo de estudio.

    Returns 
    No devuelve nada directamente, pero imprime en la consola si las medianas son diferentes o iguales para cada métrica.
    Se utiliza la prueba de Mann-Whitney U para evaluar si hay diferencias significativas entre los grupos.
    """
          
    # aplicamos el estadístico
    statistic, p_value = stats.mannwhitneyu(columna1,columna2)
               
    if p_value < 0.05:
        print(f"Hay diferencias significativas entre las medianas de las muestras")
    else:
        print(f"No hay evidencia suficiente para concluir que las medianas son diferentes")
            