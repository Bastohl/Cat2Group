MY SUGGESTION OF HOW WE SHOULD DO THIS PROJECT:

Section 1
Create Classes
1. Board Class
   - Creates Squares using the 'Square' class. It assigns:
   - a) position on UI screen,
   - b) coordinate (e.g. a1, b3 e.t.c),
   - c) color
   - Creates Players using the 'Player' class. It assigns the player's number. The number determines:
   - a) color (e.g. 1->Black, 2->White),
   - b) organization of pieces (e.g. castle, queen, king, castle, pawn, pawn, pawn, pawn ... if player is at the top of the board and vice versa if at the bottom)
     
2. Player Class
   - Creates Pieces using the 'Piece' class. It assigns each piece:
   - a) its type (e.g. Pawn, Queen)
   - b) its starting Square
   - c) its color based on the player
     
3. Square Class
   - It is a class having:
   - a) a coordinate (for identification),
   - b) a position (for placement on the UI screen),
   - c) a color (chosen to make checkered pattern)
   - d) a graphic (linked to the piece on it)
   - It creates a button (at its assigned position) using Tkinter to display the piece on it
  
4. Piece Class
   - It is a class that has:
   - a) type of piece (to specify movment logic and to assign it an image)
   - b) its current square (for display on the screen, and for movment logic)
   - c) its color, based on its player

Section 3
Game Logic
Step 1:
- The player clicks a button to choose what to move. This pressing of the button calls a function.
- This function that is called aquires:
- a) the square's coordinate
- b) the type of piece on it
- c) the current positions of all the pieces on the board

Step 2:
-The data aquired in step 1 is passed as parameters (coordinate, piece positions on the board) 
 to a method in the Class (in Moves.py) that contains the logic for the type of piece (e.g Pawn class, King class e.t.c)

Step 3:
-The computer uses logic (that we will provide *biggest task*) to determine all the boxes that the player could move to on the board.

