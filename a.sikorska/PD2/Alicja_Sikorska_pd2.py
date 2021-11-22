# Zadanie 1

tekst = input("Wprowadź tekst: ")
print(f"Oto twój tekst: {tekst}")
lista = list(tekst)
lista_unique=[]
for n in range(0, len(lista)) :
    if lista[n] not in lista_unique :
        lista_unique.append(lista[n])
for element in lista_unique :
    print(element)

# Zadanie 2
import random
sekretna_liczba = random.randint(1,10)
liczba_gracza = -1
proby = 0
print("Spróbuj zgadnąć sekretną liczbę od 1 do 10!")
while liczba_gracza != sekretna_liczba :
        liczba_gracza = int(input())
        proby += 1
        if liczba_gracza == sekretna_liczba :
            print("Gratulacje! Sekretna liczba to", sekretna_liczba, ". Liczba pojętych prób to:", proby)

# Zadanie 3
kontynent_ile_panstw = {
    "Europa" : 46,
    "Azja" : 50,
    "Ameryka Południowa" : 13,
    "Ameryka Północna" : 22,
    "Afryka" : 57,
    "Australia" : 14
}
kontynent = str(input("Proszę podać nazwę kontynentu: "))
print(f"Kontynent ma {kontynent_ile_panstw[kontynent]} państw.")
