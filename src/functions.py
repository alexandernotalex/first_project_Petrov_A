from src import Globals
import pygame
import pygame.font
import pygame_menu
import random
import time


globals = Globals.Globals()


class Game:
    # initialising pygame
    pygame.font.init()
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snake_game')
    
    def __init__(self):
        self.game_window = pygame.display.set_mode((globals.window_x, globals.window_y))
        self.new_table = pygame.display.set_mode((globals.window_x, globals.window_y))
        self.font_table = pygame.font.SysFont('Arial', 40, bold=True)
        self.fps = pygame.time.Clock()
        self.image = pygame.image.load('background.jpg')
        self.results = []


# displaying Score function
def show_score(color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(globals.score), True, color)

    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game.game_window.blit(score_surface, score_rect)


# game over function
def game_over():
    globals.counter += 1
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(globals.score), True, pygame.Color('red'))

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (globals.window_x / 2, globals.window_y / 4)

    # blit will draw the text on screen
    game.game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    game.results.append([globals.name.get_value(), globals.score])
    globals.counter_j += 1
    game.results.sort(key=lambda x: -x[1])

    game.game_window.fill(pygame.Color('black'))
    # after 2 seconds we will quit the
    # program
    time.sleep(2)

    start_menu()

# set difficulty


def set_difficulty(help_button, difficulty):
    globals.level = difficulty
    pass

# set records


def records():
    game.new_table.blit(game.image, (0, 0))
    for i in range(min(globals.counter, 5)):
        output = str(game.results[i][0]) + ':' + str(game.results[i][1])
        render_table = game.font_table.render(f' {output}', True, pygame.Color('red'))
        game.new_table.blit(render_table, (100, 100 + 50 * i))
    time.sleep(6)

# drawing rocks


def rooks():
    if globals.level == 1:
        for rook in globals.level1:
            pygame.draw.rect(game.game_window, pygame.Color('red'), pygame.Rect(
                rook[0], rook[1], 10, 10))
    if globals.level == 2:
        for rook in globals.level2:
            pygame.draw.rect(game.game_window, pygame.Color('red'), pygame.Rect(
                rook[0], rook[1], 20, 20))
    if globals.level == 3:
        for rook in globals.level3:
            pygame.draw.rect(game.game_window, pygame.Color('red'), pygame.Rect(
                rook[0], rook[1], 30, 30))
    if globals.level == 4:
        for rook in globals.level4:
            pygame.draw.rect(game.game_window, pygame.Color('red'), pygame.Rect(
                rook[0], rook[1], 40, 40))
    if globals.level == 5:
        for rook in globals.level5:
            pygame.draw.rect(game.game_window, pygame.Color('red'), pygame.Rect(
                rook[0], rook[1], 50, 50))

# check if snake have met a rock


def check_rook(snake_position):
    if globals.level == 1:
        for rook in globals.level1:
            c = snake_position[0] - rook[0]
            d = snake_position[1] - rook[1]
            if c == 0 and d == 0:
                game_over()
    if globals.level == 2:
        for rook in globals.level2:
            c = snake_position[0] - rook[0]
            d = snake_position[1] - rook[1]
            if 0 <= c <= 10 and 0 <= d <= 10:
                game_over()
    if globals.level == 3:
        for rook in globals.level3:
            c = snake_position[0] - rook[0]
            d = snake_position[1] - rook[1]
            if 0 <= c <= 20 and 0 <= d <= 20:
                game_over()
    if globals.level == 4:
        for rook in globals.level4:
            c = snake_position[0] - rook[0]
            d = snake_position[1] - rook[1]
            if 0 <= c <= 30 and 0 <= d <= 30:
                game_over()
    if globals.level == 5:
        for rook in globals.level5:
            c = snake_position[0] - rook[0]
            d = snake_position[1] - rook[1]
            if 0 <= c <= 40 and 0 <= d <= 40:
                game_over()

# Main function


def start_the_game():
    i = 0
    k = 0
    snake_position = [100, 50]
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
    globals.score = 0
    direction = 'RIGHT'
    change_to = direction
    globals.snake_speed = 15 + globals.level
    fruit_spawn = True
    fruit_spawn_big = True
    fruit_position = [random.randrange(1, (globals.window_x // 10)) * 10,
                      random.randrange(1, (globals.window_y // 10)) * 10]
    fruit_position_big = [random.randrange(2, (globals.window_x // 10) - 1) * 10,
                          random.randrange(2, (globals.window_y // 10) - 1) * 10]
    while True:
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two directions
        # simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= globals.pixel
        if direction == 'DOWN':
            snake_position[1] += globals.pixel
        if direction == 'LEFT':
            snake_position[0] -= globals.pixel
        if direction == 'RIGHT':
            snake_position[0] += globals.pixel

        # Snake body growing mechanism
        # if fruits and snakes collide then scores will be
        # incremented by 10
        snake_body.insert(0, list(snake_position))
        a = snake_position[0] - fruit_position_big[0]
        b = snake_position[1] - fruit_position_big[1]
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            i += 1
            globals.score += 10
            globals.snake_speed += 0.5
            fruit_spawn = False
        elif (a == 10 or a == 0) and (b == 10 or b == 0):
            i += 1
            k += 1
            globals.score += 20
            globals.snake_speed += 1
            fruit_spawn_big = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (globals.window_x // 10)) * 10,
                              random.randrange(1, (globals.window_y // 10)) * 10]

        if not fruit_spawn_big:
            fruit_position_big = [random.randrange(2, (globals.window_x // 10 - 1)) * 10,
                                  random.randrange(2, (globals.window_y // 10 - 1)) * 10]

        fruit_spawn = True
        fruit_spawn_big = True
        game.game_window.fill(pygame.Color('black'))
        rooks()
        for pos in snake_body:
            pygame.draw.rect(game.game_window, pygame.Color('green'), pygame.Rect(
                pos[0], pos[1], 10, 10))
        pygame.draw.rect(game.game_window, pygame.Color('white'), pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))
        if i % 5 == 0:
            k = 0
        if k == 0:
            pygame.draw.rect(game.game_window, pygame.Color('purple'), pygame.Rect(
                fruit_position_big[0], fruit_position_big[1], 20, 20))
        # Game Over conditions
        check_rook(snake_position)
        if snake_position[0] < 0 or snake_position[0] > globals.window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > globals.window_y - 10:
            game_over()
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # displaying score
        show_score(pygame.Color('white'), 'arial', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        game.fps.tick(globals.snake_speed)
#        pass


def start_menu():
    menu = pygame_menu.Menu('Welcome', 400, 300,
                            theme=pygame_menu.themes.THEME_BLUE)

    globals.name = menu.add.text_input('Name :', default='Player')
    menu.add.button('Records', records)
    menu.add.selector('Difficulty :', [('Very Easy', 1), ('Easy', 2), ('Medium', 3), ('Hard', 4), ('Very Hard', 5)],
                      onchange=set_difficulty)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(game.game_window)


game = Game()
