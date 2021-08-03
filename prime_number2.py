number = int(input("Please Enter A Number: "))
if number > 1:
    for i in range (2, number):
        if num%i == 0:
            print(number, "is not a prime number")
        else:
            print(number, "is a prime number")
        break
else:
    print(number, "is not a prime number")
