from typing import Tuple
from entity import Entity


class Enemy(Entity):

    def __init__(
        self,
        left: float,
        top: float,
        width: float,
        height: float,
        color: Tuple[int, int, int],
        speed: int,
    ) -> None:
        super().__init__(left, top, width, height, color)
        self.speed = speed

    def move_right(self) -> None:
        self.rect.move_ip(self.speed, 0)
