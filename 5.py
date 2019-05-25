lst = [10,9,8,7,6,5,4,3,2,1]
lst2 = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

def znajdz_liczbe(lista):
    for i in range(20,1000000000,20):
        print(i)
        for j in lista:
            if i % j != 0:
                break
            if j == 1:
                return i
        i+=1

znajdz_liczbe(lst2)

