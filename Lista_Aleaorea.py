#Lista_de_Numeros_Ordenados
import random
class NumeroRandom():
  def unico(x,L):
    esUnico=True
    for i in range(len(L)):
      if x==L[i]:
        esUnico=False
        break
    return esUnico
  L=[]
  j=0
  while j<100:
    x=random.randint(1,100)
    if unico(x,L):
      L.append(x)
      j+=1
  print(L)
  L.sort()
  print(L)
