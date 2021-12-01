CREATE DATABASE USER_DB


CREATE TABLE Registry ( 
   id INTEGER(11) PRIMARY KEY NOT NULL,
   name VARCHAR(100) NOT NULL,
   surname VARCHAR(100) NOT NULL,
   email VARCHAR(300) NOT NULL UNIQUE,
   password_hash VARCHAR(64) NOT NULL
                        );
                        

CREATE TABLE Wallet (
   id INTEGER(11) FOREIGN KEY NOT NULL REFERENCES Registry(id),
   wallet_basket VARCHAR(1000) NOT NULL      -- da capire come creare la lista di ticker code degli asset da inserire nella voce "wallet_basket"
                        );                   -- dovrebbe essere qualcosa del tipo aapl,tsla,pypl,btc,...
                        
                 
CREATE TABLE Balance (
   id INTEGER(11) FOREIGN KEY NOT NULL REFERENCES Registry(id),
   total INTEGER(12) NOT NULL,
   invested INTEGER(12) NOT NULL,
   available INTEGER(12) NOT NULL
                     );
                     
                    
CREATE TABLE Stats (
   id INTEGER(11) FOREIGN KEY NOT NULL REFERENCES Registry(id),
   porl_cumulative INTEGER(10) NOT NULL,
   porl_jan INTEGER(10) NOT NULL,
   porl_feb INTEGER(10) NOT NULL,
   porl_mar INTEGER(10) NOT NULL,
   porl_apr INTEGER(10) NOT NULL,
   porl_may INTEGER(10) NOT NULL,
   porl_jun INTEGER(10) NOT NULL,
   porl_jul INTEGER(10) NOT NULL,
   porl_Aug INTEGER(10) NOT NULL,
   porl_Sep INTEGER(10) NOT NULL,
   porl_Ott INTEGER(10) NOT NULL,
   porl_Nov INTEGER(10) NOT NULL,
   porl_Dec INTEGER(10) NOT NULL,
   stocks INTEGER(3) NOT NULL,   --porzione del portafogli in azioni 
   forex INTEGER(3) NOT NULL,    -- in forex 
   crypto INTEGER(3) NOT NULL,   -- in crypto
   futures INTEGER(3) NOT NULL,  -- futures
   trades_per_week INTEGER(12) NOT NULL,
   avg_holding_time INTEGER(10) NOT NULL, -- The time is expressed in seconds, so, if we want to express it in minutes or hours we can just divide for 60, 3600, 3600*24,3600*24*7 and so on (for minutes, hours, days, weeks...)
   trading_since DATE NOT NULL,
   profitable_weeks INTEGER(4)
   );
