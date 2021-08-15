list1 = [] 
# Kaç sayı girilecek
n = int(input("Enter number of elements in list: ")) 
# Sayı Girişi yapilmasi
for i in range(1, n + 1): 
    elements = int(input("Enter elements: ")) 
    list1.append(elements) 
list1.sort()      
print(list1)
print("En Büyük Sayı:", list1[-1]) 