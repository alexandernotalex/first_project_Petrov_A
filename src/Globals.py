
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
        # rocks parameters are randomized
        self.level1 = ([15*self.pixel, 15*self.pixel], [20*self.pixel, 20*self.pixel], [30*self.pixel, 30*self.pixel],
                       [52*self.pixel, 14*self.pixel], [26*self.pixel, 25*self.pixel])
        self.level2 = ([10*self.pixel, 10*self.pixel], [20*self.pixel, 20*self.pixel], [31*self.pixel, 27*self.pixel],
                       [2*self.pixel, 3*self.pixel], [68*self.pixel, 9*self.pixel])
        self.level3 = ([55*self.pixel, 15*self.pixel], [2*self.pixel, 2*self.pixel], [11*self.pixel, 30*self.pixel],
                       [30*self.pixel, 15*self.pixel], [65*self.pixel, 8*self.pixel])
        self.level4 = ([15*self.pixel, 15*self.pixel], [17*self.pixel, 40*self.pixel], [48*self.pixel, 19*self.pixel],
                       [27*self.pixel, 42*self.pixel], [56*self.pixel, 18*self.pixel])
        self.level5 = ([self.pixel, self.pixel], [14*self.pixel, 37*self.pixel], [15*self.pixel, 19*self.pixel],
                       [25*self.pixel, 21*self.pixel], [53*self.pixel, 33*self.pixel])
        # snake parameters
        self.snake_speed = 15
