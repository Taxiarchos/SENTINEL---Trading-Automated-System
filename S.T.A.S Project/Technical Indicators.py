from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd



def Stock_info():
  stock_name = input("Enter the ticker symbol (the code) of the stock you want to analyze: ")
  msft = yf.Ticker(stock_name)
  print("Now, a description of the stock and the company...\n")

  info=[["Info", msft.info],["historical market data", msft.history(period="max")],["Actions", msft.actions],["Dividends", msft.dividends],["Splits", msft.splits],["Financials", msft.financials],
        ["Quarterly financials", msft.quarterly_financials],["Major holders", msft.major_holders],["Institutional holders", msft.institutional_holders],["Balance sheet", msft.balance_sheet],
        ["Quarterly Balance sheet", msft.quarterly_balance_sheet], ["Cash Flow", msft.cashflow], ["Quarterly cash flow", msft.quarterly_cashflow], ["Earnings", msft.earnings],
        ["Quarterly earnings", msft.quarterly_earnings], ["Sustainability", msft.sustainability],  ["Recommendations", msft.recommendations], ["Calendar of next events", msft.calendar],
        ["Options expirations", msft.options]]

  for i in range(0,19):            #questo ciclo for scrive il nome del dataset e il dataset
      print(info[i][0])            #tipo "info" seguito dal dataset msft.info, "historical market data" seguito da msft.history(period="max")
      dataset=pd.DataFrame(info[i][1])
      print(dataset)
      print("\n")

      
def Stock_plot():
  stock_price=pd.DataFrame(info[1][1])
  stock_price.reset_index(inplace=True)

  closing_price=stock_price["Close"]   #stock_price[close] viene salvato in closing_price perchè servirà spesso più avanti!!
  Date=stock_price["Date"]

  stockplot = px.line(x=Date, y=closing_price, labels=dict(x="Date", y="Price"))
  stockplot.show()
  
  
def MobileAverage(MArange,closing_price):                            #Creazione della media mobile , cerca la formula su wikipedia della media mobile per capirla
  while (MArange >= len(closing_price)):
    print("the range is too wide, we advice using no more than 250 days...")
    MArange

  MA=[]

  for i in range(0,len(closing_price)):
    if((len(closing_price)-(i+MArange)) <= 0):
      value=closing_price[i:len(closing_price)].mean()
      MA.append(value)
    else:
      value=closing_price[i:i+MArange].mean()
      MA.append(value)

  return MA


def MA_signal_Fermat(closing_price):                  #segnale per capire se la media mobile si flette cambiando da crescente a
    Presignal_List = []                  #decrescente o viceversa usando il teorema di Fermat
    MA10 = MobileAverage(10,closing_price)
    for i in range(0,len(MA10)-1):
        for k in range(i,len(MA10)-1):
                if((MA10[i+1] - MA10[i]) > 0 and (MA10[k+1] - MA10[k]) < 0):    
                    PreSignal = 'SELL'
                    Presignal_List.append(PreSignal)
                    break
                elif((MA10[i+1] - MA10[i]) < 0 and (MA10[k+1] - MA10[k]) > 0):
                    PreSignal = 'BUY'
                    Presignal_List.append(PreSignal)
                    break
                elif(k==(len(MA10)-3)):
                    PreSignal = 'NO SIGNAL'
                    Presignal_List.append(PreSignal)
                    
    return Presignal_List
 


def Triple_MA(closing_price):                             #riceve 3 interi e restituisce tre medie mobili
  NumOfMA=input("Number of MA: ")          #una per ogni periodo, il periodo è definito dagli interi
  NumOfMA = int(NumOfMA)
  MArangeList = []
  MA_list = []

  for i in range(0, NumOfMA):    
      MArange = input("Insert the time period: ")
      MArange = int(MArange)
      MArangeList.append(MArange)
      MA = MobileAverage(MArangeList[i],closing_price)
      MA_list.append(MA)

  return MA_list


