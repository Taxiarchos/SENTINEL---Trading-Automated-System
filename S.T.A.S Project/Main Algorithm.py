
def Market_Discover_and_Trading_Signal():
    DEFINITIVE = "NO SIGNAL"
    nbuys = 0
    nsells = 0
    nosignals = 0

    ticker_list = ['MSFT', 'MC', 'FB', 'TSLA']
    historical_price_list = []

    Signal_list = []
    Signal_matrix = []
    Final_Signal = []

    for stock_name in ticker_list: 
            msft = yf.Ticker(stock_name)
            info=[["Info", msft.info],["historical market data", msft.history(period="max")],["Actions", msft.actions],["Dividends", msft.dividends],["Splits", msft.splits],["Financials", msft.financials],
                ["Quarterly financials", msft.quarterly_financials],["Major holders", msft.major_holders],["Institutional holders", msft.institutional_holders],["Balance sheet", msft.balance_sheet],
                ["Quarterly Balance sheet", msft.quarterly_balance_sheet], ["Cash Flow", msft.cashflow], ["Quarterly cash flow", msft.quarterly_cashflow], ["Earnings", msft.earnings],
                ["Quarterly earnings", msft.quarterly_earnings], ["Sustainability", msft.sustainability],  ["Recommendations", msft.recommendations], ["Calendar of next events", msft.calendar],
                ["Options expirations", msft.options]]
            
            stock_price=pd.DataFrame(info[1][1])
            stock_price.reset_index(inplace=True)

            stock_price_array = stock_price["Close"]
            Date = stock_price["Date"]

            historical_price_list.append(stock_price_array)

    for i in range(0,len(ticker_list)):
        closing_price = historical_price_list[i]

        indicator0 = MA_signal_Fermat(closing_price)
        indicator1 = Bollinger_Signal(closing_price)
        indicator2 = RSI_Signal(closing_price)
        indicator3 = CMO_Signal(closing_price)
        
        Signal_list = [indicator0,indicator1,indicator2,indicator3]
        Signal_matrix.append(Signal_list)

    for i in range(0,len(ticker_list)):
        for k in range(0,len(indicator0)):
            for n in range(0,4):
                if(Signal_matrix[i][n][k] == 'BUY'):
                    ++nbuys
                elif(Signal_matrix[i][n][k] == 'SELL'):
                    ++nsells
                elif(Signal_matrix[i][n][k] == 'NO SIGNAL'):
                    ++nosignals
            if(nbuys == 3):
                DEFINITIVE = 'BUY'
            elif(nsells == 3):
                DEFINITIVE = 'SELL'
            elif(nbuys == 4):
                DEFINITIVE = 'LEVERAGE-BUY'
            elif(nsells == 4):
                DEFINITIVE = 'LEVERAGE-SELL'
            elif(nbuys == 2):
                DEFINITIVE = 'NO SIGNAL'
            Final_Signal.append([ticker_list[i], historical_price_list[i][k], DEFINITIVE])

    return Final_Signal
