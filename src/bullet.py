import pygame


class Bullet:
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
    ) -> None:
        self.width = width
        self.height = height
        self.position = position
        self.color = color
        self.speed = speed

    def move(self) -> None:
        self.position[0] -= self.speed

    def update(self, screen) -> None:
        pygame.draw.rect(screen, self.color, (*self.position, self.width, self.height))
