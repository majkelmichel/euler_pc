wynik=0
list3=[]
list5=[]
def mult5(num,lst):
    if num % 5 == 0:
        lst.append(str(num))
    return lst

def mult3(num,lst):
    if num % 3 == 0:
        lst.append(str(num))
    return lst
for i in range(1000):
    mult3(i,list3)
    mult5(i,list5)

def check(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                lst1.remove(i)
    return lst1,lst2
check(list3,list5)
for i in list3:
    wynik+= int(i)
for i in list5:
    wynik+= int(i)

print(wynik)