import enum

import pygame


class Directions(enum.Enum):
    LEFT = "left"
    RIGHT = "right"


class Player:
    width: int
    height: int
    position: list[int]
    color: tuple[int, int, int]
    speed: int

    def __init__(
        self,
        width: int,
        height: int,
        position: list[int],
        color: tuple[int, int, int],
        speed: int,
    ):
        self.width = width
        self.height = height
        self.position = position
        self.color = color
        self.speed = speed

    def move(self, direction: Directions) -> None:
        match direction:
            case Directions.LEFT:
                self.position[0] -= self.speed
            case Directions.RIGHT:
                self.position[0] += self.speed

    def update(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (*self.position, self.width, self.height),
        )
