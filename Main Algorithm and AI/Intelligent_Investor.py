import Main_Algorithm import SENTINEL_REDUX, SENTINEL_and_Indicators_output
from Efficiency_Testing import Test_Efficiency_for_Machine_Learning
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd


ticker_list = ['MSFT','MC','FB','TSLA','PYPL']
OUTPUT = Test_Efficiency_for_Machine_Learning(ticker_list)



for i in range(0,len(OUTPUT)):
  for j in range(0,13):
    if(OUTPUT[i][j] == 'SELL'):
      OUTPUT[i][j] == 1
    elif(OUTPUT[i][j] == 'BUY'):
        OUTPUT[i][j] == 0
    elif(OUTPUT[i][j] == 'LEVERAGE-SELL'):
        OUTPUT[i][j] == 1
    elif(OUTPUT[i][j] == 'LEVERAGE-BUY'):
        OUTPUT[i][j] == 0

OUTPUT = pd.to_dataframe(OUTPUT)
OUTPUT.rename(columns={0:'Fermat Signal apertura', 1:'Bollinger apertura', 2:'RSI apertura', 3:'CMO apertura', 4:'Fermat Signal chiusura', 5:'Bollinger chiusura', 6:'RSI chiusura', 7:'CMO chiusura', 8:'Prezzo apertura', 9:'Prezzo chiusura', 10:'Final Signal apertura', 11:'Final Signal chiusura', 12:'Esito'}, inplace = True)
OUTPUT.head()

TO_CHECK = SENTINEL_REDUX(ticker_list)

X_train, X_test, y_train, y_test = train_test_split(OUTPUT['Fermat Signal apertura':'Prezzo chiusura', 'Esito'], OUTPUT['Final Signal apertura'], test_size = 0.30)
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train,y_train)
y_pred = classifier.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

def Intelligent_Investor(OUTPUT):
  Final_confirm = classifier(TO_CHECK)
  if(Final_confirm == TO_CHECK[1]):
    #Effettua acquisto
  else:
    #NON effettuare acquisto


