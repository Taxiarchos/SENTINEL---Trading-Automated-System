def Stock_List_Gen(ticker_list):
    historical_price_list = []

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
        historical_price_list.append(stock_price_array)

    return historical_price_list
