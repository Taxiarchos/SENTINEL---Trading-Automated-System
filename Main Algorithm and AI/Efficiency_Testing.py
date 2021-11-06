from Main_Algorithm import SENTINEL
from Main_Algorithm import SENTINEL_and_Indicators_output


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
    
    
    
    
    #This is the output of the function Test_Efficiency_simple()
    #This is what you have at the end (with simple interest):  1029009.8317198614 , This is the simple yield (not compound):  102900.98317198672
    
    
    
    
    
def Test_Efficiency_compound():
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

    PL = 0.000000001
    Starting = PL
    PL_total_list = []
    Profit_sum = 0

    for R in range(0,len(PorL)):
        new_start = PL
        PL = PL + (PL*PorL[R])
        FINAL_PL = PL - new_start 
        PL_total_list.append(FINAL_PL)
    
    Profit_sum = sum(PL_total_list)

    Real_compound_yield = (Profit_sum/Starting)*100

    print("This is what you have at the end: ", Profit_sum, ", This is the compound yield: ", Real_compound_yield)
    
    
    
    #This is the output of the function Test_Efficiency_compound()
    
    #This is what you have at the end:  nan , This is the compound yield:  nan
    #C:\Users\Notebook\AppData\Local\Temp/ipykernel_2728/1244704258.py:35: RuntimeWarning:

    #overflow encountered in double_scalars

    #C:\Users\Notebook\AppData\Local\Temp/ipykernel_2728/1244704258.py:35: RuntimeWarning:

    #invalid value encountered in double_scalars
    
    
    
def Test_Efficiency_for_Machine_Learning():
    OUTPUT = SENTINEL(ticker_list)
    OUTPUT2 = SENTINEL_and_Indicators_output(ticker_list)
    Result = 0
    Result_short = 0
    PorL = []
    buy_price=""
    short_sell_price=""
    sell_price=""
    buy_after_short_price=""
    IMPROVAL_MATRIX = []

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
                Result = (((sell_price - buy_price)/buy_price)*100)
                PorL.append(Result)
                if(Result>0):
                    Result=0
                elif(Result<=0):
                    Result=1
                #Quello in basso è il valore degli indicatori quando si acquista, il valore degli indicatori quando si vende, prezzo di acquisto, prezzo di vendita, segnale di 
                #acquisto, segnale di vendita e infine il "Result" che sarà 1 se si perdono soldi o 0 se si è in profitto
                IMPROVAL_MATRIX.append([OUTPUT2[i][1],OUTPUT2[i][2],OUTPUT2[i][3],OUTPUT2[i][4], OUTPUT2[K][1], OUTPUT2[K][2] ,OUTPUT2[K][3], OUTPUT2[K][4], buy_price, sell_price, OUTPUT[i][1], OUTPUT[k][1], Result])
                break
            elif(OUTPUT[k][1] == 'BUY' and tag==1):
                buy_after_short_price = OUTPUT[k][2]
                Result_short = (((short_sell_price - buy_after_short_price)/buy_after_short_price)*100)
                PorL.append(Result_short)
                if(Result>0):
                    Result=0
                elif(Result<=0):
                    Result=1
                IMPROVAL_MATRIX.append([OUTPUT2[i][1],OUTPUT2[i][2],OUTPUT2[i][3],OUTPUT2[i][4], OUTPUT2[K][1], OUTPUT2[K][2] ,OUTPUT2[K][3], OUTPUT2[K][4], buy_after_short_price, short_sell_price, OUTPUT[i][1], OUTPUT[k][1], Result])
                break
            else:
                pass
            
    return(IMPROVAL_MATRIX)


    
    
