class Pawn:
    present= True
    def __init__(self, piece):
        self.__graphic= {'black':'♙', 'white':'♟'}        
        self.__allowedMoves= {'1':{'forward': [1,0], 'diagonalL': [1,-1], 'diagonalR': [1,1]},
                              '2':{'forward': [-1,0], 'diagonalL': [-1,1], 'diagonalR': [-1,-1]}}
        self.__board= None
        self.__piece= piece
        self.__allowedSquares= []
        self.__present= Pawn.present

    def getPresent(self):
        return self.__present

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
        playerNumber= self.__piece.getPlayer().getNumber()        
        if move in list(self.__allowedMoves[playerNumber].values()):
            allowedMove= next(direction for direction, vector in self.__allowedMoves[playerNumber].items() if vector == move)
            condition= self.checkSquareCondition(square, allowedMove)
            if condition:
                self.__allowedSquares.append(square)
    
    def getSquares(self):        
        for square in list(self.__board.getSquares().values()):            
            self.checkAllowed(square)        

    def getMoves(self, board):        
        self.__allowedSquares= []
        self.__board= board
        self.getSquares()        
        return self.__allowedSquares

class King:
    present= True
    def __init__(self, piece):
        self.__graphic= {'black':'♔', 'white':'♚'}
        self.__allowedMoves= {'forward': [-1,0], 'diagonal1': [-1,-1], 'diagonal2': [-1,1],
                              'right': [0,-1], 'left': [0,1],
                              'backward': [1,0], 'diagonal3': [1,-1], 'diagonal4': [1,1]}
        self.__board= None
        self.__piece= piece
        self.__allowedSquares= []
        self.__present= King.present

    def getPresent(self):
        return self.__present

    def checkSquareCondition(self, square):
        pieceOnSquare= square.getPiece()
        condition= True
        #print(pieceOnSquare)
        if pieceOnSquare:
            condition= (pieceOnSquare.getPlayer().getNumber() != self.__piece.getPlayer().getNumber())                
        return condition

    def getGraphics(self):
        return self.__graphic
    
    def checkAllowed(self, square):
        squareCoordinate= list(map(int, str(square.getCoordinate())))
        pieceCoordinate= list(map(int, str(self.__piece.getSquare().getCoordinate())))
        move= [a - b for a, b in zip(squareCoordinate, pieceCoordinate)]                   
        if move in list(self.__allowedMoves.values()):
            condition= self.checkSquareCondition(square)
            if condition:
                self.__allowedSquares.append(square)

    def getSquares(self):        
        for square in list(self.__board.getSquares().values()):            
            self.checkAllowed(square)

    def getMoves(self, board):        
        self.__allowedSquares= []
        self.__board= board
        self.getSquares()        
        return self.__allowedSquares

class Castle:
    present= True
    def __init__(self, piece):
        self.__graphic= {'black':'♖', 'white':'♜'}
        self.__moves= []
        self.__allowedMoves= {'forward':[[-1,0],[-2,0],[-3,0]], 'backward':[[1,0],[2,0],[3,0]], 
                              'right':[[0,-1],[0,-2],[0,-3]], 'left':[[0,1],[0,2],[0,3]]}
        self.__board= None
        self.__piece= piece
        self.__allowedSquares= None
        self.__paths= {}
        self.__present= Castle.present

    def getPresent(self):
        return self.__present

    def findEnd(self):
        playerNumber= self.__piece.getPlayer().getNumber()
        for direction in list(self.__allowedSquares.keys()):
            squares= self.__allowedSquares[direction]            
            if playerNumber== '2':
                squares.reverse()
            remove= False
            for square in squares:
                pieceOnSquare= square.getPiece()
                if remove:
                    squares.remove(square)                    
                if pieceOnSquare:                    
                    remove= True                
            self.__allowedSquares[direction]= squares

    def endPath(self, move, allowedMove):  
        path= self.__paths[allowedMove]      
        moveIndex= path.index(move)
        pastEnd= len(path)-moveIndex
        for i in range(pastEnd):
            path.pop()        

    def checkSquareCondition(self, square, allowedMove, move):
        pieceOnSquare= square.getPiece()
        condition= True       
        #print(pieceOnSquare) 
        if pieceOnSquare:
            condition= (pieceOnSquare.getPlayer().getNumber() != self.__piece.getPlayer().getNumber())
        if not condition:
            pass
            self.endPath(move, allowedMove)
        return condition

    def getGraphics(self):
        return self.__graphic
    
    def checkAllowed(self, square):
        squareCoordinate= list(map(int, str(square.getCoordinate())))
        pieceCoordinate= list(map(int, str(self.__piece.getSquare().getCoordinate())))
        move= [a - b for a, b in zip(squareCoordinate, pieceCoordinate)]          
        for moves in list(self.__allowedMoves.values()):
            allowedMove= next(direction for direction, vector in self.__allowedMoves.items() if vector == moves)
            if move in moves:                
                condition= self.checkSquareCondition(square, allowedMove, move)                
                if condition and (move in self.__paths[allowedMove]):
                    self.__allowedSquares[allowedMove].append(square)                   

    def getSquares(self):        
        for square in list(self.__board.getSquares().values()):            
            self.checkAllowed(square)

    def getMoves(self, board):
        self.__moves= []
        for direction in list(self.__allowedMoves.keys()):
            self.__paths[direction]= self.__allowedMoves[direction]
        self.__allowedSquares= {'forward':[],'backward':[],
                                'right':[],'left':[]}
        self.__board= board
        self.getSquares()
        self.findEnd()              
        for squares in list(self.__allowedSquares.values()):            
            for square in squares:                
                self.__moves.append(square)  
        print(self.__moves)      
        return self.__moves

