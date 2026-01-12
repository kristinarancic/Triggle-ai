from triangle import Triangle
import copy
#atributi: dimension, boardMatrix, edgeList, indeksiSlova

class Board:
    def __init__(self, n) -> None:
        self.dimension=n
        self._createBoard()

    #lista grana
    edgeList = set()
    
    #Funkcija za kreiranje table
    def _createBoard(self):
        dimX=2*(self.dimension-2)+2 #broj vrsta, vertikalno je dimenzija dimX
        dimY=4*(self.dimension-2)+3 #broj kolona, horizontalno je dimenzjia dimY
        self.boardMatrix=list()

        self.indeksiSlova=list()
        pom=ord('A')
        for x in range(0, 2*self.dimension-1):
            self.indeksiSlova.append(chr(pom))
            pom=pom+1

        for i in range(dimX):
            counter=1
            flag = True
            pomLista=list()
            for j in range(dimY):
                trougao = Triangle()
                if(i+j<=self.dimension-3 or i-j>=self.dimension or j-i>=(self.dimension-1)*3 or i+j>=5*self.dimension-6):
                    trougao.addValue('#')
                else:
                    # trougao.addValue('X')
                    trougao.isValid = True

                    if(i<dimX/2):
                        if(flag):
                            trougao.addPoints((self.indeksiSlova[i], counter),(self.indeksiSlova[i+1],counter), (self.indeksiSlova[i+1],counter+1))
                        else:
                            trougao.addPoints((self.indeksiSlova[i], counter),(self.indeksiSlova[i],counter+1), (self.indeksiSlova[i+1],counter+1))
                            counter+=1
                    else:
                        if(flag):
                            trougao.addPoints((self.indeksiSlova[i], counter),(self.indeksiSlova[i],counter+1), (self.indeksiSlova[i+1],counter))
                        else:
                            trougao.addPoints((self.indeksiSlova[i], counter+1),(self.indeksiSlova[i+1],counter), (self.indeksiSlova[i+1],counter+1))
                            counter+=1
                    flag = not flag
                pomLista.append(trougao)
                
            self.boardMatrix.append(pomLista)

    def headerAndFooter(self):
        print()
        indeksiBrojevi=list(range(1, 2*self.dimension))
        horizontal = list()
        horizontal = indeksiBrojevi
        space = str(" "*((self.dimension-1)*int(6/2)+int(6/2)+4))
        print(space, end="")
        for x in horizontal:
            print(x, end="")
            print(str(" "*5), end="")
        print("\n")

    #Funkcija za prikaz trenutnog stanja table
    def printBoard(self) :
        self.headerAndFooter()
        print_matrix = list()
        up_slash = ' /'
        up_backslash = '\\ '
        down_slash = '/ '
        down_backslash  = ' \\'
        blanko = ' '
        five_dashes = '-----'
        five_spaces = '     '

        lineNodes=self.dimension
        for i in range(len(self.indeksiSlova)):
            #Pravljenje reda 3 reda:
            elements = list()
            for node in range(lineNodes):
                elements.append('@')
                edge = ((self.indeksiSlova[i], node+1),(self.indeksiSlova[i], node+2))
                if(node != lineNodes-1):
                    if(edge in self.edgeList or (edge[1], edge[0]) in self.edgeList):
                        elements+=five_dashes
                    else:
                        elements+=five_spaces
            if(i<int(len(self.indeksiSlova)/2)):
                lineNodes+=1
            else:
                lineNodes-=1
            
            if(i<=int(len(self.indeksiSlova)/2)):
                justify = str(" "*((self.dimension-(i+1))*int(6/2)+int(6/2)))
                elements = self.indeksiSlova[i] + justify + (''.join(elements))
            else:
                justify = justify + " "*int(6/2)
                elements = self.indeksiSlova[i] + justify + (''.join(elements))
            
            print_matrix.append(elements)

            if(i<len(self.boardMatrix)):
                #Idemo medjuredove
                topRow = list()
                bottomRow = list()
                first = True
                counter = 0
                
                index=0
                while(index < len(self.boardMatrix[i])):
                # for index in range(len(self.boardMatrix[i])):
                    if(i<int(len(self.indeksiSlova)/2)):
                        if(self.boardMatrix[i][index].isValid):
                            counter+=1
                            if(first): 
                                edge = ((self.indeksiSlova[i], 1), (self.indeksiSlova[i+1], 1))
                                if(edge in self.edgeList or (edge[1], edge[0]) in self.edgeList):
                                    topRow.append(up_slash)
                                    bottomRow.append(down_slash)
                                else:
                                    topRow.append(blanko+blanko)
                                    bottomRow.append(blanko+blanko)
                                first = False
                                    
                            #Uspravni trouglici
                            edge = ((self.indeksiSlova[i], counter), (self.indeksiSlova[i+1], counter+1))
                            if(edge in self.edgeList or (edge[1], edge[0]) in self.edgeList):
                                topRow.append(down_backslash+blanko)
                                bottomRow.append(self.boardMatrix[i][index].fieldValue if self.boardMatrix[i][index].fieldValue else blanko)
                                bottomRow.append(down_backslash)
                            else:
                                topRow.append(blanko+blanko+blanko)
                                bottomRow.append(blanko+blanko+blanko)
                            index+=1
                            #Okrenuti trouglici
                            edge = ((self.indeksiSlova[i], counter+1), (self.indeksiSlova[i+1], counter+1))
                            if(edge in self.edgeList or (edge[1], edge[0]) in self.edgeList):
                                topRow.append(self.boardMatrix[i][index].fieldValue if self.boardMatrix[i][index].fieldValue else blanko)
                                topRow.append(up_slash)#' /'
                                bottomRow.append(up_slash+blanko)#' /'
                            else:
                                topRow.append(blanko+blanko+blanko)
                                bottomRow.append(blanko+blanko+blanko)
                            

                    else:#donji deo
                        if(self.boardMatrix[i][index].isValid):
                            counter+=1
                            if(first): 
                                edge = ((self.indeksiSlova[i], 1), (self.indeksiSlova[i+1], 1))
                                if(edge in self.edgeList or (edge[1], edge[0]) in self.edgeList):
                                    topRow.append(up_backslash)
                                    bottomRow.append(down_backslash)
                                else:
                                    topRow.append(blanko+blanko)
                                    bottomRow.append(blanko+blanko)
                                first = False
                            
                            #Okrenuti trouglici
                            edge = ((self.indeksiSlova[i], counter+1), (self.indeksiSlova[i+1], counter))
                            if(edge in self.edgeList or (edge[1], edge[0]) in self.edgeList):
                                topRow.append(self.boardMatrix[i][index].fieldValue if self.boardMatrix[i][index].fieldValue else blanko)
                                topRow.append(up_slash)
                                bottomRow.append(up_slash+blanko)
                            else:
                                topRow.append(blanko+blanko+blanko)
                                bottomRow.append(blanko+blanko+blanko)
                            index+=1

                            #Uspravni trouglici
                            edge = ((self.indeksiSlova[i], counter+1), (self.indeksiSlova[i+1], counter+1))
                            if(edge in self.edgeList or (edge[1], edge[0]) in self.edgeList):
                                topRow.append(down_backslash+blanko)
                                bottomRow.append(self.boardMatrix[i][index].fieldValue if self.boardMatrix[i][index].fieldValue else blanko)
                                bottomRow.append(down_backslash)
                            else:
                                topRow.append(blanko+blanko+blanko)
                                bottomRow.append(blanko+blanko+blanko)
                            
                    index+=1
                if(i<int(len(self.indeksiSlova)/2)):
                    justify_pom = str(" "*((self.dimension-(i+1))*int(6/2)+int(6/2)-1))
                    topRow = justify_pom + (''.join(topRow))
                    topRow = topRow.rstrip()
                    bottomRow = justify_pom + (''.join(bottomRow))
                    bottomRow = bottomRow.rstrip()
                else:
                    if(i != len(self.indeksiSlova)//2):
                        justify_pom = justify_pom + " "*int(6/2)
                    topRow = justify_pom + (''.join(topRow))
                    topRow = topRow.rstrip()
                    bottomRow = justify_pom + (''.join(bottomRow))
                    bottomRow = bottomRow.rstrip()

                print_matrix.append(topRow)
                print_matrix.append(bottomRow)

        for i in range(len(print_matrix)):
            for j in range(len(print_matrix[i])):
                print(print_matrix[i][j], end="")
            print()
        
        self.headerAndFooter()


    #Funkcija za pravljenje grana na osnovu dve tacke
    def makeEdge(self, startPoint, endPoint):
        #startPoint i endPoint su tuple
        if(startPoint[0] < endPoint[0] or (startPoint[0] == endPoint[0] and startPoint[1] < endPoint[1])):
            edge = (startPoint, endPoint)
        else:
            edge = (endPoint, startPoint)

        for i in self.edgeList:
            if i == (startPoint, endPoint) or i== (endPoint, startPoint):
                return
   
        self.edgeList.add(edge)
        return
    
    #Funkcija koja pravi sve grane (proizvoljno trenutno stanje)
    def createAllEdges(self):
        pom=self.dimension
        for i in range(len(self.indeksiSlova)//2):
            for j in range(1,pom+1):
                if j!=pom:
                    self.makeEdge((self.indeksiSlova[i],j),(self.indeksiSlova[i],j+1))
                self.makeEdge((self.indeksiSlova[i],j),(self.indeksiSlova[i+1],j))
                self.makeEdge((self.indeksiSlova[i],j),(self.indeksiSlova[i+1],j+1))
            pom+=1
        pom=self.dimension
        for j in range(1 ,len(self.indeksiSlova)):
            self.makeEdge((self.indeksiSlova[len(self.indeksiSlova)//2],j),(self.indeksiSlova[len(self.indeksiSlova)//2],j+1))

        for i in range(len(self.indeksiSlova)-1, len(self.indeksiSlova)//2, -1):
            for j in range(1,pom+1):
                if j!=pom:
                    self.makeEdge((self.indeksiSlova[i],j),(self.indeksiSlova[i],j+1))
                self.makeEdge((self.indeksiSlova[i],j),(self.indeksiSlova[i-1],j))
                self.makeEdge((self.indeksiSlova[i],j),(self.indeksiSlova[i-1],j+1))
            pom+=1

    #Funkcija za proveru kraja igre
    def isEndOfGame(self):
        countX = 0
        countO = 0
        countEmpty = 0

        for index in self.boardMatrix:
            for triangle in index:
                if(triangle.fieldValue == "X"):
                    countX+=1
                elif(triangle.fieldValue == "O"):
                    countO+=1
                elif(triangle.fieldValue == None and triangle.isValid):
                    countEmpty+=1
        print(f"X:{countX}")
        print(f"O:{countO}")
        
        matrixSize = countX+countEmpty+countO

        if(countEmpty == 0):
            if(countO>countX):
                print("Pobedik je igrač O")
                return True
            elif(countX>countO):
                print("Pobedik je igrač X")
                return True
            elif(countX==countO and countO+countX==matrixSize):
                print("Kraj igre! Rezultat je nerešen.")
                return True
        elif(countX > matrixSize/2):
            print("Pobednik je igrač X.")
            return True
        elif(countO > matrixSize/2):
            print("Pobednik je igrač O.")
            return True
            
        return False
    
    #Funkcija za unos poteza
    def inputMove(self, newMove, character, computer_player):
        if(computer_player):
            move = newMove
            letter = move[0]
            number = move[1]
            direction = move[2]
        else:
            move = input("Unesite potez u obliku: slovo, broj, smer: ")
            parts = move.split(",")
        
            if len(parts) == 3:
                letter = parts[0].strip()
                number = int(parts[1].strip())
                direction = parts[2].strip()

                direction=direction.lower()
                letter=letter.upper()

                if(direction not in ["dd", "d", "dl"]):
                    print("Nevalidan smer kretanja!")
                    return False
                
                if(letter not in self.indeksiSlova):
                    print("Nevalidno slovo!")
                    return False
                
                if(number not in range(1, len(self.indeksiSlova)+1)):
                    print("Nevalidan broj!")
                    return False
        
                print(f"Uneli ste: Slovo: {letter}, Broj: {number}, Smer: {direction}")
            else:
                print("Nevalidan format! Molimo unesite u obliku: slovo, broj, smer")
                return False 

        edgePom=list()
        #Validnost:
        #udesno
        if(direction=='d'):
            #pom je opseg u odgovarajucem redu
            pom=len(self.indeksiSlova)-abs(self.indeksiSlova.index(self.indeksiSlova[len(self.indeksiSlova)//2])-self.indeksiSlova.index(letter))
            if(number+3>pom):
                print("Pokušani potez izlazi iz opsega!")
                return False
            
            edgePom.append(((letter, number), (letter, number+1)))
            edgePom.append(((letter, number+1), (letter, number+2)))
            edgePom.append(((letter, number+2), (letter, number+3)))
            
        #dole desno
        if(direction=='dd'):
            pom=len(self.indeksiSlova)-abs(self.indeksiSlova.index(self.indeksiSlova[len(self.indeksiSlova)//2])-(self.indeksiSlova.index(letter)+3))
            #sve 3 grane u gumici su iznad polovine
            if(self.indeksiSlova.index(letter)<=len(self.indeksiSlova)//2-3):
                if(number+3>pom):
                    print("Pokušani potez izlazi iz opsega!")
                    return False
                for i in range(3):
                    edgePom.append(((chr(ord(letter)+i), number+i), (chr(ord(letter)+i+1), number+i+1)))
            #2 grane su iznad polovine, 1 ispod
            elif(self.indeksiSlova.index(letter)==len(self.indeksiSlova)//2-2):
                if(number+2>pom):
                    print("Pokušani potez izlazi iz opsega!")
                    return False
                edgePom.append(((letter, number), (chr(ord(letter)+1), number+1)))
                edgePom.append(((chr(ord(letter)+1), number+1), (chr(ord(letter)+2), number+2)))
                edgePom.append(((chr(ord(letter)+2), number+2), (chr(ord(letter)+3), number+2)))
            #1 grana je iznad polovine, 2 ispod
            elif(self.indeksiSlova.index(letter)==len(self.indeksiSlova)//2-1):
                if(number+1>pom):
                    print("Pokušani potez izlazi iz opsega!")
                    return False
                edgePom.append(((letter, number), (chr(ord(letter)+1), number+1)))
                edgePom.append(((chr(ord(letter)+1), number+1), (chr(ord(letter)+2), number+1)))
                edgePom.append(((chr(ord(letter)+2), number+1), (chr(ord(letter)+3), number+1)))
            #sve 3 grane su ispod polovine
            else:
                if(number>pom or not chr(ord(letter)+3) in self.indeksiSlova):
                    print("Pokušani potez izlazi iz opsega!")
                    return False
                for i in range(3):
                    edgePom.append(((chr(ord(letter)+i), number), (chr(ord(letter)+i+1), number)))

        #dole levo
        if(direction=='dl'):
            pom=len(self.indeksiSlova)-abs(self.indeksiSlova.index(self.indeksiSlova[len(self.indeksiSlova)//2])-(self.indeksiSlova.index(letter)+3))
            #sve 3 grane su iznad polovine
            if(self.indeksiSlova.index(letter)<=len(self.indeksiSlova)//2-3):
                if(number<1):
                    print("Pokušani potez izlazi iz opsega!")
                    return False
                for i in range(3):
                    edgePom.append(((chr(ord(letter)+i), number), (chr(ord(letter)+i+1), number)))
            #2 grane su iznad, 1 ispod polovine
            elif(self.indeksiSlova.index(letter)==len(self.indeksiSlova)//2-2):
                if(number-1<1):
                    print("Pokušani potez izlazi iz opsega!")
                    return False
                edgePom.append(((letter, number), (chr(ord(letter)+1), number)))
                edgePom.append(((chr(ord(letter)+1), number), (chr(ord(letter)+2), number)))
                edgePom.append(((chr(ord(letter)+2), number), (chr(ord(letter)+3), number-1)))
            #1 grana iznad, 2 ispod polovine
            elif(self.indeksiSlova.index(letter)==len(self.indeksiSlova)//2-1):
                if(number-2<1):
                    print("Pokušani potez izlazi iz opsega!")
                    return False
                edgePom.append(((letter, number), (chr(ord(letter)+1), number)))
                edgePom.append(((chr(ord(letter)+1), number), (chr(ord(letter)+2), number-1)))
                edgePom.append(((chr(ord(letter)+2), number-1), (chr(ord(letter)+3), number-2)))
            #sve 3 grane su ispod polovine
            else:
                if(number-3<1 or not chr(ord(letter)+3) in self.indeksiSlova):
                    print("Pokušani potez izlazi iz opsega!")
                    return False
                edgePom.append(((chr(ord(letter)), number), (chr(ord(letter)+1), number-1)))
                edgePom.append(((chr(ord(letter)+1), number-1), (chr(ord(letter)+2), number-2)))
                edgePom.append(((chr(ord(letter)+2), number-2), (chr(ord(letter)+3), number-3)))
                       
        #Proveravamo da smo u opsegu brojeva, da gumica vec ne postoji i dodajemo grane i pravimo trouglice
        pom=len(self.indeksiSlova)-abs(self.indeksiSlova.index(self.indeksiSlova[len(self.indeksiSlova)//2])-self.indeksiSlova.index(letter))
        if(number > pom):
            print("Nevalidan potez! Izlazite iz opsega brojeva")
            return False

        if(edgePom[0] in self.edgeList and edgePom[1] in self.edgeList and edgePom[2] in self.edgeList):
            print("Na ovim poljima već postoje gumice")
            return False
        else:
            self.makeEdge(edgePom[0][0], edgePom[0][1])
            self.makeEdge(edgePom[1][0], edgePom[1][1])
            self.makeEdge(edgePom[2][0], edgePom[2][1])

        self.addTriangleValue(edgePom[0], edgePom[1], edgePom[2], character, self.boardMatrix, self.edgeList)
        return True
            

    #funkcija za ispunjavanje trouglica, ako je potrebno
    def addTriangleValue(self, edge1, edge2, edge3, character, matrix, edges):
        pointsList = [edge1[0], edge1[1], edge2[1], edge3[1]]
        for index in range(3):
            for row in matrix:
                for trig in row:
                    if(pointsList[index] in trig.points and pointsList[index+1] in trig.points):
                        edgeListPom=list(trig.points)
                        edge1 = (edgeListPom[0], edgeListPom[1])
                        edge2 = (edgeListPom[1], edgeListPom[2])
                        edge3 = (edgeListPom[2], edgeListPom[0])
                        if((edge1 in edges or (edgeListPom[1], edgeListPom[0]) in edges) and (edge2 in edges or (edgeListPom[2], edgeListPom[1]) in edges) and (edge3 in edges or (edgeListPom[0], edgeListPom[2]) in edges)):
                            if(trig.fieldValue == None):
                                trig.addValue(character)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def newGameState(self, state, move, character):

        newStateMatrix = copy.deepcopy(state[0])
        newEdgeList = copy.deepcopy(state[1])
        edgePom=tuple()
        edgePom=self.defineMove(state, move)

        if(edgePom == None):
            print("None")
            return (newStateMatrix, newEdgeList)
        
        newEdgeList.add((edgePom[0][0], edgePom[0][1]))
        newEdgeList.add((edgePom[1][0], edgePom[1][1]))
        newEdgeList.add((edgePom[2][0], edgePom[2][1]))

        self.addTriangleValue(edgePom[0], edgePom[1], edgePom[2], character, newStateMatrix, newEdgeList)

        return (newStateMatrix, newEdgeList)
    
    #Funkcija koja na osnovu zadatog igrača na potezu i zadatog stanje igre (table) formira sve moguće poteze 
    def allPossibleMoves(self, character, state):
        #idemo kroz svaki stubic i proveravamo da li moze da se postavi gumica pomocu defineMove funkcije i dodajemo u listu moveList sve moguce poteze
        moveList = set()
        for row in self.indeksiSlova:
            pom=len(self.indeksiSlova)-abs(self.indeksiSlova.index(self.indeksiSlova[len(self.indeksiSlova)//2])-self.indeksiSlova.index(row))
            for column in range(1, pom+1):
                edgePom = self.defineMove(state, (row, column, "d"))
                if(edgePom != None):
                    moveList.add((row, column, "d"))
                edgePom = self.defineMove(state, (row, column, "dd"))
                if(edgePom != None):
                    moveList.add((row, column, "dd"))
                edgePom = self.defineMove(state, (row, column, "dl"))
                if(edgePom != None):
                    moveList.add((row, column, "dl"))

        return moveList
    
    #Funkcija koja na osnovu svih mogućih poteza formira sva moguća stanja igre, pomocu allPossibleMoves i newGameState
    def allPossibleStates(self, state, character):
        moveList = set() 
        pomTuple = tuple()
        states = list()
        moveList = self.allPossibleMoves(character, state)

        for move in moveList:
            pomTuple = self.newGameState(state, move, character)
            states.append(pomTuple)
            
        return states


    #Funkcija koju koristimo u allPossibleMoves i newGameState
    def defineMove(self, state, move):
        #hocemo da vracamo tri formirane grane na osnovu prosledjenog poteza
        letter = move[0]
        number = move[1]
        direction = move[2]
        edgePom=list()
        
        direction=direction.lower()
        letter=letter.upper()

        #Validnost:
        #udesno
        if(direction=='d'):
            #pom je opseg u odgovarajucem redu
            pom=len(self.indeksiSlova)-abs(self.indeksiSlova.index(self.indeksiSlova[len(self.indeksiSlova)//2])-self.indeksiSlova.index(letter))
            if(number+3>pom):
                return None
                
            edgePom.append(((letter, number), (letter, number+1)))
            edgePom.append(((letter, number+1), (letter, number+2)))
            edgePom.append(((letter, number+2), (letter, number+3)))
                
        #dole desno
        if(direction=='dd'):
            pom=len(self.indeksiSlova)-abs(self.indeksiSlova.index(self.indeksiSlova[len(self.indeksiSlova)//2])-(self.indeksiSlova.index(letter)+3))
            #sve 3 grane u gumici su iznad polovine
            if(self.indeksiSlova.index(letter)<=len(self.indeksiSlova)//2-3):
                if(number+3>pom):
                    return None
                for i in range(3):
                    edgePom.append(((chr(ord(letter)+i), number+i), (chr(ord(letter)+i+1), number+i+1)))
            #2 grane su iznad polovine, 1 ispod
            elif(self.indeksiSlova.index(letter)==len(self.indeksiSlova)//2-2):
                if(number+2>pom):
                    return None
                edgePom.append(((letter, number), (chr(ord(letter)+1), number+1)))
                edgePom.append(((chr(ord(letter)+1), number+1), (chr(ord(letter)+2), number+2)))
                edgePom.append(((chr(ord(letter)+2), number+2), (chr(ord(letter)+3), number+2)))
            #1 grana je iznad polovine, 2 ispod
            elif(self.indeksiSlova.index(letter)==len(self.indeksiSlova)//2-1):
                if(number+1>pom):
                    return None
                edgePom.append(((letter, number), (chr(ord(letter)+1), number+1)))
                edgePom.append(((chr(ord(letter)+1), number+1), (chr(ord(letter)+2), number+1)))
                edgePom.append(((chr(ord(letter)+2), number+1), (chr(ord(letter)+3), number+1)))
            #sve 3 grane su ispod polovine
            else:
                if(number>pom or not chr(ord(letter)+3) in self.indeksiSlova):
                    return None
                for i in range(3):
                    edgePom.append(((chr(ord(letter)+i), number), (chr(ord(letter)+i+1), number)))

        #dole levo
        if(direction=='dl'):
            pom=len(self.indeksiSlova)-abs(self.indeksiSlova.index(self.indeksiSlova[len(self.indeksiSlova)//2])-(self.indeksiSlova.index(letter)+3))
            #sve 3 grane su iznad polovine
            if(self.indeksiSlova.index(letter)<=len(self.indeksiSlova)//2-3):
                if(number<1):
                    return None
                for i in range(3):
                    edgePom.append(((chr(ord(letter)+i), number), (chr(ord(letter)+i+1), number)))
            #2 grane su iznad, 1 ispod polovine
            elif(self.indeksiSlova.index(letter)==len(self.indeksiSlova)//2-2):
                if(number-1<1):
                    return None
                edgePom.append(((letter, number), (chr(ord(letter)+1), number)))
                edgePom.append(((chr(ord(letter)+1), number), (chr(ord(letter)+2), number)))
                edgePom.append(((chr(ord(letter)+2), number), (chr(ord(letter)+3), number-1)))
            #1 grana iznad, 2 ispod polovine
            elif(self.indeksiSlova.index(letter)==len(self.indeksiSlova)//2-1):
                if(number-2<1):
                    return None
                edgePom.append(((letter, number), (chr(ord(letter)+1), number)))
                edgePom.append(((chr(ord(letter)+1), number), (chr(ord(letter)+2), number-1)))
                edgePom.append(((chr(ord(letter)+2), number-1), (chr(ord(letter)+3), number-2)))
            #sve 3 grane su ispod polovine
            else:
                if(number-3<1 or not chr(ord(letter)+3) in self.indeksiSlova):
                    return None
                edgePom.append(((chr(ord(letter)), number), (chr(ord(letter)+1), number-1)))
                edgePom.append(((chr(ord(letter)+1), number-1), (chr(ord(letter)+2), number-2)))
                edgePom.append(((chr(ord(letter)+2), number-2), (chr(ord(letter)+3), number-3)))
                        
        #Proveravamo da smo u opsegu brojeva, da gumica vec ne postoji i dodajemo grane i pravimo trouglice
        pom=len(self.indeksiSlova)-abs(self.indeksiSlova.index(self.indeksiSlova[len(self.indeksiSlova)//2])-self.indeksiSlova.index(letter))
        if(number > pom):
            return None

        if(edgePom[0] in state[1] and edgePom[1] in state[1] and edgePom[2] in state[1]):
            return None

        return tuple(edgePom)

#-------------------------------------------------------------------------------------------------------------------------------------------------------
    def countCharacter(self, state):
        countX = 0
        countO = 0

        for index in state[0]:
            for triangle in index:
                if(triangle.fieldValue == "X"):
                    countX+=1
                elif(triangle.fieldValue == "O"):
                    countO+=1

        return (countX, countO)

    def evaluateState(self, state, character):
        countX, countO = self.countCharacter(state)

        return countX-countO if character == 'X' else countO-countX

    def minValue(self, state, depth, alpha, beta, character, move=None):
        newMoves = self.allPossibleMoves(character, state)
        
        if(depth == 0 or newMoves is None or len(newMoves) == 0):
            return (move, self.evaluateState(state, character))
        else:
            for m in newMoves:
                beta = min(beta, self.maxValue(self.newGameState(state, m, character), depth-1, alpha, beta, character,
                           m if move is None else move), key=lambda x: x[1])
                if(beta[1] <= alpha[1]):
                    return alpha
            
        return beta

    def maxValue(self, state, depth, alpha, beta, character, move=None):
        newMoves = self.allPossibleMoves(character, state)
        
        if(depth == 0 or newMoves is None or len(newMoves) == 0):
            return (move, self.evaluateState(state, character))
        else:
            for m in newMoves:
                alpha = max(alpha, self.minValue(self.newGameState(state, m, character), depth-1, alpha, beta, character,
                           m if move is None else move), key=lambda x: x[1])
                if(alpha[1] >= beta[1]):
                    return beta
            
        return alpha

    def minimax(self, state, depth, myMove, character, alpha=(None, -200), beta=(None, 200)):
        if myMove:
            return self.maxValue(state, depth, alpha, beta, character)
        else:
            return self.minValue(state, depth, alpha, beta, character)