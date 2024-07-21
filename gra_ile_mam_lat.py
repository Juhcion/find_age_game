#########################################################################################
# Gra "Zgadnij ile mam lat"
#########################################################################################
# Zadanie polega na stworzeniu gry w której użytkownik zgaduję wiek fikcyjnej postaci. 
#########################################################################################
# Wytyczne: 
# 1. program po wpisaniu przez użytkowniaka dowolnej liczby z zakresu 10-100 musi w wyniku zwracać, czy użytkownika zgadł wiek który jest w słowniku.
# 2. gra losuje losową wartość z listy zawierającej 3 imiona (klucze) i 3 wartości wieku (dowolne)
# 2. program musi informować, czy użytkownik jest blisko zgadniecia wieku (zawiera się w +/- 10% podanego wieku, np. wiek to 30 lat, użytkownik podał 27 co oznacza, że 10% z 30 +/- to 27 i 33
# więc podpowiedź powinna zawierać informację, że jest +/- 10% od zgadnięcia wieku)
# użytkownik ma tylko 5 szans na zgadnięcie, po 4 nieudanej próbie powinno wyświetlić się, że przegrał grę.
# gra powinna wyświetlać komunikat powitalny, informację o tym, że liczba jest blisko (+/- 10%) o przegranej i wygranej. 
# po nieudanej próbie można ponowić grę, wpisując TAK, lub NIE (wtedy informacją o zakończeniu gry)

# Zmiany: 
# - dodane automatyczne losowanie wieku z wybranego zakresu, bez podawania wartości (aby nie widzieć, jakie to liczby)
# - automatycznie uzupełnianie printów w przywitaniu i komunikatach o podane wartości wejściowe dla gry
# - dodanie zmiennych do słównika, zamiast stałych wartości wieku
# - (do zmiany) wartość odległości np. 5 lat od wyniku a nie procentowa

import random

# budowa słownika + zmienne do szybkiej podmiany
x = random.randint(10, 100)
y = random.randint(10, 100)
z = random.randint(10, 100)

ludzie = [
    {
        "name": "Kasia",
        "age": (x),
    },
    {
        "name": "Basia",
        "age": (y),
    },
    {
        "name": "Asia",
        "age": (z),
    },
]

# losowanie ze słownika osoby
wylosowana_osoba = random.choice(ludzie)

# przypisanie zmiennych do wartości imienia i wieku wylosowanej osoby

imie_wylosowanej_osoby = wylosowana_osoba["name"]
wiek_wylosowanej_osoby = wylosowana_osoba["age"]

# sekcja na dane do wprowadzenia:
proby = 11 # ustawienie liczby prób
min_wiek = 10 # minimalny wiek
max_wiek = 100 # maksymalny wiek
czy_blisko = 0.3 #procent przy którym będzie podpowiedź (0.1 to 10%)

# weryfikacja działania - ok
# print(f"Wylosowane imię: {imie_wylosowanej_osoby}, wiek: {wiek_wylosowanej_osoby}")

# budowa przywitania

print("----- Witaj w grze - Zgadnij ile mam lat -----", "\n",
    "Zasady:", "\n", 
    "1. Masz", proby, "prób", "\n",
    "2. Podaj wiek z przedziału od:", min_wiek, "do", max_wiek,".","\n",
    "3. Jeżeli podany wiek będzie +/-:", czy_blisko*10, "% od szukanej liczby, otrzymasz podpowiedź.", "\n",
    "Powodzenia! " )

# logika gry

print ("Wylosowna osoba to:", imie_wylosowanej_osoby)

while proby > 0:
    
    podany_wiek = input("Podaj wiek: ")

    try:
        podany_wiek = int(podany_wiek)
        if podany_wiek < min_wiek or podany_wiek > max_wiek:
            print("Nieprawidłowy zakres, podaj liczbę z przedziału od:", min_wiek, "do", max_wiek,".","\n")
        else:
            if podany_wiek == wiek_wylosowanej_osoby:
                print("Gratulacje wygrana!!! Prawidłowy wiek to:", wiek_wylosowanej_osoby)
                break
            else:
                proby -= 1
                if proby > 0:
                    if abs(podany_wiek - wiek_wylosowanej_osoby) <= wiek_wylosowanej_osoby * czy_blisko: # przykład 20-30 <= 30* 0,3 sprawdzić czy to aby na pewno najlepszy sposób
                        print("Podpowiedź: Jesteś blisko!")
                    print(f"Zła odpowiedź. Pozostało prób: {proby}")
                else:
                    print("Koniec gry. Wyczerpałeś wszystkie próby.")
                    print(f"Prawidłowy wiek to: {wiek_wylosowanej_osoby}")
    except ValueError:
        print("Wprowadzona wartość inną niż liczbowa")