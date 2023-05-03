import pygame,variables,funcs

pygame.init()
running = True
game_matrix = variables.game_matrix

class PieceFactory:
    """
    A class that defines the current position and orientation of a Tetris piece.
    """
    @staticmethod
    def create_piece():
        all_info_of_current_piece = funcs.get_piece()
        return all_info_of_current_piece


while running:
    #detectar si hay pieza en juego
    if funcs.detect_if_piece_in_play(game_matrix) == False:
        all_info_of_current_piece = funcs.get_piece()
        current_piece = all_info_of_current_piece[0]
        funcs.insert_piece(current_piece, game_matrix)

    #mover la pieza actual hacia abajo
    funcs.move_down(game_matrix, variables.delay)

    funcs.update_score(variables.gameDisplay, funcs.score_counter(game_matrix), variables.x_to_center)

    #detectar si hay lineas llenas y borrarlas
    funcs.line_isfull_check(game_matrix)

    #detectar evento de cerrar ventana
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

    keys = pygame.key.get_pressed()

    #detectar evento de tecla Q
    if keys[pygame.K_q]:
        running = False

    #detectar evento de tecla izquierda
    if keys[pygame.K_LEFT]:
        funcs.move_left(game_matrix)
        funcs.display_update(variables.gameDisplay ,variables.width ,game_matrix, variables.square_size, variables.x_to_center)

    #detectar evento de tecla derecha
    if keys[pygame.K_RIGHT]:
        funcs.move_right(game_matrix)
        funcs.display_update(variables.gameDisplay ,variables.width ,game_matrix, variables.square_size, variables.x_to_center)

    #detectar evento de tecla arriba
    if keys[pygame.K_UP]:
        funcs.rotate_piece(game_matrix, current_piece, all_info_of_current_piece[2], all_info_of_current_piece[1], all_info_of_current_piece[1].sides[all_info_of_current_piece[2]+1], all_info_of_current_piece, current_piece)

    #detectar evento de tecla abajo
    if keys[pygame.K_DOWN]:
        funcs.move_down(game_matrix,variables.delay)
        funcs.display_update(variables.gameDisplay ,variables.width ,game_matrix, variables.square_size,variables.x_to_center)

    #detectar evento de tecla espacio
    if keys[pygame.K_SPACE]:
        go_down = True
        while go_down == True:
            funcs.move_down(game_matrix,variables.delay)
            if funcs.detect_if_piece_in_play(game_matrix) == False:
                funcs.display_update(variables.gameDisplay ,variables.width ,game_matrix, variables.square_size, variables.x_to_center)
                go_down = False

    #detectar evento de tecla P
    if keys[pygame.K_p]:
        pause = True
        funcs.paused()

    funcs.display_update(variables.gameDisplay ,variables.width ,game_matrix, variables.square_size, variables.x_to_center)
    pygame.display.flip()

    if funcs.game_over(game_matrix, running) == False:
        running = False

pygame.quit()
