#atributi: polje s vrednostima X i O 
#          3 tacke smestene u setovima

class Triangle:
    def __init__(self) -> None:
        self.fieldValue=None
        #mozda kasnije prebacimo u posebne vrenosti za svaku tacku
        self.points=set()
        self.isValid = False
    
    #provericemo da li je vrednost validna kad unosimo stvari
    def addValue(self, value):
        self.fieldValue=value
    
    #p1,p2 i p3 su tuple
    def addPoints(self, p1, p2, p3):
        self.points.add(p1)
        self.points.add(p2)
        self.points.add(p3)

