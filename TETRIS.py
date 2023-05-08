import pygame, variables, funcs
from observer import GameState,ScoreObserver
from pieces import  create_piece

pygame.init()
running = True

game_state = GameState.get_instance()
score_observer = ScoreObserver()
game_state.add_observer(score_observer)

while running:
    # Detectar si hay pieza en juego
    if funcs.detect_if_piece_in_play(variables.game_matrix) == False:
        all_info_of_current_piece = create_piece()
        current_piece = all_info_of_current_piece[0]
        funcs.insert_piece(current_piece, variables.game_matrix)

    # Mover la pieza actual hacia abajo
    funcs.move_down(variables.game_matrix, variables.delay)

    # Actualiza el puntaje en el singleton
    game_state.score = funcs.score_counter(variables.game_matrix)
    game_state.notify_observers()

    # Detectar si hay lineas llenas y borrarlas
    funcs.line_isfull_check(variables.game_matrix)

    # Detectar evento de cerrar ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Detectar evento de tecla Q
    if keys[pygame.K_q]:
        running = False

    # Detectar evento de tecla izquierda
    if keys[pygame.K_LEFT]:
        funcs.move_left(variables.game_matrix)

    # Detectar evento de tecla derecha
    if keys[pygame.K_RIGHT]:
        funcs.move_right(variables.game_matrix)
        funcs.display_update(variables.gameDisplay, variables.width, variables.game_matrix, variables.square_size, variables.x_to_center)
    # Detectar evento de tecla arriba
    if keys[pygame.K_UP]:
        funcs.rotate_piece(variables.game_matrix, current_piece, all_info_of_current_piece[2], all_info_of_current_piece[1], all_info_of_current_piece[1].sides[all_info_of_current_piece[2]+1], all_info_of_current_piece, current_piece)

    # Detectar evento de tecla abajo
    if keys[pygame.K_DOWN]:
        funcs.move_down(variables.game_matrix, variables.delay)
        funcs.display_update(variables.gameDisplay, variables.width, variables.game_matrix, variables.square_size, variables.x_to_center)

    # Detectar evento de tecla espacio
    if keys[pygame.K_SPACE]:
        go_down = True
        while go_down == True:
            funcs.move_down(variables.game_matrix, variables.delay)
            if funcs.detect_if_piece_in_play(variables.game_matrix) == False:
                funcs.display_update(variables.gameDisplay, variables.width, variables.game_matrix, variables.square_size, variables.x_to_center)
                go_down = False

    # Detectar evento de tecla P
    if keys[pygame.K_p]:
        pause = True
        funcs.paused()

    funcs.display_update(variables.gameDisplay ,variables.width ,variables.game_matrix, variables.square_size, variables.x_to_center)
    pygame.display.flip()

    if funcs.game_over(variables.game_matrix, running) == False:
        running = False

pygame.quit()
