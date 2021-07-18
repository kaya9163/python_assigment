# Python password reminder assigment
enter_name = input("What is your name? ")
my_name, password = "Kaya","123"
if enter_name.capitalize() == my_name:
  print("Hello, {}! The password is {},".format(my_name,password))
else:
  print("Hello, {}! See you later.".format(enter_name.capitalize()))
