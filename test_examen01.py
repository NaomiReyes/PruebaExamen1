from pandas.testing import assert_frame_equal
from examen_01 import generate_dataframe_distributions
import pandas as pd

# lista de rics
rics_1 = ['^SPX', '^IXIC', '^MXX', '^STOXX', '^GDAXI', '^FCHI', '^VIX']
rics_2 = ['XLK', 'XLF', 'XLV', 'XLE', 'XLU', 'XLI', 'XLB','XLC']
rics_3 = ['EURUSD=X', 'GBPUSD=X', 'CHFUSD=X', 'SEKUSD=X', 'NOKUSD=X', 'JPYUSD=X', 'MXNUSD=X']
rics_4 = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'USDC-USD', 'USDT-USD', 'DAI-USD']

# lista de métricas
metrics_1 = ['mean_annual', 'volatility_annual', 'skewness', 'kurtosis']
metrics_2 = ['skewness', 'kurtosis', 'jb_stat', 'p_value', 'is_normal']
metrics_3 = ['mean_annual', 'volatility_annual', 'sharpe_ratio', 'var_95']

#Prueba 1
def test_1_1():
    df_obtenido = generate_dataframe_distributions(rics_1, metrics_1)
    df_esperado = 'unit_tests_01/df_1_1.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 2
def test_1_2():
    df_obtenido = generate_dataframe_distributions(rics_1, metrics_2)
    df_esperado = 'unit_tests_01/df_1_2.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 3
def test_1_3():
    df_obtenido = generate_dataframe_distributions(rics_1, metrics_3)
    df_esperado = 'unit_tests_01/df_1_3.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 4
def test_2_1():
    df_obtenido = generate_dataframe_distributions(rics_2, metrics_1)
    df_esperado = 'unit_tests_01/df_2_1.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 5
def test_2_2():
    df_obtenido = generate_dataframe_distributions(rics_2, metrics_2)
    df_esperado = 'unit_tests_01/df_2_2.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 6
def test_2_3():
    df_obtenido = generate_dataframe_distributions(rics_2, metrics_3)
    df_esperado = 'unit_tests_01/df_2_3.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 7
def test_3_1():
    df_obtenido = generate_dataframe_distributions(rics_3, metrics_1)
    df_esperado = 'unit_tests_01/df_3_1.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 8
def test_3_2():
    df_obtenido = generate_dataframe_distributions(rics_3, metrics_2)
    df_esperado = 'unit_tests_01/df_3_2.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 9
def test_3_3():
    df_obtenido = generate_dataframe_distributions(rics_3, metrics_3)
    df_esperado = 'unit_tests_01/df_3_3.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 10
def test_4_1():
    df_obtenido = generate_dataframe_distributions(rics_4, metrics_1)
    df_esperado = 'unit_tests_01/df_4_1.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 11
def test_4_2():
    df_obtenido = generate_dataframe_distributions(rics_4, metrics_2)
    df_esperado = 'unit_tests_01/df_4_2.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

#Prueba 12
def test_4_3():
    df_obtenido = generate_dataframe_distributions(rics_4, metrics_3)
    df_esperado = 'unit_tests_01/df_4_3.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)

