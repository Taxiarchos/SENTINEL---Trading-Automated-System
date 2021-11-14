import yfinance as yf


def Futures_List_Gen(ticker_list):  #Ticker_list must be a list of futures' ticker codes ex. 'ES=F' for Bitcoin price
    historical_price_list = []
    
    for future in ticker_list:       
        #start_date=01-01-2000
        #end_date=08-01-2000
        future_data = yf.download(future, interval="1d")  #The interval can be "1m" for 1 minute, "1h" for 1 hour, "1d" for 1 day, and so on.
        future_price = future_data["Close"]                    #IF YOU DESIRE (FOR EXAMPLE "1m" AS INTERVAL, REMEMBER TO CREATE TWO VARIABLES
                                                             #start_date and end_date, the datatype is timedate (DD-MM-YYYY) and the max timeframe
        historical_price_list.append(future_price)            #for a "1m" interval df is 7 days! it's wider for "1h" interval and so on.
        
    return historical_price_list               #For example Stock_List_Gen(['ES=F']) RICORDA CHE L'ARGOMENTO ticker_list E' UNA
                                               #LISTA! QUINDI ANCHE SE C'E' UN SOLO VALORE, QUESTO VA TRA PARENTESI QUADRE.
