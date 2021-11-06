import Main_Algorithm import SENTINEL, SENTINEL_and_Indicators_output
from Efficiency_Testing import Test_Efficiency_for_Machine_Learning


ticker_list = ['MSFT','MC','FB','TSLA','PYPL']
OUTPUT = Test_Efficiency_for_Machine_Learning(ticker_list)

for i in range(0,len(OUTPUT)):
  for j in range(0,13):
    if(OUTPUT[i][j] == 'SELL'):
      OUTPUT[i][j] == 1
    elif(OUTPUT[

def Intelligent_Investor(OUTPUT):


