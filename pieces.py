import pygame
pygame.init()

#FACTORY METHOD 
class Piece:
    """
    A class representing a Tetris piece with different orientations (sides).
    """
    def __init__(self, sides):
        self.x = 0
        self.y = 0
        self.sides = sides

    @classmethod
    def create_piece(cls, *sides):
        return cls(generate_sides(*sides))

def generate_sides(*sides):
    """
    A function to generate sides for pieces by converting input tuples into lists.
    """
    return [list(side) for side in sides]


# Create the I piece
piece_I = Piece.create_piece(
     [
      [0,1,0,0],
      [0,1,0,0],
      [0,1,0,0],
      [0,1,0,0]
  ],
  [
      [0,0,0,0],
      [1,1,1,1],
      [0,0,0,0],
      [0,0,0,0]
  ],
  [
      [0,0,1,0],
      [0,0,1,0],
      [0,0,1,0],
      [0,0,1,0]
  ],
[
      [0,0,0,0],
      [0,0,0,0],
      [1,1,1,1],
      [0,0,0,0]
  ],
[
      [0,1,0,0],
      [0,1,0,0],
      [0,1,0,0],
      [0,1,0,0]
  ]

)

# Create the O piece
piece_O = Piece.create_piece(
     [
      [1,1],
      [1,1]
  ],
  [
      [1,1],
      [1,1]
  ],
  [
      [1,1],
      [1,1]
  ],
  [
      [1,1],
      [1,1]
  ],
  [
      [1,1],
      [1,1]
  ]
)

# Create the L piece
piece_L = Piece.create_piece(
     [
      [0,1,1],
      [0,0,1],
      [0,0,1]
  ],
  [
      [0,0,0],
      [0,0,1],
      [1,1,1]
  ],
  [
      [1,0,0],
      [1,0,0],
      [1,1,0]
  ],
  [
      [1,1,1],
      [1,0,0],
      [0,0,0]
  ],
  [
      [0,1,1],
      [0,0,1],
      [0,0,1]
  ]

)

# Create the J piece
piece_J = Piece.create_piece(
     [
       [0,0,1],
       [0,0,1],
       [0,1,1]
   ],
   [
       [0,0,0],
       [1,0,0],
       [1,1,1]
   ],
   [
       [1,1,0],
       [1,0,0],
       [1,0,0]
   ],
   [
       [1,1,1],
       [0,0,1],
       [0,0,0]
   ],
   [
       [0,0,1],
       [0,0,1],
       [0,1,1]
   ]

)

# Create the T piece
piece_T = Piece.create_piece(
    [
      [0,0,0],
      [0,1,0],
      [1,1,1]
  ],
  [
      [0,1,0],
      [0,1,1],
      [0,1,0]
  ],
  [
      [0,0,0],
      [1,1,1],
      [0,1,0]
  ],
  [
      [0,1,0],
      [1,1,0],
      [0,1,0]
  ],
  [
      [0,0,0],
      [0,1,0],
      [1,1,1]
  ]
)

# Create the Z piece
piece_Z = Piece.create_piece(
     [
      [0,1,0],
      [1,1,0],
      [1,0,0]
  ],
  [
      [0,0,0],
      [1,1,0],
      [0,1,1]
  ],
  [
      [0,1,0],
      [1,1,0],
      [1,0,0]
  ],
  [
      [0,0,0],
      [1,1,0],
      [0,1,1]
  ],
  [
      [0,1,0],
      [1,1,0],
      [1,0,0]
  ]
)

# Create the S piece
piece_S = Piece.create_piece(
    [
      [1,0,0],
      [1,1,0],
      [0,1,0]
  ],
  [
      [0,0,0],
      [0,1,1],
      [1,1,0]
  ],
  [
      [1,0,0],
      [1,1,0],
      [0,1,0]
  ],
  [
      [0,0,0],
      [0,1,1],
      [1,1,0]
  ],
  [
      [1,0,0],
      [1,1,0],
      [0,1,0]
  ]
)
