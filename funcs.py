import pygame, colors, random, pieces, variables

sum_score = 0
y_to_insert = 0
x_to_insert = 5


def get_piece():
    """
    Randomly selects and returns a Tetris piece with its current shape, name, and shape number.

    Returns:
        list: A list containing the current piece's side, name, and shape number.
    """
    list_of_pieces = [pieces.piece_I, pieces.piece_T, pieces.piece_O, pieces.piece_J, pieces.piece_L, pieces.piece_S, pieces.piece_Z]
    piece_name = list_of_pieces[random.randrange(len(list_of_pieces))]
    shape = random.randint(0, 3)
    current_piece_name = piece_name
    current_piece_shape_number = shape
    return [piece_name.sides[shape], current_piece_name, current_piece_shape_number]


def insert_piece(piece, game_matrix):
    """
    Inserts the given Tetris piece into the game matrix at the initial position.

    Args:
        piece (list): A 2D list representing the current Tetris piece.
        game_matrix (list): A 2D list representing the game matrix.
    """
    global y_to_insert
    global x_to_insert
    y_to_insert = 0
    x_to_insert = 5
    for piece_row_index in range(len(piece)):
        for piece_col_index in range(len(piece[0])):
            game_matrix[y_to_insert + piece_row_index][x_to_insert + piece_col_index] = piece[piece_row_index][piece_col_index]


def move_down(game_matrix,delay):
    """
    Moves the current Tetris piece down in the game matrix if there is space available.

    Args:
        game_matrix (list): A 2D list representing the game matrix.
        current_piece (list): A 2D list representing the current Tetris piece.
        delay (int): The time delay in milliseconds between each downward movement.
    """
    pygame.time.delay(delay)
    there_is_space = True
    for row in range(len(game_matrix)-2, -1, -1):
        for col in range(len(game_matrix[0])):  # read the matrix
            if game_matrix[row][col] == 1:  # get index of the 1s
                if game_matrix[row + 1][col] == 2 or game_matrix[row + 1][col] == 7:  # if below the 1 there is a 2 or a 7...
                    there_is_space = False
                    
    if there_is_space == True:
        for row in range(len(game_matrix)-2, -1, -1):
            for col in range(len(game_matrix[0])):
                if game_matrix[row][col] == 1:
                    game_matrix[row + 1][col] = 1
                    game_matrix[row][col] = 0
        global y_to_insert
        y_to_insert += 1

    if there_is_space == False:
        for row in range(len(game_matrix)-2, -1, -1):
            for col in range(len(game_matrix[0])):
                if game_matrix[row][col] == 1:
                    game_matrix[row][col] = 2


def detect_if_piece_in_play(game_matrix):
    """
    Checks if there is a Tetris piece currently in play within the game matrix.

    Args:
        game_matrix (list): A 2D list representing the game matrix.

    Returns:
        bool: True if a piece is in play, False otherwise.
    """
    piece_in_play = False
    for row in range(len(game_matrix)):
        for col in range(len(game_matrix[0])):
            if game_matrix[row][col] == 1:
                piece_in_play = True
    return piece_in_play

def line_isfull_check(game_matrix):
    """
    Checks for full lines in the game matrix, clears them, and updates the matrix accordingly.

    Args:
        game_matrix (list): A 2D list representing the game matrix.
    """
    lines_cleared = 0
    lines_cleared = game_matrix.count([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])  # count how many lines were filled in one move
    for i in range(len(game_matrix)):
        if game_matrix[i] == [7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7]:
            game_matrix.pop(i)
            game_matrix.insert(0, [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7])


def display_update(gameDisplay, width, game_matrix, square_size, x_to_center):
    """
    Updates the game display based on the current state of the game matrix.

    Args:
        gameDisplay (pygame.Surface): The main display surface.
        width (int): The width of the game display.
        game_matrix (list): A 2D list representing the game matrix.
        square_size (int): The size of each square in the game matrix.
        x_to_center (int): The distance from the left edge of the game display to center the game matrix.
    """
    for row_index in range(len(game_matrix)):
        for col_index in range(1, len(game_matrix[0]) - 1):
            if game_matrix[row_index][col_index] == 0:
                pygame.draw.rect(gameDisplay, colors.WHITE, [(col_index - 1) * square_size + (x_to_center), (row_index * square_size) - 100, square_size, square_size])
            if game_matrix[row_index][col_index] == 1:
                pygame.draw.rect(gameDisplay, colors.ORANGE, [(col_index - 1) * square_size + (x_to_center), (row_index * square_size) - 100, square_size, square_size])
                pygame.draw.rect(gameDisplay, colors.DARKER_ORANGE, [(col_index - 1) * square_size + (x_to_center), (row_index * square_size) - 100, square_size, square_size], 1)
            if game_matrix[row_index][col_index] == 2:
                pygame.draw.rect(gameDisplay, colors.DARK_BLUE, [(col_index - 1) * square_size + (x_to_center), (row_index * square_size) - 100, square_size, square_size])
                pygame.draw.rect(gameDisplay, colors.DARKER_BLUE, [(col_index - 1) * square_size + (x_to_center), (row_index * square_size) - 100, square_size, square_size], 1)

