import random

compNr = random.randint(1, 100)
for i in range(10):

    while True:

        try:
            userNr = int (input('Zgadnij liczbe 1-100: '))

            if userNr < 1 or userNr > 100:
                raise ValueError

            break

        except ValueError:
            print ("BŁĄD: Podaj liczbę z zakresu 1-100\n")

        except KeyboardInterrupt:
            print ("Pa pa!")
            exit()

        except Exception:
            print ("BŁĄD: Wystąpił nieoczekiwany błąd")
            exit()

    if userNr == compNr:
        print ("Zgadłeś!\n")
        break

    elif userNr > compNr:
        print ("Szukana liczba jest mniejsza\n")

    else:
        print ("Szukana liczba jest większa\n")
