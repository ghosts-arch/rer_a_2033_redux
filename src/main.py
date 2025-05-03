import pygame
import sys
from player import Player

from enemy import Enemy
from bullet import Bullet

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


def game(screen) -> bool:
    font = pygame.font.Font(None, 32)

    ADD_ENNEMY_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENNEMY_EVENT, 5000)
    is_running: bool = True
    clock = pygame.time.Clock()
    player: Player = Player(
        x=player_position[0],
        y=player_position[1],
        width=PLAYER_WIDTH,
        height=PLAYER_HEIGHT,
        color=PLAYER_COLOR,
        speed=PLAYER_SPEED,
    )

    ennemies: list[Enemy] = []
    bullets: list[Bullet] = []
    munitions_text = f"{player.munitions}/20"
    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("space pressed")
                    if player.munitions > 0:
                        bullet: Bullet = Bullet(
                            player.rect.x,
                            player.rect.y + player.rect.width // 2,
                            5,
                            5,
                            (0, 255, 0),
                        )
                        bullets.append(bullet)
                        player.munitions = player.munitions - 1
                        munitions_text = f"{player.munitions}/20"
                        print(f"munitions: {player.munitions}")
                elif event.key == pygame.K_r:
                    player.munitions = 20
                    munitions_text = f"{player.munitions}/20"
            elif event.type == ADD_ENNEMY_EVENT:
                ennemy: Enemy = Enemy(
                    left=ennemy_position[0],
                    top=ennemy_position[1],
                    width=ENNEMY_WIDTH,
                    height=ENNEMY_HEIGHT,
                    color=ENNEMY_COLOR,
                    speed=ENNEMY_SPEED,
                )
                ennemies.append(ennemy)

        screen.fill((30, 30, 30))
        munitions_text_surface = font.render(munitions_text, True, (255, 255, 255))
        munitions_text_rectangle = munitions_text_surface.get_rect(topleft=(32, 32))

        screen.blit(munitions_text_surface, munitions_text_rectangle)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player.rect.x > 0:
            player.move_left()
        if key[pygame.K_RIGHT] and player.rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
            player.move_right()

        # move all bullets
        for bullet in bullets:
            bullet.move_left()
            if bullet.rect.x < 0:
                bullets.remove(bullet)
                print("bullet removed")
        # move all ennemies
        for ennemy in ennemies:
            ennemy.move_right()

        # check collisions between bullets and ennemies
        collied_bullets = []
        collied_ennemies: list[Enemy] = []

        for ennemy in ennemies:
            for bullet in bullets:
                if ennemy.rect.colliderect(bullet.rect):
                    ennemy.life = ennemy.life - 1
                    collied_bullets.append(bullet)
                    if ennemy.life == 0:
                        collied_ennemies.append(ennemy)
                    print(ennemy.life)
            if ennemy.rect.colliderect(player.rect):
                is_running = False

        # remove bullets
        bullets = [bullet for bullet in bullets if bullet not in collied_bullets]
        # remove ennemies
        ennemies = [ennemy for ennemy in ennemies if ennemy not in collied_ennemies]
        # draw bullets
        for bullet in bullets:
            bullet.update()
        # draw ennemies
        for ennemy in ennemies:
            ennemy.update()

        player.update()

        clock.tick(FPS)
        pygame.display.update()
    return is_running


def main() -> None:
    print("Hello from rer-a-2033-redux!")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RER A 2033 Redux")

    ADD_ENNEMY_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENNEMY_EVENT, 5000)

    clock = pygame.time.Clock()

    is_running: bool = True

    font = pygame.font.Font(None, 36)

    main_title = font.render("RER A 2033 Redux", True, (255, 255, 255))
    main_title_rectangle = main_title.get_rect(center=(400, 150))

    start_text = font.render(
        "Appuyer sur `entrée`pour commencer...", True, (255, 255, 255)
    )
    start_text_rectangle = start_text.get_rect(center=(400, 300))

    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill((100, 100, 100))
        screen.blit(main_title, main_title_rectangle)
        screen.blit(start_text, start_text_rectangle)

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            print("game started...")
            game(screen)
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
