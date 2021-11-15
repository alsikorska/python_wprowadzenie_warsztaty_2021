# Zadanie 1
A = 5
B = 10
C = A
A = B
B = C

# Zadanie 2
lbs_w_kg = 0.453
ft_w_m = 0.3048
imie = str(input("Proszę wpisać swoje imię: "))
lbs = float(input("Proszę podać swoją wagę w funtach (lbs): "))
ft = float(input("Proszę podać swój wzrost w stopach (ft): "))
kg = lbs_w_kg * lbs
m = ft_w_m * ft
bmi = kg / (m**2)
komunikat = f"Witaj {imie}! \nTwój wzrost w metrach wynosi {m}. \nTwoja waga w kilogramach to {kg}. \nTwoje BMI wynosi {bmi}."
print(komunikat)
lista = [{imie}, {m}, {kg}, {bmi}]

# Zadanie 3
print("Proszę o podanie następujących danych:")
imie = str(input("Imię: "))
nazwisko = str(input("Nazwisko: "))
wiek = int(input("Wiek: "))
print("Proszę wymienić po przecinku:")
jezyki_programowania = str(input("Języki programowania, z którymi miałes/miałaś styczność: "))
jezyki_obce = str(input("Języki obce, któe znasz w stopniu biegłym: "))
ile_jez_progr = jezyki_programowania.count(",")+1
ile_jez_obc = jezyki_obce.count(",")+1
informacja = f"Nazywam się {imie} {nazwisko}. Mam {wiek} lat(a). \nIlość języków programowania, z którymi miałem/miałam styczność to {ile_jez_progr}. \nIlość języków obcych, które znam w stopniu biegłym to {ile_jez_obc}."
print(informacja)
