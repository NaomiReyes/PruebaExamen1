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

#Prueba 3
def test_1_3():
    df_obtenido = generate_dataframe_distributions(rics_1, metrics_3)
    df_esperado = 'unit_tests_01/df_1_3.csv'
    result = pd.read_csv(df_esperado)
    assert_frame_equal(df_obtenido,result)