from Main_Algorithm import SENTINEL


def Test_Efficiency_simple():
    OUTPUT = SENTINEL(ticker_list)
    PorL = []
    buy_price=""
    short_sell_price=""
    sell_price=""
    buy_after_short_price=""

    for i in range(0,len(OUTPUT)):
        if(OUTPUT[i][1] == 'BUY'):
            buy_price=OUTPUT[i][2]
            tag=0
        elif(OUTPUT[i][1] == 'SELL'):
            short_sell_price=OUTPUT[i][2]
            tag=1
        for k in range(i,len(OUTPUT)):
            if(OUTPUT[k][1] == 'SELL' and tag==0):
                sell_price=OUTPUT[k][2]
                PorL.append((((sell_price - buy_price)/buy_price)*100))
                break
            elif(OUTPUT[k][1] == 'BUY' and tag==1):
                buy_after_short_price = OUTPUT[k][2]
                PorL.append((((short_sell_price - buy_after_short_price)/buy_after_short_price)*100))
                break
            else:
                pass

    Starting = 10
    PL_total_list = []
    real_simple_yield = 0
    Profit_sum = 0

    for R in range(0,len(PorL)):
        PL = Starting*PorL[R]
        PL_total_list.append(PL)
    
    Profit_sum = sum(PL_total_list)
    
    for Z in range(0,len(PorL)):
        real_simple_yield = real_simple_yield + PorL[Z]

    print("This is what you have at the end (with simple interest): ", Profit_sum, ", This is the simple yield (not compound): ", real_simple_yield)
