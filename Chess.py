from Moves import Pawn, Castle, King, Queen, Empty
import customtkinter as ctk

class Square:
    def __init__(self, coordinate, color, board):
        self.__coordinate= coordinate
        self.__color= color
        self.__board= board
        self.__graphic= None # the image for the piece e.g ♜
        self.__square= None
        self.__positions= {'11':{'x':0, 'y':0},   '12':{'x':0.25,'y':0},    '13':{'x':0.5,'y':0},    '14':{'x':0.75,'y':0},
                           '21':{'x':0,'y':0.25}, '22':{'x':0.25,'y':0.25}, '23':{'x':0.5,'y':0.25}, '24':{'x':0.75,'y':0.25},
                           '31':{'x':0,'y':0.5},  '32':{'x':0.25,'y':0.5},  '33':{'x':0.5,'y':0.5},  '34':{'x':0.75,'y':0.5},
                           '41':{'x':0,'y':0.75}, '42':{'x':0.25,'y':0.75}, '43':{'x':0.5,'y':0.75}, '44':{'x':0.75,'y':0.75}} #Positions of Squares on the screen depending on its assigned coordinate
        self.__fontSize= ctk.CTkFont(size=60)
        self.__position= self.__positions[str(self.__coordinate)]
        self.__piece= None

    def findMoves(self):
        if self.__board.getState() and self.__piece:
            self.__piece.getMoves()
            self.__square.configure(state= 'enabled')
        if self.__piece:
            self.__board.setState()
        if self.__board.getState():
            for square in self.__board.getSquares().values():                
                square.getSquare().configure(state= 'normal')
                square.updateLook()

    def createSquareButton(self):
        self.__square = ctk.CTkButton(self.__board.getBoard(), width=100, height=100, text=self.__graphic, fg_color= self.__color, 
                                      hover_color= '#94b06c', corner_radius= 3, font= self.__fontSize, command= lambda: self.findMoves())
        self.__square.place(relx= self.__position['x'], rely=self.__position['y'])

    def updateLook(self):
        pieceColor= self.__color
        if self.__piece:
            pieceColor= self.__piece.getColor()
        self.__square.configure(text= self.__graphic, text_color= pieceColor, fg_color= self.__color) #once a piece is created, or moved to a new location, the square button is updated
    
    def setColor(self, newColor):
        self.__square.configure(fg_color= newColor)

    def setGraphic(self, newGraphic):
        self.__graphic= newGraphic
        self.updateLook()

    def setPiece(self, newPiece):
        self.__piece= newPiece          
        self.findMoves()

    def getCoordinate(self):
        return self.__coordinate
    
    def getPiece(self):
        return self.__piece
    
    def getSquare(self):
        return self.__square

class Piece:
    def __init__(self, name, square, color, player):        
        self.__square= square
        self.__name= name
        self.__color= color
        self.__piece= self.__name(self) #creates an instace of its 'type' class e.g the Castle/Queen Class so as to get its moves
        self.__player= player

    def getGraphic(self):        
        return self.__piece.getGraphics()[self.__color] #Returns a black-Pawn or white-King etc. to be assigned to the square
    
    def updatePieceSquare(self):
        if self.__square:
            self.__square.setPiece(self)
            self.__square.updateLook()

    def getColor(self):
        return self.__color
    
    def getMoves(self):
        board= self.__player.getBoard()
        moves= self.__piece.getMoves(board)
        for square in list(board.getSquares().values()):
            square.updateLook()
        for square in moves:
            self.__square.setColor('grey')            
            square.setColor('#68a030')
        for square in board.getSquares().values():
            if square not in moves:
                square.getSquare().configure(state= 'disabled')        
        #print(moves, '\n')

    def getSquare(self):
        return self.__square
    
    def getPlayer(self):
        return self.__player
    
    def getPiece(self):
        return self.__piece

class Player:
    def __init__(self, number, board):
        self.__number= number
        self.__pieces= []
        self.__pieceNames= {'1':[Castle, Queen, King, Castle,
                                 Pawn, Pawn, Empty, Queen], 
                            '2':[Pawn, Queen, Empty, Pawn,
                                 Castle, Queen, Castle, King]} #Board organization from top to bottom
        
        self.__colors= {'1':'black', '2':'white'}
        self.__board= board

    def createPieces(self, squares):
        for square in squares:
            squareIndex= squares.index(square)
            pieceName= self.__pieceNames[self.__number][squareIndex] #Assigns the piece's type based on its initial Square position
            pieceColor= self.__colors[self.__number] #Assigns the piece's color based on the player
            if not pieceName.present:
                square= None
            newPiece= Piece(pieceName, square, pieceColor, self)
            newPiece.updatePieceSquare()
            graphic= newPiece.getGraphic()
            if newPiece.getSquare():
                square.setGraphic(graphic)            
            self.__pieces.append(newPiece)

    def getBoard(self):
        return self.__board
    
    def getNumber(self):
        return self.__number

class Board:
    def __init__(self):
        self.__players= []
        self.__squares= {}
        self.__columns= [1,2,3,4]
        self.__rows= [1,2,3,4]        
        self.__colors= ['#c6947a','#7c4529','#c6947a','#7c4529',
                        '#7c4529','#c6947a','#7c4529','#c6947a',
                        '#c6947a','#7c4529','#c6947a','#7c4529',
                        '#7c4529','#c6947a','#7c4529','#c6947a']  #Alternating Square colors; in hex format
        self.__board= ctk.CTk(); self.__board.geometry('400x400'); self.__board.title('4x4 Silverman Chess')
        self.__state= True

    def createSquares(self):
        newColor= 0        
        for column in self.__columns:
            for row in self.__rows:
                coordinate= int(f'{column}{row}') #Combining column and row to get unique Coordinate e.g 'a1', 'c4'
                color= self.__colors[newColor]
                newSquare= Square(coordinate, color, self)
                newSquare.createSquareButton()
                self.__squares[coordinate]= newSquare #Add the coordinate and its Square to the Squares dictionary
                newColor+= 1

    def createPlayers(self): 
        squares= list(self.__squares.values())       
        middleSquare= len(squares) // 2 # Split the Squares into two parts        
        playerSquares= [squares[:middleSquare], squares[middleSquare:]] #A list with the initial Squares for the 2 players
        for i in range(2):
            newPlayer= Player(str(i+1), self)
            newPlayer.createPieces(playerSquares[i]) #Each Player gets assigned the Squares for their Pieces at the start
            self.__players.append(newPlayer)
        for square in self.__squares.values():
            square.getSquare().configure(state= 'normal')

    def setup(self):
        self.createSquares()
        self.createPlayers()
        self.__board.mainloop()

    def getSquares(self):
        return self.__squares
    
    def getState(self):
        return self.__state
    
    def getBoard(self):
        return self.__board
    
    def setState(self):
        if self.__state:
            self.__state= False
        else:
            self.__state= True

chess= Board()
chess.setup()