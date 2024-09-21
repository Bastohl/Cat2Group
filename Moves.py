class Pawn:
    def __init__(self):
        self.__piece= {'black':'♙', 'white':'♟'}

    def getGraphics(self):
        return self.__piece

class Castle:
    def __init__(self):
        self.__piece= {'black':'♖', 'white':'♜'}

    def getGraphics(self):
        return self.__piece

class King:
    def __init__(self):
        self.__piece= {'black':'♔', 'white':'♚'}

    def getGraphics(self):
        return self.__piece

class Queen:
    def __init__(self):
        self.__piece= {'black':'♕', 'white':'♛'}

    def getGraphics(self):
        return self.__piece