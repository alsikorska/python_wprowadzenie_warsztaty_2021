# Zadanie 1

class Student():
    def __init__(self, imie, nazwisko, nr_albumu):
        
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_albumu = nr_albumu
        self.kierunek = None
        self.srednia = None
        self.stypendium  = None

    def wybierz_kierunek(self):

        while True:
                
            option = (input("Wybierz kierunek z podanych opcji: \n Ekonomia \n Zarządzanie \n Finanse \n")).capitalize()

            if option == "Ekonomia":
                self.kierunek = "Ekonomia"
                break
            elif option == "Zarządzanie":
                self.kierunek = "Zarządzanie"
                break
            elif option == "Finanse":
                self.kierunek = "Finanse"
                break           
            else:
                print("Nie ma takiego kierunku – proszę wybrać ponownie")
                    

    def jaka_srednia(self):

        while True:

            import random
            maximum, minimum = 5.01, 2.00
            answer = random.random() * (maximum - minimum) + minimum
            srednia_ocen = float(str(round(answer,2)))
            self.srednia = srednia_ocen
            print(f"Średnia studenta {self.imie} {self.nazwisko} o numerze indeksu {self.nr_albumu} wynosi {self.srednia}")
            break

            
    def czy_stypendium(self):
        
        while True:

            srednia_studenta = self.srednia

            if srednia_studenta <= 3.0 :
                def __del__(self):
                    print("Student został skreślony z listy studentów")
                break
            elif srednia_studenta >= 4.7 :
                print("Student otrzymuje stypendium!")
                self.stypendium = True
                break
            else :
                print("Student nie otrzymuje stypendium.")
                self.stypendium = False
                break

student1 = Student("Jan", "Nowak", 682311)
student1.wybierz_kierunek()
student1.jaka_srednia()
student1.czy_stypendium()

student2 = Student("Anna", "Kowalska", 425633)
student2.wybierz_kierunek()
student2.jaka_srednia()
student2.czy_stypendium()

student3 = Student("Piotr", "Polak", 974882)
student3.wybierz_kierunek()
student3.jaka_srednia()
student3.czy_stypendium()
