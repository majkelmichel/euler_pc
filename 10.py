import math
lb_pierwsze=[]
wynik=0
def main(wynik):
    count = 3

    while True:
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            if count <= 2000000:
                wynik+=count
                print(wynik,count)
            else:
                return wynik

        count += 1

main(wynik)
print(wynik,"wynik")