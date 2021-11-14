import yfinance as yf


def Stock_List_Gen(ticker_list):
    historical_price_list = []
    
    for stock_name in ticker_list:
        stock_data = yf.download(stock_name)
        stock_price = stock_data["Close"]
        
        historical_price_list.append(stock_price)
        
    return historical_price_list               #For example Stock_List_Gen(['TSLA']) RICORDA CHE L'ARGOMENTO ticker_list E' UNA
                                               #LISTA! QUINDI ANCHE SE C'E' UN SOLO VALORE, QUESTO VA TRA PARENTESI QUADRE.
