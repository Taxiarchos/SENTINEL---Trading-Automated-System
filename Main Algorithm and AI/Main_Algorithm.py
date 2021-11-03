import pandas as pd
import yfinance as yf
import nbformat
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from Technical_Indicators import MA_signal_Fermat
from Technical_Indicators import Bollinger_Signal
from Technical_Indicators import RSI_Signal
from Technical_Indicators import CMO_Signal
from SENTINEL/'DATA MINING'/'STOCK DATA'/Stock_Price_Info import Stock_List_Gen



def SENTINEL(ticker_list):                                                          #this is the long output version of the SENTINEL function
    DEFINITIVE = "NO SIGNAL"                                                        #this one will indeed generate a nested list with the output
                                                                                    #of the SENTINEL function for each price from beginning to end
    historical_price_list = Stock_List_Gen(ticker_list)                             #of each stock in the input list. All these values will be used to 
                                                                                    #train and test the machine learning classification model based on KNN 
    Signal_list = []                                                                
    Signal_matrix = []
    Final_Signal = []

    for i in range(0,len(ticker_list)):
        closing_price = historical_price_list[i]

        ind0 = MA_signal_Fermat(closing_price)
        ind1 = Bollinger_Signal(closing_price)
        ind2 = RSI_Signal(closing_price)
        ind3 = CMO_Signal(closing_price)
        
        Signal_list = [ind0,ind1,ind2,ind3]
        Signal_matrix.append(Signal_list)
    
    perfection = len(Signal_list)
    reliability = int(float(70*len(Signal_list))/100.0)

    for i in range(0,len(ticker_list)):
        indicator_length = []
        for l in range(0,4):
            indicator_length.append(len(Signal_matrix[i][l]))
        ind = min(indicator_length)
        for k in range(0,ind):
            nbuys= 0
            nsells= 0
            nosignals= 0
            for n in range(0,4):
                value = Signal_matrix[i][n][k]

                if(value == 'BUY'):
                    nbuys = nbuys + 1
                elif(value == 'SELL'):
                    nsells = nsells + 1
                elif(value == 'NO SIGNAL'):
                    nosignals = nosignals + 1
            if(nbuys >= reliability and nbuys < perfection):
                DEFINITIVE = 'BUY'
                Final_Signal.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
            elif(nsells >= reliability and nsells < perfection):
                DEFINITIVE = 'SELL'
                Final_Signal.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
            elif(nbuys == perfection):
                DEFINITIVE = 'LEVERAGE-BUY'
                Final_Signal.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
            elif(nsells == perfection):
                DEFINITIVE = 'LEVERAGE-SELL'
                Final_Signal.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
            else:
                DEFINITIVE = 'NO SIGNAL'
    
    return(Final_Signal)







def SENTINEL_REDUX(ticker_list):                             #this is the function to create the signal for actually buy and sell assets
    DEFINITIVE = "NO SIGNAL"                                 #infact, only the last signal is returned
    
    historical_price_list = Stock_List_Gen(ticker_list)

    Signal_list = []
    Signal_matrix = []
    Final_Signal = []

    for i in range(0,len(ticker_list)):
        closing_price = historical_price_list[i]

        ind0 = MA_signal_Fermat(closing_price)
        ind1 = Bollinger_Signal(closing_price)
        ind2 = RSI_Signal(closing_price)
        ind3 = CMO_Signal(closing_price)
        
        Signal_list = [ind0,ind1,ind2,ind3]
        Signal_matrix.append(Signal_list)
    
    perfection = len(Signal_list)
    reliability = int(float(70*len(Signal_list))/100.0)
    Final_value_Matrix = []

    for i in range(0,len(ticker_list)):
        indicator_length = []
        for l in range(0,4):
            indicator_length.append(len(Signal_matrix[i][l]))
        ind = min(indicator_length)
        for k in range(0,ind):
            nbuys= 0
            nsells= 0
            nosignals= 0
            for n in range(0,4):
                value = Signal_matrix[i][n][k]

                if(value == 'BUY'):
                    nbuys = nbuys + 1
                elif(value == 'SELL'):
                    nsells = nsells + 1
                elif(value == 'NO SIGNAL'):
                    nosignals = nosignals + 1
            if(nbuys >= reliability and nbuys < perfection):
                DEFINITIVE = 'BUY'
                Final_Signal.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
            elif(nsells >= reliability and nsells < perfection):
                DEFINITIVE = 'SELL'
                Final_Signal.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
            elif(nbuys == perfection):
                DEFINITIVE = 'LEVERAGE-BUY'
                Final_Signal.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
            elif(nsells == perfection):
                DEFINITIVE = 'LEVERAGE-SELL'
                Final_Signal.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
            else:
                DEFINITIVE = 'NO SIGNAL'
                Final_Signal.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
                
        if(k==(ind-1)):
            Final_value_Matrix.append([ticker_list[i], DEFINITIVE, historical_price_list[i][k]])
    
    return(Final_value_Matrix)
