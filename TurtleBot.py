from Robot import Robot
import turtle

class TurtleBot(Robot):

    def __init__(self, nom, x=0, y=0):
        super().__init__(nom)
        self.__x = x
        self.__y = y
        self.__t = turtle.Turtle()
        self.wn = turtle.Screen()
        self.__angle = 0

    def angle_rad(self):
        '''
        retourne l'angle en degres radius représentant la direction du robot
        '''

        return self.__angle

    def __str__(self):
        """
        Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant le nom,
        les coordonnées et l'orientation du robot.
        """
        return str(super().nom()) + "@(" + str(self.x()) + "," + \
               str(self.y()) + ") angle: " + str(self.angle())

    def position(self):
        return self.x(), self.y()

    def angle(self):
        "retourne l'angle en degres représentant la direction du robot"
        # return ( self.angle_rad() * 180 / pi ) % 360
        self.__angle = self.__t.heading()
        return self.__angle

    def move_forward(self, distance):
        self.__t.forward(distance)
        self.__x = self.__t.xcor()
        self.__y = self.__t.xcor()
        super().add_action('move_forward', distance)

    def move_backward(self, distance):
        self.__t.backward(distance)
        self.__x = self.__t.xcor()
        self.__y = self.__t.ycor()
        super().add_action('move_backward', distance)

    def turn_left(self):
        self.__t.left(90)
        super().add_action("turn_left", 90)

    def turn_right(self):
        self.__t.right(90)
        super().add_action("turn_right", 90)

    def x(self):
        return self.__x

    def y(self):
        return self.__y


# Exemple d'utilisation de cette classe (il suffit d'exécuter ce fichier)
if __name__ == '__main__':
    toto = TurtleBot("Toto")
    print(toto)
    toto.move_backward(50)
    print(toto)
    toto.turn_right()
    toto.move_forward(50)
    print(toto)
    print(toto.history())
    toto.wn.mainloop()
