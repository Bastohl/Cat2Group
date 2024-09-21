class Pawn:
    def __init__(self, piece):
        self.__graphic= {'black':'♙', 'white':'♟'}
        self.__moves= []
        self.__allowedMoves= {'forward': [1,0], 'diagonalL': [1,1], 'diagonalR': [1,-1]}
        self.__board= None
        self.__piece= piece
        self.__allowedSquares= []

    def checkSquareCondition(self, square, move):
        conditions = {'forward': lambda x: x is None, 'diagonalL': lambda x: x is not None, 'diagonalR': lambda x: x is not None }
        condition = conditions[move](square.getPiece())
        return condition

    def getGraphics(self):
        return self.__graphic
    
    def checkAllowed(self, square):
        squareCoordinate= list(map(int, str(square.getCoordinate())))
        pieceCoordinate= list(map(int, str(self.__piece.getSquare().getCoordinate())))
        move= [a - b for a, b in zip(squareCoordinate, pieceCoordinate)]        
        if move in list(self.__allowedMoves.values()):            
            allowedMove= next(direction for direction, vector in self.__allowedMoves.items() if vector == move)
            condition= self.checkSquareCondition(square, allowedMove)
            if condition:
                self.__allowedSquares.append(square)
    
    def getSquares(self):        
        for square in list(self.__board.getSquares().values()):            
            self.checkAllowed(square)
        print(self.__allowedSquares)

    def getMoves(self, board):
        self.__allowedSquares= []
        self.__board= board
        self.getSquares()
        return self.__moves

class Castle:
    def __init__(self, piece):
        self.__piece= {'black':'♖', 'white':'♜'}

    def getGraphics(self):
        return self.__piece

class King:
    def __init__(self, piece):
        self.__piece= {'black':'♔', 'white':'♚'}

    def getGraphics(self):
        return self.__piece

class Queen:
    def __init__(self, piece):
        self.__piece= {'black':'♕', 'white':'♛'}

    def getGraphics(self):
        return self.__piece