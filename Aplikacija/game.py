from board import Board

computer_player = False
character = "X"
N = 0
playerOne = True
playerTwo = False
characterOne = None
characterTwo = None

#Funkcija za proveru koji igrač igra prvi, da li prvo igra X ili O i koje su dimenzije table
def enterParametersThroughConsole():
    global character, computer_player, N, characterOne, characterTwo

    N = input("Unesite dimenziju table: ")

    if(int(N)<1 or int(N)>8):
        print("Nevalidna dimenzija table!")
        return
    
    #Deo iz prve faze za biranje prvog igrača između čoveka i računara
    while(1):
        first_player = input("Ko će igrati prvi? Ako čovek igra prvi unesite 0, ako računar igra prvi unesite 1: ")
        if(first_player == "1"):
            computer_player = True
            break
        elif(first_player == "0"):
            break
        else:
            print("Nevalidan izbor za prvog igrača! Pokusajte ponovo")

    while(1):
        character = input("Koji igrač igra prvi? Za X unesite 0, za O unesite 1: ")
        if(character == "0"):
            characterOne = "X"
            characterTwo = "O"
            print("X je prvi na potezu")
            break
        elif(character == "1"):
            # character = "O"
            characterOne = "O"
            characterTwo = "X"
            print("O je prvi na potezu")
            break
        else:
            print("Nevalidan izbor za karakter!Pokusajte ponovo!")

def playGame(board):
    global playerOne, playerTwo, characterOne, characterTwo

    isEnd = board.isEndOfGame()
    while(not isEnd):
        print("Prvi igrac je na potezu")
        isValidMove=False
        while(not isValidMove):
            isValidMove = board.inputMove(characterOne)
        isEnd = board.isEndOfGame()
        board.printBoard()
        if(isEnd):
            break

        print("Drugi igrac je na potezu")
        isValidMove=False
        while(not isValidMove):
            isValidMove = board.inputMove(characterTwo)
        isEnd = board.isEndOfGame()
        board.printBoard()
        if(isEnd):
            break

def playGameAI(board):
    global playerOne, playerTwo, characterOne, characterTwo, computer_player

    isEnd = board.isEndOfGame()

    while(not isEnd):
        print("Prvi igrac je na potezu")  
        isValidMove=False
        if(computer_player):
            newMoveTuple = board.minimax((board.boardMatrix, board.edgeList), 3, True, characterOne)
            newMove = newMoveTuple[0]
            isValidMove = board.inputMove(newMove, characterOne, computer_player)
        else:
            while(not isValidMove):
                isValidMove = board.inputMove(None, characterOne, computer_player)
        computer_player = not computer_player
        isEnd = board.isEndOfGame()
        board.printBoard()
        if(isEnd):
            break

        print("Drugi igrac je na potezu")
        isValidMove=False
        if(computer_player):
            newMoveTuple = board.minimax((board.boardMatrix, board.edgeList), 3, True, characterTwo)
            newMove = newMoveTuple[0]
            isValidMove = board.inputMove(newMove, characterTwo, computer_player)
        else:
            while(not isValidMove):
                isValidMove = board.inputMove(None, characterTwo, computer_player)
        computer_player = not computer_player
        isEnd = board.isEndOfGame()
        board.printBoard()
        if(isEnd):
            break

#Funkcija za pokretanje igre
def startGame() :

    enterParametersThroughConsole()
    
    board = Board(int(N))
    board.printBoard()

    playGameAI(board)
    

startGame()