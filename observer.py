
import variables, funcs
from abc import ABC, abstractmethod

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