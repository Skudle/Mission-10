from XYRobot import XYRobot, TurtleBot


class Robot:

    def __init__(self, nom):
        self.__nom = nom

    def nom(self):
        return self.__nom

    def move_forward(self, distance):
        self.nom().move_forward(distance)

    def move_backward(self, distance):
        self.nom().move_backward(distance)

    def turn_left(self):
        self.nom().turn_left()

    def turn_right(self):
        self.nom().turn_right()

    def history(self):
        pass

    def unplay(self):
        pass


toto = TurtleBot("toto")
toto2 = Robot(toto)
toto2.turn_right()