def Triple_Crossover_Signal(closing_price):               #l'intersezioni della media mobile breve con quella media da un segnale buy o sell
    NumOfMA=3                                #in base al fatto che la media breve arrivi da su o da giù
    MArangeValues=[4,9,18]                   #La media mobile breve tocca la lunga e da un altro segnale
    MArangeList = []                         #la media mobile media tocca la lunga e crea un segnale buy o sell
    MA_list = []                             #3 segnali sell danno un sell
    Signal_matrix = []                       #3 segnali buy danno un buy
    Signal_list = []                         #negli altri casi, nessun segnale
    n_buys = 0
    n_sells = 0
    Final_signal_list = []
    
    for i in range(0, NumOfMA):    
        MArange = MArangeValues[i]
        MArangeList.append(MArange)
        MA = MobileAverage(MArangeList[i],closing_price)
        MA_list.append(MA)
    
    for i in range(1,len(MA_list[0])):
        for j in range(0,NumOfMA-1):
            Presignal = 'NO SIGNAL'
            for k in range(0,i):
                if((MA_list[j][i-k] > MA_list[j+1][i-k]) and (MA_list[j][i] <= MA_list[j+1][i])):
                    Presignal = 'SELL'
                elif(j==0 and (MA_list[j][i-k] > MA_list[j+2][i-k]) and (MA_list[j][i] <= MA_list[j+2][i])):
                    Presignal = 'SELL'
                elif(j==0 and (MA_list[j][i-k] < MA_list[j+2][i-k]) and (MA_list[j][i] >= MA_list[j+2][i])):
                    Presignal = 'BUY'
                elif((MA_list[j][i-k] < MA_list[j+1][i-k]) and (MA_list[j][i] >= MA_list[j+1][i])):
                    Presignal = 'BUY'
            if(Presignal != 'BUY' and Presignal != 'SELL'):    
                Presignal = 'NO SIGNAL'
            else:
                Signal_list.append(Presignal)
        Signal_matrix.append(Signal_list)
        Signal_list = []
    
    for v in range(0,len(Signal_matrix)):
        for n in range(0,len(Signal_list)):
            if(Signal_list[n] == 'BUY'):
                ++n_buys
            elif(Signal_list[n] == 'SELL'):
                ++n_sells
            else:
                continue
        if(n_buys == 3 ):
            Final_signal = 'BUY'
        elif(n_sells == 3):
            Final_signal = 'SELL'
        else:
            Final_signal = 'NO SIGNAL'
        Final_signal_list.append(Final_signal)
        
    return Final_signal_list
  
  
def Simple_Crossover_Signal(closing_price):                           #Questo segnale è migliore del triple crossover signal
  NumOfMA=2                                            #e' una intersezione semplice tra due medie mobili e funziona meglio del  
  MArangeValues=[25,35]                                #triplo crossover, anche se questo funziona meglio con i future su commodities
  MArangeList = []
  MA_list = []
  Signal_list = []

  for i in range(0, NumOfMA):    
      MArange = MArangeValues[i]
      MArangeList.append(MArange)
      MA = MobileAverage(MArangeList[i],closing_price)
      MA_list.append(MA)

  for i in range(1,len(MA_list[0])):
          j=0
          if((MA_list[j][i-1] > MA_list[j+1][i-1]) and (MA_list[j][i] <= MA_list[j+1][i])):
              Presignal = 'SELL'
          elif((MA_list[j][i-1] < MA_list[j+1][i-1]) and (MA_list[j][i] >= MA_list[j+1][i])):
              Presignal = 'BUY'
          else:
              Presignal = 'NO SIGNAL'
          Signal_list.append(Presignal)

  return Signal_list


def MAplot():
    fig = make_subplots(rows=1, cols=1)
    NumOfMA=input("Number of MA: ")
    NumOfMA = int(NumOfMA)
    MArangeList = []
    
    for i in range(0, NumOfMA) :
        MArange = input("Insert the time period: ")
        MArange = int(MArange)
        MArangeList.append(MArange)
        MA = MobileAverage(MArangeList[i],closing_price)
        title = "Mobile Av. " + str(MArangeList[i]) + " days"
        fig.add_trace(go.Scatter(name= title, x=Date, y=MA), row=1, col=1)
        
    fig.add_trace(go.Scatter(name="Stock Price", x=Date, y=closing_price), row=1, col=1)
    
    return fig
  
  
