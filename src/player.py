from typing import Tuple
from entity import Entity
from settings import PLAYER_MAXIMUM_MUNITIONS


class Player(Entity):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: Tuple[int, int, int],
        speed: int,
    ) -> None:
        super().__init__(left=x, top=y, width=width, height=height, color=color)
        self.speed = speed
        self.munitions = PLAYER_MAXIMUM_MUNITIONS

    def move_left(self) -> None:
        self.rect.move_ip(-self.speed, 0)

    def move_right(self) -> None:
        self.rect.move_ip(self.speed, 0)
