'''
# ♔♕♙♖ ♚♛♟♜
# Composition -> Board has squares, Piece has square, Player has pieces, Board has Players
# Encapsulation -> Data hiding using '__' before attributes
# Abstraction -> Using get and set methods
# Association -> Squares-Board (many-1), Square-Piece (1-1), Players-Board (many-1), Player-Pieces (1-many)), Delegation(Moves File
# Delegation and Dependency -> using Moves.py to store logic behind moves
'''

from Moves import Pawn, Castle, King, Queen
import customtkinter as ctk

class Square:
    def __init__(self, coordinate, color, board):
        self.__coordinate= coordinate
        self.__color= color
        self.__board= board
        self.__graphic= None
        self.__square= None
        self.__positions= {'a1':{'x':0, 'y':0},   'a2':{'x':0.25,'y':0},    'a3':{'x':0.5,'y':0},    'a4':{'x':0.75,'y':0},
                           'b1':{'x':0,'y':0.25}, 'b2':{'x':0.25,'y':0.25}, 'b3':{'x':0.5,'y':0.25}, 'b4':{'x':0.75,'y':0.25},
                           'c1':{'x':0,'y':0.5},  'c2':{'x':0.25,'y':0.5},  'c3':{'x':0.5,'y':0.5},  'c4':{'x':0.75,'y':0.5},
                           'd1':{'x':0,'y':0.75}, 'd2':{'x':0.25,'y':0.75}, 'd3':{'x':0.5,'y':0.75}, 'd4':{'x':0.75,'y':0.75}} #Positions of Squares on the screen depending on its assigned coordinate
        self.__fontSize= ctk.CTkFont(size=60)
        self.__position= self.__positions[self.__coordinate]
        self.__pieceColor= None

    def createSquareButton(self):        
        self.__square = ctk.CTkButton(self.__board, width=126, height=126, text=self.__graphic, fg_color= self.__color, hover_color= 'grey', corner_radius= 3, font= self.__fontSize)
        self.__square.place(relx= self.__position['x'], rely=self.__position['y'])

    def updateGraphic(self):
        self.__square.configure(text= self.__graphic, text_color= self.__pieceColor)

    def setGraphic(self, newGraphic):
        self.__graphic= newGraphic
        self.updateGraphic()

    def setPieceColor(self, newPieceColor):
        self.__pieceColor= newPieceColor

class Piece:
    def __init__(self, name, square, color):
        self.__square= square
        self.__name= name
        self.__color= color
        self.__piece= self.__name() #creates an instace of its 'type' class e.g the Castle/Queen Class so as to get its moves

    def getGraphic(self):        
        return self.__piece.getGraphics()[self.__color] #Returns a black-Pawn or white-King etc. to be assigned to the square
    
    def updatePieceColor(self):
        self.__square.setPieceColor(self.__color)
        self.__square.updateGraphic()

class Player:
    def __init__(self, number):
        self.__number= number
        self.__pieces= []
        self.__pieceNames= {'1':[Castle, Queen, King, Castle, 
                                 Pawn, Pawn, Pawn, Pawn], 
                            '2':[Pawn, Pawn, Pawn, Pawn, 
                                 Castle, Queen, King, Castle]} #Board organization from top to bottom
        
        self.__colors= {'1':'black', '2':'white'}

    def createPieces(self, squares):
        for square in squares:
            squareIndex= squares.index(square)
            pieceName= self.__pieceNames[self.__number][squareIndex] #Assigns the piece's type based on its initial Square position
            pieceColor= self.__colors[self.__number] #Assigns the piece's color based on the player
            newPiece= Piece(pieceName, square, pieceColor)
            newPiece.updatePieceColor()
            graphic= newPiece.getGraphic()
            square.setGraphic(graphic)            
            self.__pieces.append(newPiece)

class Board:
    def __init__(self):
        self.__players= []
        self.__squares= {}
        self.__columns= ['a','b','c','d']
        self.__rows= [1,2,3,4]        
        self.__colors= ['#c6947a','#7c4529','#c6947a','#7c4529',
                        '#7c4529','#c6947a','#7c4529','#c6947a',
                        '#c6947a','#7c4529','#c6947a','#7c4529',
                        '#7c4529','#c6947a','#7c4529','#c6947a']  #Alternating Square colors; in hex format
        self.__board= ctk.CTk(); self.__board.geometry('500x500'); self.__board.title('4x4 Silverman Chess')

    def createSquares(self):
        newColor= 0        
        for column in self.__columns:
            for row in self.__rows:
                coordinate= f'{column}{row}' #Combining column and row to get unique Coordinate e.g 'a1', 'c4'
                color= self.__colors[newColor]
                newSquare= Square(coordinate, color, self.__board)
                newSquare.createSquareButton()
                self.__squares[coordinate]= newSquare #Add the coordinate and its Square to the Squares dictionary
                newColor+= 1

    def createPlayers(self): 
        squares= list(self.__squares.values())       
        middleSquare= len(squares) // 2 # Split the Squares into two parts        
        playerSquares= [squares[:middleSquare], squares[middleSquare:]] #A list with the initial Squares for the 2 players
        for i in range(2):
            newPlayer= Player(str(i+1))
            newPlayer.createPieces(playerSquares[i]) #Each Player gets assigned the Squares for their Pieces at the start
            self.__players.append(newPlayer)

    def setup(self):
        self.createSquares()
        self.createPlayers()
        self.__board.mainloop()

chess= Board()
chess.setup()