def Bollinger(closing_price):                              #crea le bande di bollinger
    import math
    BigDS = []
    MiniDS = []
    SqrdErr=0
    BollingerMA=MobileAverage(20,closing_price)
    for i in range(0,len(closing_price)):
        SqrdErr = SqrdErr + ((closing_price[i] - closing_price.mean())**2)     #errore quadrato
        if(i==0):
            continue
        else:
            DS = math.sqrt((SqrdErr)/len(closing_price[0:i]))                   #deviazione standard
        BigDS.append(BollingerMA[i] + (0.2*DS) )
        MiniDS.append(BollingerMA[i] - (0.2*DS) )     #fattore di attualizzazione 0.6 che moltiplica la deviazione standard
    DS_Matrix = [BigDS,BollingerMA,MiniDS]            #di solito il fattore è = a 3, ma con 0.6 sembra funzionare meglio
    
    return DS_Matrix
  
  
def Bollinger_Signal(closing_price):                                       #quando il prezzo tocca la banda alta si vende
    Signal_list = []                                          #quando tocca la banda bassa si compra
    Bollinger_output = Bollinger(closing_price)
    for i in range(0, len(closing_price)):
        if(closing_price[i] > Bollinger_output[1][i]):
            Final_signal = 'SELL'
        elif(closing_price[i] < Bollinger_output[1][i]):
            Final_signal = 'BUY'
        elif(closing_price[i] == Bollinger_output[1][i]):
            Final_signal = 'NO SIGNAL'
        Signal_list.append(Final_signal)
    
    return Signal_list
  
  
def Bollinger_plot():
    
    fig = make_subplots(rows=1, cols=1)
    DS_Matrix = Bollinger(closing_price)
    
    fig.add_trace(go.Scatter(name="Stock Price", x=Date, y=closing_price), row=1, col=1)
    fig.add_trace(go.Scatter(name="Big Bollinger Band", x=Date, y=DS_Matrix[0]), row=1, col=1)
    fig.add_trace(go.Scatter(name="Bollinger 20 days mobile average", x=Date, y=DS_Matrix[1]), row=1, col=1)
    fig.add_trace(go.Scatter(name="Little Bollinger Band", x=Date, y=DS_Matrix[2]), row=1, col=1)
    
    return fig


def RSI(closing_price,flag=True):                               #cerca su wikipedia la formula del Relative Strenght Index
    import pandas as pd                                 
    
    if(flag):
        timeframe_int = 14
        timeframe = float(timeframe_int)
    else:
        timeframe_int = input("Choose the time period for the RSI (We advice to use 14 days): ")
        timeframe = float(timeframe_int)
    
    Bigdiff_list = []
    Lildiff_list = []
    RSI_list = []
    
    for i in range(0,len(closing_price)):
        if (i==0):
            closing_price_diff_major = 0
            closing_price_diff_major = 0
        else:
            if (closing_price[i] > closing_price[i-1]):
                closing_price_diff_major = closing_price[i] - closing_price[i-1]
                Bigdiff_list.append(closing_price_diff_major)
                Lildiff_list.append(0)
            elif (closing_price[i] < closing_price[i-1]):
                closing_price_diff_minor = closing_price[i-1] - closing_price[i] 
                Lildiff_list.append(closing_price_diff_minor)
                Bigdiff_list.append(0)
            elif (closing_price[i] == closing_price[i-1]):
                Lildiff_list.append(0)
                Bigdiff_list.append(0)
            
            if (i-timeframe < 0):
                Major_Average = sum(Bigdiff_list[0:i])/(timeframe)
                Minor_Average = sum(Lildiff_list[0:i])/(timeframe)
            else:
                Major_Average = sum(Bigdiff_list[(i-timeframe_int):i])/(timeframe)
                Minor_Average = sum(Lildiff_list[(i-timeframe_int):i])/(timeframe)
                
            if (Minor_Average == 0 and Major_Average > 0):
                RSI = 100
                RSI_list.append(RSI)
            elif (Minor_Average == 0 and Major_Average == 0):
                pass
            else:
                RS = Major_Average/Minor_Average
                RSI = 100 - (100/(1+RS))
                RSI_list.append(RSI)
                
    RSI_df=pd.DataFrame(RSI_list)
    RSI_df.rename(columns={0:'RSI'}, inplace= True)
    
    return RSI_df
  

