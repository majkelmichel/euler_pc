def kwadrat_2(potega):
    potega = int(potega)
    wynik = 2 ** potega
    wynik = str(wynik)
    return wynik

def suma_liczb(liczba):
    suma = 0
    liczba = str(liczba)
    for i in liczba:
        suma += int(i)
    return suma

def potega_pytaj():
    potega = input("Podaj potęgę: ")
    wyn = kwadrat_2(potega)
    wyn = int(wyn)
    print(suma_liczb(wyn))

potega_pytaj()