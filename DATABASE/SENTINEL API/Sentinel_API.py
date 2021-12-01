from dbmodule import connect  
import SENTINEL/'Main Algorithm and AI'/Main_Algorithm
import SENTINEL/'Main Algorithm and AI'/Efficiency_Testing
import hashlib
                                                          #THIS PART IS DEDICATED TO THE USER DATABASE

class User:
    def __init__(self, id, name, surname, email, password):
        self.id = id
        self.name = name 
        self.surname = surname
        self.email = email
        self.password = password
        self.password_hash = hashlib.sha512(password).hexdigest()
    
    def Add():
        connection_USER = connect('USER_DB', 'username', 'pwd') #creating connection object to USER_DB
        Cursor_USER = connection_USER.cursor() #Cursor object for USER_DB

        try:
            Cursor_USER.execute('''
            INSERT INTO TABLE Registry(id, name, surname, email, password_hash)
            VALUES({User.id}, {User.name}, {User.surname}, {User.email}, {User.password_hash});
            ''')
        except:
            print("Unexpected error in uploading data into the Database Target")
        else:
            return 0
        

                                                          #THIS PART IS DEDICATED TO THE AI DATABASE


def AI_Database_Data_Uploader():
    connection_AI = connect('AI_DB', 'username', 'pwd') #creating connection object to AI_DB
    Cursor_AI = connection_AI.cursor() #Cursor object for AI_DB


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

    try:
        for i in len(OUTPUT['Fermat Signal apertura']):
            row = OUTPUT.iloc[i,:]
            Cursor_AI.execute('''
            INSERT INTO AI_Dataset(fermat_signal_opening, bollinger_opening, rsi_opening, cmo_opening, fermat_signal_closing, bollinger_closing, rsi_closing, cmo_closing, opening_price, closing_price, final_signal_opening, final_signal_closing, result)
            VALUES({row});
            ''')
    except:
        print("Unexpected error in uploading data into the Database Target")
    else:
        return 0
    

#time to fetch data
def AI_Database_data_fetcher():
    connection_AI = connect('AI_DB', 'username', 'pwd') #creating connection object to AI_DB
    Cursor_AI = connection_AI.cursor() #Cursor object for AI_DB

    Cursor_AI.execute('SELECT * from AI_Dataset')
    Result = Cursor_AI.fetchall()

    return Result
