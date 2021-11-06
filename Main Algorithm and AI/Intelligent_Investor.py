import Main_Algorithm import SENTINEL_REDUX, SENTINEL_and_Indicators_output
from Efficiency_Testing import Test_Efficiency_for_Machine_Learning
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd


ticker_list = ['MSFT','MC','FB','TSLA','PYPL']
OUTPUT = Test_Efficiency_for_Machine_Learning(ticker_list)