def RSI_Signal(closing_price):
    Signal_List = []
    RSI_df = RSI(closing_price,flag=True)
    RSI_value = RSI_df['RSI']
    for i in range(0,len(RSI_value)):
        if((RSI_value[i] > 50) and (RSI_value[i] <= 100)):
            Final_Signal = 'SELL'
        elif(RSI_value[i] == 50):
            Final_Signal = 'NO SIGNAL'
        elif((RSI_value[i] < 50) and (RSI_value[i] >= 0)):
            Final_Signal = 'BUY'
        Signal_List.append(Final_Signal)
    
    return Signal_List 
  
 
def RSI_Bar_plot():
    RSI_df = RSI(closing_price)
    
    layout = go.Layout(title='RSI and Stock price',
                   yaxis=dict(title='Stock Price'),
                   yaxis2=dict(title='RSI',
                               overlaying='y',
                               side='right'))
    
    trace1 = go.Scatter(x=Date, y=closing_price, name="Stock Price", yaxis='y1')
    trace2 = go.Bar(x=Date, y=RSI_df["RSI"], name="RSI", marker_color='red', yaxis='y2')
    
    data = [trace1, trace2]
    
    return go.Figure(data= data, layout=layout)
 

def RSI_Line_plot():
    RSI_df = RSI(closing_price)
    
    layout = go.Layout(title='RSI and Stock price',
                       yaxis=dict(title='Stock Price'),
                       yaxis2=dict(title='RSI',
                                   overlaying='y',
                                   side='right'))
    
    trace1 = go.Scatter(x=Date, y=closing_price, name="Stock Price", yaxis='y1')
    trace2 = go.Scatter(x=Date, y=RSI_df["RSI"], name="RSI", yaxis='y2')
    
    data= [trace1, trace2]
    
    return go.Figure(data=data, layout=layout)
  
 
def CMO(closing_price):                                                  #una semplice differenza del prezzo con il prezzo[i] 
    time_frame= input("Insert the time period: ")               #con il prezzo[i-periodo di tempo fisso scelto]
    time_frame = int(time_frame)                                #esempio: prezzo[giorno 30] - prezzo[giorno 10] = CMO[30]
    M_list = []
    
    for i in range(0, len(closing_price)):
        if(i-time_frame<0):
            M = closing_price[i] - closing_price[0]
            M_list.append(M)
        elif(i-time_frame>=0):
            M = closing_price[i] - closing_price[i-time_frame]
            M_list.append(M)
    
    M_df=pd.DataFrame(M_list)
    M_df.rename(columns={0:'CMO'}, inplace= True)
    
    return M_df
  
 
def CMO_Signal(closing_price):
    time_frame= 20
    M_list = []
    
    for i in range(0, len(closing_price)):
        if(i-time_frame<0):
            M = closing_price[i] - closing_price[0]
            M_list.append(M)
        elif(i-time_frame>=0):
            M = closing_price[i] - closing_price[i-time_frame]
            M_list.append(M)
    
    M_df=pd.DataFrame(M_list)
    M_df.rename(columns={0:'CMO'}, inplace= True)
    
    CMO_value = M_df['CMO']
    Signal_List = []
    
    for i in range(0,len(closing_price)):
        if(CMO_value[i] > 0):
            Final_Signal = 'SELL'
        elif(CMO_value[i] == 0):
            Final_Signal = 'NO SIGNAL'
        elif(CMO_value[i] < 0):
            Final_Signal = 'BUY'
        Signal_List.append(Final_Signal)
    
    return Signal_List
  
  
def CMO_plot():
    M_df=CMO(closing_price)
    
    layout = go.Layout(title='CMO and Stock price',
                       yaxis=dict(title='Stock Price'),
                       yaxis2=dict(title='CMO',
                                   overlaying='y',
                                   side='right'))
    
    trace1= go.Scatter(name="Stock Price", x=Date, y=closing_price, yaxis='y1')
    trace2= go.Scatter(name="Change Momentum Oscillator", x=Date, y=M_df['CMO'], yaxis='y2')
    
    data= [trace1, trace2]
    
    return go.Figure(data=data, layout=layout)
  
  
  
 
  
  
  



   
  
  
