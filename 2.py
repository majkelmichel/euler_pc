liczby_fib = []
def fibonacci(zakres,lista):
    num1=0
    num2=1
    while num1<zakres:
        num1+=num2
        num2+=num1
        lista.append(num1)
        lista.append(num2)
    return lista

fibonacci(4000000,liczby_fib)
wynik = 0
for i in liczby_fib:
    if i % 2 == 0:
        wynik+=i
print(wynik)