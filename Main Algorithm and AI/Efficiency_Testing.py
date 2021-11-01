from Main_Algorithm import SENTINEL


def Test_Efficiency():
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
          elif(OUTPUT[k][1] == 'BUY' and tag==1):
              buy_after_short_price = OUTPUT[k][2]
              PorL.append((((short_sell_price - buy_after_short_price)/buy_after_short_price)*100))
          else:
              pass

  PL_total = 10
  Starting = PL_total

  for R in range(0,len(PorL)):
      PL_total = PL_total + (PL_total*PorL[R])

  real_yield = (((PL_total - Starting)/Starting)*100)

  print("This is what you have at the end: ",PL_total, "This is the yield: ", real_yield)
