from typing import Tuple
import pygame
from abc import ABC


class Entity(ABC):
    def __init__(
        self,
        left: float,
        top: float,
        width: float,
        height: float,
        color: Tuple[int, int, int],
    ) -> None:
        self.rect: pygame.Rect = pygame.Rect(left, top, width, height)
        self.color: Tuple[int, int, int] = color

    def update(self) -> None:
        pygame.draw.rect(pygame.display.get_surface(), self.color, self.rect)
