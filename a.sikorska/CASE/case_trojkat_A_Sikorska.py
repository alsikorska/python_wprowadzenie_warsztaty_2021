class TriangleChecker():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print("Sprawdźmy czy można utworzyć trójkąt!")

        
    def is_triangle(self):
        if self.check_is_triangle() :
            print("Hurra, możesz zbudować trójkąt!")
    
        elif self.a<0 or self.b<0 or self.c<0 :
            print("Przy liczbach ujemnych nic z tego nie wyjdzie!")
  
        else: 
            print("Szkoda, ale nie da się z tego zrobić trójkąta.")
            

    def check_is_triangle(self):
        return self.a+self.b>self.c and self.a+self.c>self.b and self.b+self.c>self.a          
        
    def calculateArea(self):
        if self.check_is_triangle():
            import math
            p = (self.a+self.b+self.c)/2
            S2 = p*(p-self.a)*(p-self.b)*(p-self.c)
            pole = pow(S2, 1/2)
            print(f"Pole tego trójkąta wynosi {pole}")
                  
    def calculatePerimeter(self):
        if self.check_is_triangle():
            obwod = self.a+self.b+self.c
            print(f"Obwód trójkąta wynosi {obwod}")
        
    def calculateCosinuses(self):
        if self.check_is_triangle():
            cos_a = (self.a**2 + self.c**2 - self.b**2) / (2*self.a*self.c)
            cos_b = (self.a**2 + self.b**2 - self.c**2) / (2*self.a*self.b)
            cos_y = (self.b**2 + self.c**2 - self.a**2) / (2*self.c*self.b)
            print(f"Cos(a) wynosi {cos_a}, \nCos(b) wynosi {cos_b}, \ncos(y) wynosi {cos_y}.")

def start():
    

    try:
        a = float(input("Wprowadź długość pierwszego odcinka :"))
        b = float(input("Wprowadź długość drugiego odcinka :"))
        c = float(input("Wprowadź długość trzeciego odcinka :"))
        
    except ValueError:
        print("Wystarczy wpisać cyfry!")
        start()


            
    trojkat1 = TriangleChecker(a, b, c)
    trojkat1.is_triangle()
    trojkat1.calculateArea()
    trojkat1.calculatePerimeter()
    trojkat1.calculateCosinuses()

start()
