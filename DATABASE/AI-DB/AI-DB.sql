CREATE DATABASE AI_DB


CREATE TABLE AI_Dataset (                      -- 0 is buy, 1 is sell
   fermat_signal_opening INTEGER(1) NOT NULL,
   bollinger_opening INTEGER(1) NOT NULL,  
   rsi_opening INTEGER(1) NOT NULL,
   cmo_opening INTEGER(1) NOT NULL,
   fermat_signal_closing INTEGER(1) NOT NULL,
   bollinger_closing INTEGER(1) NOT NULL,
   rsi_closing INTEGER(1) NOT NULL,
   cmo_closing INTEGER(1) NOT NULL,
   opening_price INTEGER(1) NOT NULL,
   closing_price INTEGER(1) NOT NULL,
   final_signal_opening INTEGER(1) NOT NULL,
   final_signal_closing INTEGER(1) NOT NULL,
   result INTEGER(1) PRIMARY KEY NOT NULL                   -- 0 is positive result, 1 is neutral or negative
   );
