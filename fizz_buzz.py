"""n = 20
#def fizz_buzz(1,n):
for i in range(1,n+1):
        if i%15 == 0:
            print("fizzbuz")
        elif i%5 == 0 :
            print("fizz")
        elif i%3 == 0 :
            print("buzz")
        else:
            print(i)
    
#fizz_buzz(1,50)"""

print((lambda x : x[::-1])("hello"))

"""


def hesapla(n, y):
    for i in range (n, y+1):
        if i % 3 == 0 and i % 5 != 0:
            print("fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        else:
            print(i)
hesapla(1,50)"""