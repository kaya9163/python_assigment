liste=[]
def fib(n):
  a,b = 0,1
  while a<=n :
    liste.append(a)
    
    a,b=b, a+b
    if liste[-1]==55 :
      break
  print(liste)
fib(55)