class Queen:
    present= True
    def __init__(self, piece):
        self.__graphic= {'black':'♕', 'white':'♛'}
        self.__moves= []
        self.__allowedMoves= {'forward':[[-1,0],[-2,0],[-3,0]], 'diagonal1':[[-1,-1],[-2,-2],[-3,-3]], 'diagonal2':[[-1,1],[-2,2],[-3,3]],
                              'right':[[0,-1],[0,-2],[0,-3]], 'left':[[0,1],[0,2],[0,3]],
                              'backward':[[1,0],[2,0],[3,0]], 'diagonal3':[[1,-1],[2,-2],[3,-3]], 'diagonal4':[[1,1],[2,2],[3,3]]}
        self.__board= None
        self.__piece= piece
        self.__allowedSquares= None
        self.__paths= {}
        self.__present= Queen.present

    def getPresent(self):
        return self.__present

    def findEnd(self):
        playerNumber= self.__piece.getPlayer().getNumber()
        for direction in list(self.__allowedSquares.keys()):
            squares= self.__allowedSquares[direction]
            if playerNumber== '2':
                squares.reverse()
            remove= False
            for square in squares:
                pieceOnSquare= square.getPiece()
                if remove:                    
                    squares.remove(square)                    
                if pieceOnSquare:                    
                    remove= True                
            self.__allowedSquares[direction]= squares            

    def endPath(self, move, allowedMove):  
        path= self.__paths[allowedMove]      
        moveIndex= path.index(move)
        pastEnd= len(path)-moveIndex
        for i in range(pastEnd):
            path.pop()        

    def checkSquareCondition(self, square, allowedMove, move):
        pieceOnSquare= square.getPiece()        
        condition= True
        #print(pieceOnSquare)
        if pieceOnSquare:
            condition= (pieceOnSquare.getPlayer().getNumber() != self.__piece.getPlayer().getNumber())
        if not condition:
            self.endPath(move, allowedMove)
        return condition

    def getGraphics(self):
        return self.__graphic
    
    def checkAllowed(self, square):
        squareCoordinate= list(map(int, str(square.getCoordinate())))
        pieceCoordinate= list(map(int, str(self.__piece.getSquare().getCoordinate())))
        move= [a - b for a, b in zip(squareCoordinate, pieceCoordinate)]          
        for moves in list(self.__allowedMoves.values()):
            allowedMove= next(direction for direction, vector in self.__allowedMoves.items() if vector == moves)
            if move in moves:                
                condition= self.checkSquareCondition(square, allowedMove, move)                
                if condition and (move in self.__paths[allowedMove]):
                    self.__allowedSquares[allowedMove].append(square)                   

    def getSquares(self):        
        for square in list(self.__board.getSquares().values()):            
            self.checkAllowed(square)        

    def getMoves(self, board):
        self.__moves= []
        for direction in list(self.__allowedMoves.keys()):
            self.__paths[direction]= self.__allowedMoves[direction]
        self.__allowedSquares= {'forward':[],'diagonal1':[],'diagonal2':[],
                                'right':[],'left':[],
                                'backward':[],'diagonal3':[],'diagonal4':[]}
        self.__board= board
        self.getSquares()
        self.findEnd()        
        for squares in list(self.__allowedSquares.values()):            
            for square in squares:
                self.__moves.append(square)        
        return self.__moves
    
class Empty:
    present= False
    def __init__(self, piece):
        self.__graphic= {'black':None, 'white':None}
        self.__present= Empty.present

    def getPresent(self):
        return self.__present

    def getGraphics(self):
        return self.__graphic
    
    def getMoves(self, board):
        return []