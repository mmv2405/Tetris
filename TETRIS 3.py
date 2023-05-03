import pygame, variables, funcs
from abc import ABC, abstractmethod

pygame.init()
running = True
game_matrix = variables.game_matrix

class Observer(ABC):
    """
    Clase abstracta para observadores que siguen el patrón Observer.
    """
    @abstractmethod
    def update(self):
        """
        Método abstracto para actualizar el estado del observador.
        """
        pass

class ScoreObserver(Observer):
    """
    Clase concreta de observador que actualiza la puntuación en pantalla.
    """

    def update(self, score):
        """
        Actualiza la puntuación en pantalla.

        Args:
            score (int): La puntuación actual del juego.
        """
        funcs.update_score(variables.gameDisplay, score, variables.x_to_center)

class GameState:
    """
    Clase que define el estado actual del juego y gestiona los observadores.
    """
    _instance = None

    @staticmethod
    def get_instance():
        if GameState._instance is None:
            GameState._instance = GameState()
        return GameState._instance

    def __init__(self):
        if GameState._instance is not None:
            raise Exception("Esta clase es un Singleton, usa 'get_instance()' para obtener su instancia.")
        self.score = 0
        self.observers = []

    def add_observer(self, observer):
        """
        Agrega un observador a la lista de observadores.

        Args:
            observer (Observer): El observador que se va a agregar.
        """
        self.observers.append(observer)

    def remove_observer(self, observer):
        """
        Elimina un observador de la lista de observadores.

        Args:
            observer (Observer): El observador que se va a eliminar.
        """
        self.observers.remove(observer)

    def notify_observers(self):
        """
        Notifica a todos los observadores con la puntuación actual.
        """
        for observer in self.observers:
            observer.update(self.score)

class PieceFactory:
    """
    Clase que define la posición y orientación actuales de una pieza de Tetris.
    """

    @staticmethod
    def create_piece():
        """
        Crea una nueva pieza de Tetris.

        Returns:
            all_info_of_current_piece: Información de la pieza actual.
        """
        all_info_of_current_piece = funcs.get_piece()
        return all_info_of_current_piece

game_state = GameState.get_instance()
score_observer = ScoreObserver()
game_state.add_observer(score_observer)

while running:
    # Detectar si hay pieza en juego
    if funcs.detect_if_piece_in_play(game_matrix) == False:
        all_info_of_current_piece = funcs.get_piece()
        current_piece = all_info_of_current_piece[0]
        funcs.insert_piece(current_piece, game_matrix)

    # Mover la pieza actual hacia abajo
    funcs.move_down(game_matrix, variables.delay)

    # Actualiza el puntaje en el singleton
    game_state.score = funcs.score_counter(game_matrix)
    game_state.notify_observers()

    # Detectar si hay lineas llenas y borrarlas
    funcs.line_isfull_check(game_matrix)

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
        funcs.move_left(game_matrix)

    # Detectar evento de tecla derecha
    if keys[pygame.K_RIGHT]:
        funcs.move_right(game_matrix)
        funcs.display_update(variables.gameDisplay, variables.width, game_matrix, variables.square_size, variables.x_to_center)

    # Detectar evento de tecla arriba
    if keys[pygame.K_UP]:
        funcs.rotate_piece(game_matrix, current_piece, all_info_of_current_piece[2], all_info_of_current_piece[1], all_info_of_current_piece[1].sides[all_info_of_current_piece[2]+1], all_info_of_current_piece, current_piece)

    # Detectar evento de tecla abajo
    if keys[pygame.K_DOWN]:
        funcs.move_down(game_matrix, variables.delay)
        funcs.display_update(variables.gameDisplay, variables.width, game_matrix, variables.square_size, variables.x_to_center)

    # Detectar evento de tecla espacio
    if keys[pygame.K_SPACE]:
        go_down = True
        while go_down == True:
            funcs.move_down(game_matrix, variables.delay)
            if funcs.detect_if_piece_in_play(game_matrix) == False:
                funcs.display_update(variables.gameDisplay, variables.width, game_matrix, variables.square_size, variables.x_to_center)
                go_down = False

    # Detectar evento de tecla P
    if keys[pygame.K_p]:
        pause = True
        funcs.paused()

    funcs.display_update(variables.gameDisplay ,variables.width ,game_matrix, variables.square_size, variables.x_to_center)
    pygame.display.flip()

    if funcs.game_over(game_matrix, running) == False:
        running = False

pygame.quit()
