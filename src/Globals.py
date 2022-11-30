
class Globals:
    def __init__(self):
        # window parameters
        self.window_x = 720
        self.window_y = 480
        self.pixel = 10
        # game parameters
        self.score = 0
        self.level = 1
        self.counter = 0
        self.counter_j = 0
        self.name = ''
        # rocks parameters
        self.level1 = ([150, 150], [200, 200], [300, 300], [520, 140], [260, 250])
        self.level2 = ([100, 100], [200, 200], [310, 270], [20, 30], [680, 90])
        self.level3 = ([550, 150], [20, 20], [110, 300], [300, 150], [650, 80])
        self.level4 = ([150, 150], [170, 400], [480, 190], [270, 420], [560, 180])
        self.level5 = ([10, 10], [140, 370], [150, 190], [250, 210], [530, 330])
        # snake parameters
        self.snake_speed = 15
