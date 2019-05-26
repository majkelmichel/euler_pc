import math
lb_pierwsze=[]

def main():
    count = 3

    while True:
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            lb_pierwsze.append(count)
            print(count)
        if lb_pierwsze[len(lb_pierwsze)-1] > 2000000:
            break
        count += 1

main()
wynik = 0
lb_pierwsze = lb_pierwsze.remove(len(lb_pierwsze)-2)
print(lb_pierwsze)
for i in lb_pierwsze:
    wynik+=i
print(wynik)