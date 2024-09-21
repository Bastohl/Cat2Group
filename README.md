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

Step 1
- The player clicks a button to choose what to move. This pressing of the button calls a function.
- This function that is called aquires:
- a) the square's coordinate
- b) the type of piece on it
- c) the current positions of all the pieces on the board

Step 2
- The data aquired in step 1 is passed as parameters (coordinate, piece positions on the board) 
  to a method in the Class (in Moves.py) that contains the logic for the type of piece (e.g Pawn class, King class e.t.c)

Step 3
- The computer uses logic (that we will provide *biggest task*) to determine all the boxes that the player could move to on the board.
- This step will NOT check whether there is a piece on the squares or not
- For example you have a Queen at the bottom-right (d4).
- The computer will loop through the current positions of the pieces on the board.
- It will pick out the points that fulfil the logic it is using; IN ORDER OF HOW THEY WERE CREATED.
- This means that it will return data in this order top-left (a1), top-right (a4), b2, b4, c3, c4 (right above it), d1, d2, d3 (right on the left)
- This data will be used in step 4 

Step 4
- The computer will use more logic to create 'paths' from the identified squares
- This is what i mean:
- In step 3 we got data organized in order of how the squares were created
- In this step, we take that data and form seperate 'paths' that the piece could take.
- An example path for the Queen in d4 in step 3 would be -> [c3,b2,a1] (diagonal) or [c4,b4,a4] (upward)
- This would allow us to accomplish the last 2 steps

Step 5
- 

