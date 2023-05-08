import pygame
from abc import ABC, abstractmethod

class Component(ABC):
    """
    Component is an abstract class that represents the basic structure of a drawable object.
    """

    @abstractmethod
    def draw(self, color, rect):
        """
        Abstract method to be implemented by child classes.
        """
        pass

class BasicPiece(Component):
    """
    BasicPiece is a concrete class that represents a simple drawable object.
    """

    def draw(self, gameDisplay, color, rect):
        """
        Draws the basic piece with the given color and dimensions.
        
        Returns: the color and piece on display
        """
        pygame.draw.rect(gameDisplay, color, rect)

class PieceDecorator(Component):
    """
    PieceDecorator is an abstract class that serves as a base for concrete decorator classes.
    """

    def __init__(self, component: Component):
        """
        Initializes a new PieceDecorator with the given component.
        """
        self._component = component

    def draw(self, gameDisplay, color, rect):
        """
        Draws the decorated component with the given color and dimensions.
        Returns: the color and piece on display
        """
        self._component.draw(gameDisplay, color, rect)

class ColorChangerDecorator(PieceDecorator):
    """
    ColorChangerDecorator is a concrete decorator class that changes the color of a given drawable object.
    """

    def __init__(self, component: Component, new_color):
        """
        Initializes a new ColorChangerDecorator with the given component and new color.
       
        """
        super().__init__(component)
        self._new_color = new_color

    def draw(self, gameDisplay, color, rect):
        """
        Draws the decorated component with the new color and given dimensions.
        Returns: the color and piece on display
        """
        self._component.draw(gameDisplay, self._new_color, rect)
