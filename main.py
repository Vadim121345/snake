import pygame
import random
import sys


WIDTH, HEIGHT = 600, 400
CELL = 20
COLS, ROWS = WIDTH // CELL, HEIGHT // CELL


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (200, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)


def random_food(snake):
    while True:
        pos = (random.randrange(COLS), random.randrange(ROWS))
        if pos not in snake:
            return pos


def draw_cell(pos, color):
    x, y = pos
    rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)


def game():

    snake = [(5, 10), (4, 10), (3, 10)]
    direction = (1, 0)
    next_direction = direction
    food = random_food(snake)
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 1):
                    next_direction = (0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -1):
                    next_direction = (0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (1, 0):
                    next_direction = (-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-1, 0):
                    next_direction = (1, 0)

        direction = next_direction
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])


        if not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS):
            return score


        if new_head in snake[:-1]:
            return score

        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            food = random_food(snake)
        else:
            snake.pop()


        screen.fill(BLACK)
        draw_cell(food, RED)
        for i, segment in enumerate(snake):
            draw_cell(segment, GREEN if i == 0 else DARK_GREEN)

        text = font.render(f"Счёт: {score}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(10)


def main():
    while True:
        score = game()
        screen.fill(BLACK)
        over = font.render(f"Игра окончена! Счёт: {score}", True, WHITE)
        restart = font.render("Нажми R для рестарта или Q для выхода", True, WHITE)
        screen.blit(over, (WIDTH // 2 - over.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
            clock.tick(15)


if __name__ == "__main__":
    main()
