from entity import Entity


class Bullet(Entity):
    def __init__(self, left, top, width, height, color):
        super().__init__(left, top, width, height, color)

        self.speed = 1

    def move_left(self) -> None:
        self.rect.move_ip(-self.speed, 0)
