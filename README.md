# PISANIELLO-SACCARDO-D'ORAZI

## Ruzzle

### Abstract
Ruzzle è un gioco che si basa sull’ottenere quanti più punti possibili formando parole.Per formare queste parole il giocatore avrà a disposizione una tabella con delle lettere. *N.B.* Il giocatore dovrà compiere la sfida in un tempo limite della durata di cinque minuti.

### Funzionalità
Lo scopo del gioco è ottenere più punti possibili in un determinato tempo.Per ottenere dei punti bisogna trovare nelle parole sensate nella tabella contenente lettere. L’assegnazione dei punti dipende dalla lunghezza delle parole trovate. Inoltre sono presenti dei bonus per ottenere più punti.
Punteggio parole:
- 1 parola da 2 o 3 lettere = 20 punti 
- 1 parola da 4 o 5 lettere = 30 punti   
- 1 parole da 6 o 7 lettere = 40 punti 
- 1 parola da 8 o più lettere = 50 punti 
- 1 parola sbagliata = -15 punti  
##### Bonus 
- parola contenente le lettere j,k,y,x,w = + 30 punti  
- parola che contiene 1 doppia = + 20 punti 

### CONTESTO
Questo gioco è stato ideato durante l'ora di compresenza di matematica coding. Per realizzarlo abbiamo utilizzato alcune regole matematiche riguardanti il calcolo combinatorio
che avevamo precedentemente affrontato con la docente di matematica.
### CALCOLO COMBINATORIO 

  Il **calcolo combinatorio** è, in matematica, ciò che ci consente di determinare in quanti e in quali modi è possibile ordinare o raggruppare un determinato numero di elementi su un determinato numero di posti.
  
  Il calcolo combinatorio è un tipo di calcolo che comprende vari metodi tra i quali:
  
 #### PERMUTAZIONI SEMPLICI E PERMUTAZIONI CON RIPETIZIONE
  - Le permutazioni semplici di "n" elementi distinti, sono tutti i gruppi formati dagli "n" elementi, che differiscono per il loro ordine.
  - Le permutazioni con ripetizione di "n" elementi distinti, sono tutti i gruppi formati dagli "n" elementi, alcuni ripetuti, che differiscono per il loro ordine.
    
 #### DISPOSIZIONI SEMPLICI e DISPOSIZIONI CON RIPETIZIONE
- Le disposizioni semplici di "n" elementi su "k" posti, sono  tutti i gruppi di "k" elementi scelti tra gli "n" che si differenziano per almeno un elemento o per l'ordine con cui gli elementi sono disposti.
- Le disposizioni con ripetizione di "n" elementi su "k" posti, sono tutti i gruppi di "k" elementi, alcuni ripetuti, scelti fra gli "n" che si differenziano per almeno un elemento o per l'ordine con cui gli elementi sono disposti.
     
#### COMBINAZIONI SEMPLICI E COMBINAZIONI CON RIPETIZIONE
- Le combinazioni semplici di "n" elementi su "k" posti, sono tutti i gruppi di "k" elementi scelti tra gli "n" che differiscono per almeno un elemento e non per l'ordine.
- Le combinazioni con ripetizione di "n" elementi su "k" posti, sono tutti i gruppi di "k" elementi scelti tra gli "n", alcuni ripetuti, che differiscono per almeno un elemento e non per l'ordine. 

#### DESCRIZIONE BLOCCHI
Descrizione dei blocchi utilizzati nel diagramma di flusso
- Inizializzazione: Il blocco inizializzazione permette al giocatore di scegliere il nome utente e il livello di difficoltà di gioco;
- Aggiorna punteggio: il blocco aggiunge il punteggio in base ai risultati del giocatore;
- Schermata fine partita: il blocco mostra il punteggio realizzato durante la partita dal giocatore;
- Azzera punteggio: il blocco azzera il punteggio realizzato nella partita precedentemente iniziata dal giocatore,se quest'ultimo,decide di iniziare una nuova partita
