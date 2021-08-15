
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
hesapla(1,50)