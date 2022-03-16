# classe calcolo combinatorio

from itertools import permutations, combinations, combinations_with_replacement

class calcComb():

    def __init__(self, stringa):                                                                    
        self.__N = len(stringa)
        self.__stringa = stringa                                                                                               
        self.__listStringa = list(stringa)
        self.__anagrammi = self.anagrammi() 

    def getStringa(self):                                                                           
        return self.__stringa

    def getListStringa(self):                                                                       
        return self.__listStringa
    
    def setStringa(self, stringa):                                                                  
        self.__stringa = stringa
        self.__N = len(stringa)
        self.__listStringa = list(stringa)
        self.__anagrammi = self.anagrammi()


    def charRipetuti(self):
caratteri_casa= {"c":"1","a":"2","s":"1"}
(caratteri_casa["c"])
print('il numero di volte che si ripete il carattere c è {}'.format(caratteri_casa["c"]))
(caratteri_casa["a"])
print('il numero di volte che si ripete il carattere a è {}'.format(caratteri_casa["a"]))
     
(caratteri_casa["s"])
print('il numero di volte che si ripete il carattere s è {}'.format(caratteri_casa["s"]))

        


    def cerca(str):

str= casa

f = open('words.italian.txt', 'r')
line = f.readline()


for line in f: 
    if str == line[:-1]:  
        print("vero")

    def fattoriale(n):
   n = ('inserire numero')
def fattoriale(n):
    if n==0:
        return 1
    else:
        return n*fattoriale(n-1)

print(fattoriale(n))


def fattoriale(k):
   k = ('inserire numero')
def fattoriale(k):
    if k==0:
        return 1
    else:
        return k*fattoriale(k-1)

print(fattoriale(k))



    def coeffBinom(n, k):

  if k < 0 or k > n:
    return None
  x = 1
  for i in range(min(k, n - k)):
    x = x*(n - i)//(i + 1)
  return x


    def anagrammi(self):
      lettere = list("casa")


permutazioni = list(permutations(lettere))


temp = ''
anagrammi = []

for i in permutazioni:
    for carattere in i:

        temp += carattere 

   
    anagrammi.append(temp)
    
    temp = ''

print(anagrammi)
    
    def confUtil(self):


    # PERMUTAZIONi

    def nPermutSenzaRip(self):
        nPermutSenzaRip= fattoriale(n)
        print(fattoriale(n))
    

    def nPermutConRip(self):
      

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        pass

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        pass
    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
   if n >= k and k>0
       nDispSemplSenzaRip= n*k

print(nDispSemplSenzaRip)
  
   

    def nDispSemplConRip(self):
nDispSemplConRip= (n**k)

     
    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        pass

    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
      pass

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
nCombSemplSenzaRip = nDispSemplConRip/(fattoraiale(k))

      

    def nCombSemplConRip(self):
      nCombSemplConRip

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0

    # PROBABILITA'

    def probConfUtil(self):
        pass
