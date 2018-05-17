Pente game made for school, feel free to use.

## Pente(object)

Properties:    
    
  <li>• n : Number of intersections. </li>
  <li>•	turn : The current turn.</li>
  <li>•	greenTile : The tile for the green player (1 or 0).</li>
  <li>•	blueTile : The tile for the blue player (1 or 0).</li>
  <li>•	greenPoints : Capture Points Green Player.</li>
  <li>•	bluePoints : Capture Points Blue Player.</li>
  <li>•	x : Array with all the x coordinates for vertical lines (plus a 1000 at the end for various purposes).</li>
  <li>•	y : Array with all the y coordinates for vertical lines (plus a 1000 at the end for various purposes).</li>
  <li>•	width : pygame canvas width.</li>
  <li>•	height : pygame canvas height</li>
  <li>•	boardImage : The board image to use loaded from "Pieces/penteBoard.png"</li>
  <li>•	blue : The blueGlassPiece loaded from "Pieces/blueGlassPiece.png"</li>
  <li>•	green : The blueGlassPiece loaded from "Pieces/greenGlassPiece.png"</li>
  <li>•	screen : pygame screen (loaded with "pygame.display.set_mode((self.width, self.height))").</li>
  <li>•	background_colour : Color to use (R:224, G:195, B:112).</li>
  <li>•	board : Matrix that saves the state of the board.</li>
  
  Board Example:
  
          [['1', '0', '1', '0', '1', '1', '0', '1', '0', '1'], \
          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
          ['0', '.', '1', '.', '.', '0', '.', '1', '.', '.'], \
          ['.', '.', '.', '.', '1', '.', '.', '.', '.', '1'], \
          ['.', '.', '1', '0', '.', '.', '.', '1', '0', '.'], \
          ['1', '0', '1', '0', '1', '1', '0', '1', '0', '1'], \
          ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], \
          ['0', '.', '1', '.', '.', '0', '.', '1', '.', '.'], \
          ['.', '.', '.', '.', '1', '.', '.', '.', '.', '1'], \
          ['.', '.', '1', '0', '.', '.', '.', '1', '0', '.']]
       
  Draw a the board in pygame screen, should be call in a loop.
    <li>def makeBoard(self):</li>

  Returns empty board.
    <li>def getNewBoard(self):</li>

  Validates a move.
    <li>def isValidMove(self, move):</li>

  Check if the move can capture pieces and deletes the captured pieces.
    <li>def isCaptureMove(self, jugador, move):</li>
    
  Saves the move to self.board
    <li>def makeMove(self, jugador, move):</li>
    
  Checks if self.board is full
    <li>def isBoardFull(self):</li>

  Check if a player won.
    <li>def isWinner(self, tile):</li>

  Randomize the start (Return 'blue' or 'green')
    <li>def randomStart(self):</li>

  Function to call when user makes click
    <li> def didClickMouse(self):</li>

  Get Mouse coordinates relative to the board.
    <li>def getCoordinates(self):</li>

## move(object)

Properties:   

  <li>• x : x Coordinate of the move. </li>
  <li>•	y : y Coordinate of the move.</li>
  
  Makes the object printable.
    <li>def \_\_str__(self):</li>


