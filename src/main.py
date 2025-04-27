import pygame
import sys
from player import Player, Directions
from ennemy import Ennemy
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
    ADD_ENNEMY_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENNEMY_EVENT, 5000)
    is_running: bool = True
    clock = pygame.time.Clock()
    player: pygame.Rect = pygame.Rect(
        player_position[0],
        player_position[1],
        PLAYER_WIDTH,
        PLAYER_HEIGHT,
    )
    ennemies: list[pygame.Rect] = []
    bullets: list[pygame.Rect] = []
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("space pressed")
                    bullet: pygame.Rect = pygame.Rect(
                        player.x, player.y + player.width // 2, 5, 5
                    )
                    bullets.append(bullet)
            elif event.type == ADD_ENNEMY_EVENT:
                ennemy: pygame.Rect = pygame.Rect(64, 400, ENNEMY_WIDTH, ENNEMY_HEIGHT)
                pygame.draw.rect(screen, ENNEMY_COLOR, ennemy)
                ennemies.append(ennemy)

        screen.fill((30, 30, 30))

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player.x > 0:
            player.move_ip(-5, 0)
        if key[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - PLAYER_WIDTH:
            player.move_ip(5, 0)

        # move all bullets
        for bullet in bullets:
            bullet.move_ip(-1, 0)
            if bullet.x < 0:
                bullets.remove(bullet)
                print("bullet removed")
        # move all ennemies
        for ennemy in ennemies:
            ennemy.move_ip(1, 0)

        # check collisions between bullets and ennemies
        collied_bullets = []
        collied_ennemies = []

        for ennemy in ennemies:
            for bullet in bullets:
                if ennemy.colliderect(bullet):
                    collied_ennemies.append(ennemy)
                    collied_bullets.append(bullet)
            if ennemy.colliderect(player):
                is_running = False

        # remove bullets
        bullets = [bullet for bullet in bullets if bullet not in collied_bullets]
        # remove ennemies
        ennemies = [ennemy for ennemy in ennemies if ennemy not in collied_ennemies]
        # draw bullets
        for bullet in bullets:
            pygame.draw.rect(screen, (0, 255, 0), bullet)
        # draw ennemies
        for ennemy in ennemies:
            pygame.draw.rect(screen, ENNEMY_COLOR, ennemy)

        pygame.draw.rect(screen, PLAYER_COLOR, player)

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
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("space pressed")
                    bullet: pygame.Rect = pygame.Rect(
                        player_position[0], player_position[1] + player.width // 2, 5, 5
                    )
                bullets.append(bullet)
            elif event.type == ADD_ENNEMY_EVENT:
                ennemy: pygame.Rect = pygame.Rect(64, 400, ENNEMY_WIDTH, ENNEMY_HEIGHT)
                pygame.draw.rect(screen, ENNEMY_COLOR, ennemy)
                ennemies.append(ennemy)

        screen.fill((30, 30, 30))

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and player_position[0] > 0:
            player.move_ip(-5, 0)
        if key[pygame.K_RIGHT] and player_position[0] < SCREEN_WIDTH - PLAYER_WIDTH:
            player.move_ip(5, 0)

        # move all bullets
        for bullet in bullets:
            bullet.move_ip(-1, 0)
            if bullet.x < 0:
                bullets.remove(bullet)
                print("bullet removed")
        # move all ennemies
        for ennemy in ennemies:

            ennemy.move_ip(1, 0)

        # check collisions between bullets and ennemies
        collied_bullets = []
        collied_ennemies = []

        for ennemy in ennemies:
            for bullet in bullets:
                if ennemy.colliderect(bullet):
                    collied_ennemies.append(ennemy)
                    collied_bullets.append(bullet)
            if ennemy.colliderect(player):
                is_running = False

        # remove bullets
        bullets = [bullet for bullet in bullets if bullet not in collied_bullets]
        # remove ennemies
        ennemies = [ennemy for ennemy in ennemies if ennemy not in collied_ennemies]
        # draw bullets
        for bullet in bullets:
            pygame.draw.rect(screen, (0, 255, 0), bullet)
        # draw ennemies
        for ennemy in ennemies:
            pygame.draw.rect(screen, ENNEMY_COLOR, ennemy)

        pygame.draw.rect(screen, PLAYER_COLOR, player)

        clock.tick(FPS)
        pygame.display.update()
        """

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