def delete_line(game_matrix):
    """
    Removes full lines from the game matrix and adds a new empty line at the top.

    Args:
        game_matrix (list): A 2D list representing the game matrix.
    """
    for i in range(len(game_matrix)):
        if game_matrix[i] == [7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7]:
            game_matrix.pop(i)
            game_matrix.insert(0, [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7])


def move_left(game_matrix):
    """
    Moves the active piece one position to the left in the game matrix if possible.

    Args:
        game_matrix (list): A 2D list representing the game matrix.
    """
    there_is_space = True
    for row in range(len(game_matrix)-2,-1,-1):
        for col in range(len(game_matrix[0])):
            if game_matrix[row][col] == 1:
                if game_matrix[row][col-1] == 2 or game_matrix[row][col-1] == 7:
                    there_is_space = False
    if there_is_space == True:
        for row in range(len(game_matrix)-2,-1,-1):
            for col in range(len(game_matrix[0])):
                if game_matrix[row][col] == 1:
                    game_matrix[row][col-1] = 1
                    game_matrix[row][col] = 0
        global x_to_insert
        x_to_insert -= 1

def move_right(game_matrix):
    """
    Moves the active piece one position to the right in the game matrix if possible.

    Args:
        game_matrix (list): A 2D list representing the game matrix.
    """
    there_is_space = True
    for row in range(len(game_matrix)-2,-1,-1):
        for col in range(len(game_matrix[0])-1, 0, -1):
            if game_matrix[row][col] == 1:
                if game_matrix[row][col+1] == 2 or game_matrix[row][col+1] == 7:
                    there_is_space = False
    if there_is_space == True:
        for row in range(len(game_matrix)-2,-1,-1):
            for col in range(len(game_matrix[0])-2, 0, -1):
                if game_matrix[row][col] == 1:
                    game_matrix[row][col+1] = 1
                    game_matrix[row][col] = 0
        global x_to_insert
        x_to_insert += 1

def rotate_piece(game_matrix, current_piece_matrix, current_piece_rotation, current_piece_name, next_piece_matrix, all_info_of_current_piece, current_piece):
    """
    Rotates the active piece in the game matrix if possible.

    Args:
        game_matrix (list): A 2D list representing the game matrix.
        current_piece_matrix (list): A 2D list representing the current piece's matrix.
        current_piece_rotation (int): The current rotation state of the piece.
        current_piece_name (obj): The current piece's object.
        next_piece_matrix (list): A 2D list representing the next rotation state of the piece.
        all_info_of_current_piece (list): List containing current_piece_matrix, current_piece_name, and current_piece_rotation.
        current_piece (obj): The current piece.
    """
    global y_to_insert
    global x_to_insert
    there_is_space = True
    next_piece_indexes = []
    for piece_row_index in range(len(next_piece_matrix)):
        for piece_col_index in range(len(next_piece_matrix[0])):
            if next_piece_matrix[piece_row_index][piece_col_index] == 1:
                coords_to_append = [piece_row_index,piece_col_index]
                next_piece_indexes.append(coords_to_append)
    for piece_row_index in range(len(current_piece_matrix)):
        for coords in next_piece_indexes:
            if game_matrix[y_to_insert+coords[0]][x_to_insert+coords[1]] == 2 or game_matrix[y_to_insert+coords[0]][x_to_insert+coords[1]] == 7:
                there_is_space = False
                break
    if there_is_space == True:
        for piece_row_index in range(len(next_piece_matrix)):
            for piece_col_index in range(len(next_piece_matrix[0])):
                game_matrix[y_to_insert + piece_row_index][x_to_insert + piece_col_index] = next_piece_matrix[piece_row_index][piece_col_index]
        current_piece = next_piece_matrix
        if all_info_of_current_piece[2] == 3:
            all_info_of_current_piece[2] = 0
        else:
            all_info_of_current_piece[2] += 1

def game_over(game_matrix, running):
    """
    Determines if the game is over by checking if any fixed pieces are in row 4.

    Args:
        game_matrix (list): A 2D list representing the game matrix.
        running (bool): A boolean representing the current state of the game loop.

    Returns:
        bool: Returns False if the game is over, otherwise the function returns None implicitly.
    """
    for i in game_matrix[4]:
             if i == 2:
                 return False


def score_counter(game_matrix):
    """
    Calculates the total score by counting the number of filled lines in the game matrix.

    Args:
        game_matrix (list): A 2D list representing the game matrix.

    Returns:
        int: The updated total score.
    """
    global sum_score
    sum_score += game_matrix.count([7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7])*100  # contar cuántas lineas se llenaron en un movimiento
    return sum_score


def update_score(gameDisplay, score, x_to_center):
    """
    Updates the displayed score on the game screen.

    Args:
        gameDisplay (pygame.Surface): The game screen surface.
        score (int): The current score.
        x_to_center (int): The x-coordinate to center the score display.
    """
    pygame.draw.rect(gameDisplay, colors.red, [0,0, x_to_center-1, 100])
    text = variables.font.render("Score: " + str(score), True, colors.BLACK)
    gameDisplay.blit(text, [0,0])

def paused():
    """
    Pauses the game and waits for an event to unpause or quit the game.
    """
    global pause
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            unpause()
        pygame.display.update()

def unpause():
    """
    Unpauses the game by setting the 'pause' variable to False.
    """

    global  pause
    pause = False
