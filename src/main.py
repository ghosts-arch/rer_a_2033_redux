import pygame
import sys
from player import Player, Directions

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
FPS: int = 60

player_position: list[int] = [672, 400]
PLAYER_WIDTH: int = 32
PLAYER_HEIGHT: int = 64
PLAYER_COLOR: tuple[int, int, int] = (0, 0, 255)
PLAYER_SPEED: int = 1

ennemy_position: list[int] = [64, 400]
ENNEMY_WIDTH: int = 32
ENNEMY_HEIGHT: int = 64
ENNEMY_COLOR: tuple[int, int, int] = (255, 0, 0)
ENNEMY_SPEED: int = 1


def main() -> None:
    print("Hello from rer-a-2033-redux!")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RER A 2033 Redux")

    clock = pygame.time.Clock()
    is_running: bool = True
    player: Player = Player(
        PLAYER_WIDTH,
        PLAYER_HEIGHT,
        player_position,
        PLAYER_COLOR,
        PLAYER_SPEED,
    )
    ennemy: Player = Player(
        ENNEMY_WIDTH, ENNEMY_HEIGHT, ennemy_position, ENNEMY_COLOR, ENNEMY_SPEED
    )
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill((30, 30, 30))

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player_position[0] > 0:
            player.move(Directions.LEFT)
        if key[pygame.K_RIGHT] and player_position[0] < SCREEN_WIDTH - PLAYER_WIDTH:
            player.move(Directions.RIGHT)

        ennemy.update(screen=screen)
        player.update(screen=screen)

        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
