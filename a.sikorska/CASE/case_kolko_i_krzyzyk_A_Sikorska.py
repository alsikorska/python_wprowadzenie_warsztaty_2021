
class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0

    def win(self):
        self.score += 1

    def getScore(self):
        return self.score

    def printScore(self):
        print("Gracz ", self.name, " zdobył ", self.score, " punktów")
        
name_1 = input("Proszę gracza nr 1 o podanie nazwy: ")
name_2 = input("Proszę gracza nr 2 o podanie nazwy: ")
p1 = Player(name_1)
p2 = Player(name_2)

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.state = Game_state()

    def nextMove(self):
        target_point = int(input("Gdzie chcesz postawić znak " + self.getCurrentPlayer().name + "? Podaj pozycje: "))
        self.state.setPoint(target_point)

        self.state.printBoard()

    def printInstructions(self):
        print('''
Zapraszam do gry w "kółko i krzyżyk"!
Gre zawsze zaczyna 'O' - kółko.
Gracz wybiera gdzie na planszy chce postawić swój znak – kółka lub krzyżyka,
poprzez wybranie jednej z cyfr od 0 do 8 zapisanych w ułożeniu odpowiadającym polom jak na poniższej planszy:

0|1|2|

3|4|5|

6|7|8|

Trzy jednakowe znaki ułożone w jednej linii - w poziomie, w pionie lub w poprzek oznaczają zwycięstwo jednego z graczy.
Dobrej zabawy!



        ''')
        

    def start(self):
        self.state.printBoard()
        while True:
            self.nextMove()
            if self.state.checkIfWin() == True:
                print("Wygrana!")
                self.getCurrentPlayer().win()
                break
                
            if self.state.checkIfDraw() == True:
                print("Remis!")
                break
            
            self.state.nextPlayer()
            
        print("Koniec gry")
        self.printScore()
        want_to_continue = input("Czy chcesz kontunuowac gre? Wpisz 'tak' lub 'nie': ")
        if want_to_continue == "tak":
            newGame = Game_creator(self.player1, self.player2).createGame()
            newGame.start()
        else:
            self.printScore()
            


    def printScore(self):
        self.player1.printScore()
        self.player2.printScore()
        
    def getCurrentPlayer(self):
        if self.state.who_now == 1:
            return self.player1;
        else:
            return self.player2
            

class Game_state():

    def __init__(self):
        self.point_on_board =[0,0,0,0,0,0,0,0,0]
        self.who_now = 1

    def printBoard(self):
        import sys
        i= 0
        while i<9:
            match self.point_on_board[i]:
                case 0:
                    sys.stdout.write(str(i))
                case 1:
                    sys.stdout.write("O")
                case 2:
                    sys.stdout.write("X")
            sys.stdout.write("|")
                
            if i%3==2:
                print("\n")
    
            i+=1

    def setPoint(self, position):
        value = self.who_now
        self.point_on_board[position] = value

    def nextPlayer(self):
        if self.who_now == 1 :
            self.who_now = 2
        else :
            self.who_now = 1

    def checkIfWin(self):
        if self.point_on_board[0] != 0 and self.point_on_board[0] == self.point_on_board[1] == self.point_on_board[2]:
            return True
        elif self.point_on_board[3] != 0 and self.point_on_board[3] == self.point_on_board[4] == self.point_on_board[5]:
            return True
        elif self.point_on_board[6] != 0 and self.point_on_board[6] == self.point_on_board[7] == self.point_on_board[8]:
            return True
        elif self.point_on_board[0] != 0 and self.point_on_board[0] == self.point_on_board[3] == self.point_on_board[6]:
            return True       
        elif self.point_on_board[1] != 0 and self.point_on_board[1] == self.point_on_board[4] == self.point_on_board[7]:
            return True       
        elif self.point_on_board[2] != 0 and self.point_on_board[2] == self.point_on_board[5] == self.point_on_board[8]:
            return True
        elif self.point_on_board[0] != 0 and self.point_on_board[0] == self.point_on_board[4] == self.point_on_board[8]:
            return True
        elif self.point_on_board[2] != 0 and self.point_on_board[2] == self.point_on_board[4] == self.point_on_board[6]:
            return True  
        else:
            return False

    def checkIfDraw(self):
        for i in range(9):
            if self.point_on_board[i] == 0 :
                return False
        return True
            

class Game_creator():
    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def createGame(self):
        who_starts = input("Kto zaczyna? Podaj nazwę gracza: ")
        if who_starts == self.player1.name :
            return Game(self.player1, self.player2)
        elif who_starts == self.player2.name :
            return Game(self.player2, self.player1)
        else:
            print("Nie ma takiego gracza. Wpisz jeszcze raz: ")
            return self.createGame()


creator = Game_creator(p1, p2)
 
game = creator.createGame()
game.printInstructions()
game.start()
