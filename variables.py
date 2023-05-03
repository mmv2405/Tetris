import pygame, random, funcs, colors, pieces

# Initialize the clock object to control the game speed
clock = pygame.time.Clock()

# Control the game speed using the clock object
clock.tick

# Set the width and height of the game window
width = 500
height = 601

# Define the size of the squares that make up the Tetris pieces
square_size = 25

# Calculate the horizontal position to center the game area within the window
x_to_center = (width - 10*(square_size)) // 2

# Create the game window with the specified dimensions
gameDisplay = pygame.display.set_mode((width,height))

# Set the title of the game window
pygame.display.set_caption("Tetris")

# Fill the game window with the color red
gameDisplay.fill(colors.red)

# Draw the border of the game area on the screen
pygame.draw.rect(gameDisplay, colors.BLACK, [x_to_center-1,0,(square_size*10)+2,(square_size*20)+1], 1)

# Initialize the player's score variable
score = 0

# Initialize a variable to store the current piece in play
current_piece = False


# Set the delay time (in milliseconds) to control the falling speed of the pieces
delay = 200

#Font for the Game
font = pygame.font.SysFont("arial", 30)


#Matrix for the Game boundries
game_matrix = [
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,0,0,0,0,0,0,7],
  [7,0,0,0,0,2,0,0,0,0,0,7],
  [7,0,2,2,2,2,2,2,2,2,2,7],
  [7,0,2,2,2,2,2,2,2,2,2,7],
  [7,7,7,7,7,7,7,7,7,7,7,7]
]


