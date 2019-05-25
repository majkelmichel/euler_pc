lista =[]

for num in range(1000000000000000000):
   # prime numbers are greater than 1
    print(num)
    if num > 1:
        for i in range(2,num):
           if (num % i) == 0:
               break
        else:
           lista.append(num)
    if len(lista) == 10001:
        break
print(lista)