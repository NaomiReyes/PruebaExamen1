# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:39:07 2023

@author: Meva
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import importlib

# importar el archivo de soporte
import market_data
importlib.reload(market_data)

"""
Explicación de la Tarea-Examen 01.

Tu gerente de portafolios quiere que calcules ciertas métricas estadísticas de diferentes portafolios.

Ella te va a dar dos listas:
1. El portafolios, es decir la lista de activos o rics. Digamos que hay N rics.
2. Las métricas que le interesan. Digamos que hay M métricas.

Lo que ella espera que le regrese tu código es:
1. Un dataframe, es decir una tabla, de dimensiones N x (M+1)
2. La primera columna se llama 'rics' y contiene el portafolios o lista de N activos.
3. Las siguientes M columnas son las métricas que te pide, en el orden que te las dio.
4. El redondeo es a 6 decimales.

Notas:
1. Las M métricas son un subconjunto de todas las métricas que calcula la clase distribution.
2. El código debe tomar en cuenta que la lista de métricas puede variar en orden y tamaño.
3. El portafolios o lista de N activos es un subconjunto del universo que hemos bajado de Yahoo Finance
"""

# lista de rics
rics_1 = ['^SPX', '^IXIC', '^MXX', '^STOXX', '^GDAXI', '^FCHI', '^VIX']
rics_2 = ['XLK', 'XLF', 'XLV', 'XLE', 'XLU', 'XLI', 'XLB','XLC']
rics_3 = ['EURUSD=X', 'GBPUSD=X', 'CHFUSD=X', 'SEKUSD=X', 'NOKUSD=X', 'JPYUSD=X', 'MXNUSD=X']
rics_4 = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'USDC-USD', 'USDT-USD', 'DAI-USD']

# lista de métricas
metrics_1 = ['mean_annual', 'volatility_annual', 'skewness', 'kurtosis']
metrics_2 = ['skewness', 'kurtosis', 'jb_stat', 'p_value', 'is_normal']
metrics_3 = ['mean_annual', 'volatility_annual', 'sharpe_ratio', 'var_95']

# inicializar rics y metrics
rics = rics_2
metrics = metrics_3

# función examen para los alumnos
def generate_dataframe_distributions(rics, metrics):
    # metrics es un subconjunto de metrics_full
    metrics_full = ['mean_annual',\
                    'volatility_annual',\
                    'sharpe_ratio',\
                    'var_95',\
                    'skewness',
                    'kurtosis',\
                    'jb_stat',\
                    'p_value',\
                    'is_normal']
    df = pd.DataFrame()
    decimals = 6 # antes de return, redondea a 6 decimales usando np.round(x,decimals)
    # tu código empieza aquí
    # Hint: usa la clase "distribution" para calcular tus métricas estadísticas
    # ...
    #tu código termina aquí
    return df