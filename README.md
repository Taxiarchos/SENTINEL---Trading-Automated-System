# Automated-Trading-Algorithms

DA FINIRE: ALGORITMO DI BUY/SELL, ALGORITMO DI RICERCA NEL MERCATO AZIONARIO, INDICATORI DI BORSA

DA INIZIARE: GUI, WEB SCRAPING E/O PUBLIC API, PROGRAMMA DI CREAZIONE/GESTIONE PORTAFOGLIO (CON FUNZ. DI DIVERSIFICAZIONE E CALCOLO DI RISCHIO/VOLATILITA')

## GUI

### --- DA DECIDERE IL LINGUAGGIO, LA PRIORITA' E' LA PORTABILITA' IN OGNI OS E DISPOSITIVO. LA GUI DEVE ESSERE VELOCE, SEMPLICE ED INTUITIVA. LA SCELTA DEL LINGUAGGIO DEVE ESSERE
### --- FATTA IN MODO TALE CHE LA CREAZIONE DELLA GUI SIA RELATIVAMENTE VELOCE E COMODA DA FARE, MA QUESTO PUNTO E' SECONDARIO AL PRIMO, CHE INVECE HA LA PRIORITA'!

per la GUI, penso sia giusto ispirarsi a quella di FINECO BANK, quella dell'app, la stessa di quella del sito, con il balance messo dento un 
cerchio blu. se si va sul cerchio con il mouse, la parte AVAILABLE si colora di ARANCIONE, se si va sulla parte INVESTED, si colora di CELESTE. 
Cliccando sul cerchio nella zona INVESTED, si apre la voce del menù: Portafoglio.
Sempre nella pagina iniziale, in basso ci saranno 3 riquadri, uno accanto all'altro, in cui ci sarà scritto, AVAILABLE, INVESTED ed infine, TOTAL.
In alto 3 linee orizzontali denotano il menù, cliccando sulle 3 linee, si apre una tendina da sinistra. Le voci del menù sono:

. Balance

. Portfolio

. Cronologia Investimenti

. Performance

. IMPOSTAZIONI

. Contattaci

Nella sezione cronologia Investimenti, sarà possibile effettuare segnalazioni di investimenti andati in negativo, cioè in cui l'algoritmo non ha funzionato bene.
Queste segnalazioni serviranno a migliorare il servizio. 
P.S. nella page principale, in alto ci deve essere scritto SENTINEL (titolo), Automated Trading System (Sottotitolo). I colori dell'app sono: Bianco(sfondo), Blu(scritte),
tranne gli elementi che cambiano colore quando si effettua l'hover con il mouse o che si cliccano, i quali cambiano colore temporaneamente. Il balance deve essere al centro del
cerchio blu e scritto bello grande.

## PROGRAMMA DI CREAZIONE/GESTIONE PORTAFOGLIO

### --- USERA' UN ALGORITMO DI INTELLIGENZA ARTIFICIALE E SARA' SCRITTO INTERAMENTE IN PYTHON

da scrivere in Java o C++, da decidere ancora, aspetto il tuo consiglio roberto.
Il programma crea la classe del conto, crea una parte investita ed una disponibile, investe i soldi in base al tipo di asset, per esempio:
--5% in asset rischiosi (Forex, futures su commodities, crypto), 60% indici ed etf, 35% azioni (RISCHIO LOW)
--10% in asset rischiosi (Forex, futures su commodities, crypto), 40% indici ed etf, 50% azioni (RISCHIO MEDIO)
--25% in asset rischiosi (Forex, futures su commodities, crypto), 5% indici ed etf, 70% azioni (RISCHIO ALTO)
--40% in asset rischiosi (Forex, futures su commodities, crypto), 0% indici ed etf, 60% azioni (RISCHIO MASSIMO)
Calcola la correlazione di pearson tra i vari titoli e strumenti posseduti in portafoglio, e la porzione di portafoglio costituita da un singolo tipo di asset.
Appena i soldi sono investiti, o se ci sono soldi disponibili, l'algoritmo viene avviato ed investe i soldi, i profitti vengono reinvestiti. Se trova una opportunità migliore di
un altra, chiude quella già aperta ed apre una posizione per il titolo che conviene di più ( questa funzione non è così importante). Se l'utente vuole prelevare dei soldi, se vi
è disponibilità, si preleva e basta, se non v'è disponibilità, si avverte che bisogna chiudere delle posizioni, e si chiudono le posizioni a più bassa priorità (da capire come
calcolare la priorità). Si accettano bonifici istantanei in vari modi e si preleva con un bonifico normale o istantaneo in base alla scelta dell'utente di pagare o meno 1€ di
commissioni. Creare funzione che calcola la volatilità del portafogli. Tutte le statistiche saranno inserite nella sezione Performance, per dare all'utente un resoconto molto
dettagliato. Se il segnale è BUY, si compra con una leva (1,5<=leva<3), se quando arriva il segnale BUY, vi sono posizioni di vendita aperte, si liquidano immediatamente prima
di acquistare. Se il segnale è SELL, si vende con leva (3<=leva<=4,5) con margine di protezione!, se quando arriva il segnale ci sono posizioni di BUY aperte, si liquidano
immediatamente le posizioni di acquisto e si vende allo scoperto (Ovvero SELL. Ricorda roberto, SELL vuol dire vendere allo scoperto).

## INDICATORI DI BORSA

### --- SCRITTI IN PYTHON

Finire di creare l'indice RSI (che è fatto male)

## ALGORITMO DI BUY/SELL

### --- USERA' UN ALGORITMO DI INTELLIGENZA ARTIFICIALE E SARA' SCRITTO INTERAMENTE IN PYTHON

Una volta sistemato l'RSI, sistemare l'algoritmo e testare i segnali e vedere la frequenza di quelli esatti.
