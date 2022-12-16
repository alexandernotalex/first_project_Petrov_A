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
    def show_score(self, color, font, size):
        # creating font object score_font
        score_font = pygame.font.SysFont(font, size)

        # create the display surface object
        # score_surface
        score_surface = score_font.render('Score : ' + str(globals.score), True, color)

        # create a rectangular object for the
        # text surface object
        score_rect = score_surface.get_rect()

        # displaying text
        self.game_window.blit(score_surface, score_rect)

    # game over function
    def game_over(self):
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
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        self.results.append([globals.name.get_value(), globals.score])
        globals.counter_j += 1
        self.results.sort(key=lambda x: -x[1])

        self.game_window.fill(pygame.Color('black'))
        # after 2 seconds we will quit the
        # program
        time.sleep(2)

        start_menu()

    # set difficulty

    def set_difficulty(self, help_button, difficulty):
        globals.level = difficulty
        pass

    # set records

    def records(self):
        self.new_table.blit(self.image, (0, 0))
        for i in range(min(globals.counter, 5)):
            output = str(self.results[i][0]) + ':' + str(self.results[i][1])
            render_table = self.font_table.render(f' {output}', True, pygame.Color('red'))
            self.new_table.blit(render_table, (100, 100 + 50 * i))
        time.sleep(6)

    # drawing rocks

    def rooks(self):
        pixel = globals.pixel
        if globals.level == 1:
            for rook in globals.level1:
                pygame.draw.rect(self.game_window, pygame.Color('red'), pygame.Rect(
                    rook[0], rook[1], pixel, pixel))
        if globals.level == 2:
            for rook in globals.level2:
                pygame.draw.rect(self.game_window, pygame.Color('red'), pygame.Rect(
                    rook[0], rook[1], 2*pixel, 2*pixel))
        if globals.level == 3:
            for rook in globals.level3:
                pygame.draw.rect(self.game_window, pygame.Color('red'), pygame.Rect(
                    rook[0], rook[1], 3*pixel, 3*pixel))
        if globals.level == 4:
            for rook in globals.level4:
                pygame.draw.rect(self.game_window, pygame.Color('red'), pygame.Rect(
                    rook[0], rook[1], 4*pixel, 4*pixel))
        if globals.level == 5:
            for rook in globals.level5:
                pygame.draw.rect(self.game_window, pygame.Color('red'), pygame.Rect(
                    rook[0], rook[1], 5*pixel, 5*pixel))

    # check if snake have met a rock

    def check_rook(self, snake_position):
        pixel = globals.pixel
        if globals.level == 1:
            for rook in globals.level1:
                c = snake_position[0] - rook[0]
                d = snake_position[1] - rook[1]
                if c == 0 and d == 0:
                    self.game_over()
        if globals.level == 2:
            for rook in globals.level2:
                c = snake_position[0] - rook[0]
                d = snake_position[1] - rook[1]
                if 0 <= c <= pixel and 0 <= d <= pixel:
                    self.game_over()
        if globals.level == 3:
            for rook in globals.level3:
                c = snake_position[0] - rook[0]
                d = snake_position[1] - rook[1]
                if 0 <= c <= 2*pixel and 0 <= d <= 2*pixel:
                    self.game_over()
        if globals.level == 4:
            for rook in globals.level4:
                c = snake_position[0] - rook[0]
                d = snake_position[1] - rook[1]
                if 0 <= c <= 3*pixel and 0 <= d <= 3*pixel:
                    self.game_over()
        if globals.level == 5:
            for rook in globals.level5:
                c = snake_position[0] - rook[0]
                d = snake_position[1] - rook[1]
                if 0 <= c <= 4*pixel and 0 <= d <= 4*pixel:
                    self.game_over()

    # Main function

    def start_the_game(self):
        i = 0
        k = 0
        pixel = globals.pixel
        snake_position = [10*pixel, 5*pixel]
        snake_body = [[10*pixel, 5*pixel],
                      [9*pixel, 5*pixel],
                      [8*pixel, 5*pixel],
                      [7*pixel, 5*pixel]
                      ]
        globals.score = 0
        direction = 'RIGHT'
        change_to = direction
        globals.snake_speed = 15 + globals.level
        fruit_spawn = True
        fruit_spawn_big = True
        fruit_position = [random.randrange(1, (globals.window_x // 10)) * pixel,
                          random.randrange(1, (globals.window_y // 10)) * pixel]
        fruit_position_big = [random.randrange(2, (globals.window_x // 10) - 1) * pixel,
                              random.randrange(2, (globals.window_y // 10) - 1) * pixel]
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
                globals.score += pixel
                globals.snake_speed += 0.5
                fruit_spawn = False
            elif (a == pixel or a == 0) and (b == pixel or b == 0):
                i += 1
                k += 1
                globals.score += 2*pixel
                globals.snake_speed += 1
                fruit_spawn_big = False
            else:
                snake_body.pop()

            if not fruit_spawn:
                fruit_position = [random.randrange(1, (globals.window_x // 10)) * pixel,
                                  random.randrange(1, (globals.window_y // 10)) * pixel]

            if not fruit_spawn_big:
                fruit_position_big = [random.randrange(2, (globals.window_x // 10 - 1)) * pixel,
                                      random.randrange(2, (globals.window_y // 10 - 1)) * pixel]

            fruit_spawn = True
            fruit_spawn_big = True
            self.game_window.fill(pygame.Color('black'))
            self.rooks()
            for pos in snake_body:
                pygame.draw.rect(self.game_window, pygame.Color('green'), pygame.Rect(
                    pos[0], pos[1], pixel, pixel))
            pygame.draw.rect(self.game_window, pygame.Color('white'), pygame.Rect(
                fruit_position[0], fruit_position[1], pixel, pixel))
            if i % 5 == 0:
                k = 0
            if k == 0:
                pygame.draw.rect(self.game_window, pygame.Color('purple'), pygame.Rect(
                    fruit_position_big[0], fruit_position_big[1], 2*pixel, 2*pixel))
            # Game Over conditions
            self.check_rook(snake_position)
            if snake_position[0] < 0 or snake_position[0] > globals.window_x - pixel:
                self.game_over()
            if snake_position[1] < 0 or snake_position[1] > globals.window_y - pixel:
                self.game_over()
            # Touching the snake body
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    self.game_over()

            # displaying score
            self.show_score(pygame.Color('white'), 'arial', 2*pixel)

            # Refresh game screen
            pygame.display.update()

            # Frame Per Second /Refresh Rate
            self.fps.tick(globals.snake_speed)
    #        pass


def start_menu():
    game = Game()
    menu = pygame_menu.Menu('Welcome', 400, 300,
                            theme=pygame_menu.themes.THEME_BLUE)

    globals.name = menu.add.text_input('Name :', default='Player')
    menu.add.button('Records', game.records)
    menu.add.selector('Difficulty :', [('Very Easy', 1), ('Easy', 2), ('Medium', 3), ('Hard', 4), ('Very Hard', 5)],
                      onchange=game.set_difficulty)
    menu.add.button('Play', game.start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(game.game_window)

# game = Game()
