import random
import time
import pygame

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
grey = (46, 49, 49, 1)

size = width, height = 900, 900

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((size))
screen.fill(white)
pygame.display.update()
fps = 60
clock = pygame.time.Clock()

cell_width = 40
x = 0
y = 0

grid = []
stack_list = []
closed_list = []

path = {}


def build_grid(x, y, cell_width=cell_width):
    for n in range(20):
        x = 40
        y = y + 40
        for m in range(20):
            pygame.draw.line(screen, black, [x + cell_width, y], [x + cell_width, y + cell_width], 2)  # East wall
            pygame.draw.line(screen, black, [x, y], [x, y + cell_width], 2)  # West wall
            pygame.draw.line(screen, black, [x, y], [x + cell_width, y], 2)  # North wall
            pygame.draw.line(screen, black, [x, y + cell_width], [x + cell_width, y + cell_width], 2)  # South wall

            grid.append((x, y))
            x = x + 40
            pygame.display.update()


def Knockdown_East_Wall(x, y):
    pygame.draw.rect(screen, yellow, (x + 1, y + 1, 79, 39), 0)
    pygame.display.update()


def Knockdown_West_Wall(x, y):
    pygame.draw.rect(screen, yellow, (x - cell_width + 1, y + 1, 79, 39), 0)
    pygame.display.update()


def Knockdown_North_Wall(x, y):
    pygame.draw.rect(screen, yellow, (x + 1, y - cell_width + 1, 39, 79), 0)
    pygame.display.update()


def Knockdown_South_Wall(x, y):
    pygame.draw.rect(screen, yellow, (x + 1, y + 1, 39, 79), 0)
    pygame.display.update()


def Single_Cell(x, y):
    pygame.draw.rect(screen, yellow, (x + 1, y + 1, 38, 38), 0)
    pygame.display.update()


def backtracking_cell(x, y):
    pygame.draw.rect(screen, yellow, (x + 1, y + 1, 38, 38), 0)
    pygame.display.update()


def Path_tracker(x, y):
    pygame.draw.rect(screen, green, (x + 15, y + 15, 10, 10), 0)
    pygame.display.update()


def Maze(x, y):
    Single_Cell(x, y)
    stack_list.append((x, y))
    closed_list.append((x, y))

    while len(stack_list) > 0:
        time.sleep(0.007)
        cell = []

        if (x + cell_width, y) not in closed_list and (x + cell_width, y) in grid:
            cell.append("East")

        if (x - cell_width, y) not in closed_list and (x - cell_width, y) in grid:
            cell.append("West")

        if (x, y + cell_width) not in closed_list and (x, y + cell_width) in grid:
            cell.append("South")

        if (x, y - cell_width) not in closed_list and (x, y - cell_width) in grid:
            cell.append("North")

        if len(cell) > 0:
            current_cell = (random.choice(cell))

            if current_cell == "East":
                Knockdown_East_Wall(x, y)
                path[(x + cell_width, y)] = x, y
                x = x + cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "West":
                Knockdown_West_Wall(x, y)
                path[(x - cell_width, y)] = x, y
                x = x - cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "North":
                Knockdown_North_Wall(x, y)
                path[(x, y - cell_width)] = x, y
                y = y - cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "South":
                Knockdown_South_Wall(x, y)
                path[(x, y + cell_width)] = x, y
                y = y + cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

        else:
            x, y = stack_list.pop()
            Single_Cell(x, y)
            time.sleep(0.05)
            backtracking_cell(x, y)


def path_tracer(x, y):
    Path_tracker(x, y)
    while (x, y) != (40, 40):
        x, y = path[x, y]
        Path_tracker(x, y)
        time.sleep(0.1)


x, y = 40, 40
build_grid(40, 0, 40)
Maze(x, y)
path_tracer(800, 800)

RUN = True
print(grid)
while RUN:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

