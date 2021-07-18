lis = input("sayi gir.: ")
arm = list(lis)
int(arm[0])
len(lis)
i = 0
x = 0
for i in range(0 , len(lis)) :
  int(arm[i])**len(lis)
  x += int(arm[i])**len(lis)
  
  i +=1
if x == int(lis) :
  print("{} armstrong sayidir.".format(lis))
else :
  print("{} armstrong sayi degildir.".format(lis))

