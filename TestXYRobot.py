import unittest
from XYRobot import XYRobot
from TurtleBot import TurtleBot

class TestXYRobot(unittest.TestCase):
    r2d2 = XYRobot("R2-D2")

    def test_move_forward(self):
        forward = 50
        x, y = TestXYRobot.r2d2.position()
        expected_position = (x+forward, 0+y)
        expected_angle = TestXYRobot.r2d2.angle()
        TestXYRobot.r2d2.move_forward(50)
        self.assertEqual(TestXYRobot.r2d2.position(), expected_position, "Your turtleBot has not moved forward "+str(forward)+" as expected")
        self.assertAlmostEqual(TestXYRobot.r2d2.angle(), expected_angle, msg = "Your turtleBot changed heading while moving forward")

    def test_move_backward(self):
        backward = 50
        x, y = TestXYRobot.r2d2.position()
        expected_position = (x - backward, 0+y)
        expected_angle = TestXYRobot.r2d2.angle()
        TestXYRobot.r2d2.move_backward(50)
        self.assertEqual(expected_position, TestXYRobot.r2d2.position())
        self.assertEqual(expected_angle, TestXYRobot.r2d2.angle())

    def test_turn_left(self):
        forward = 50
        x, y = TestXYRobot.r2d2.position()
        expected_position = (x + forward, y + 0)
        expected_angle = TestXYRobot.r2d2.angle()
        for i in range(4):
            TestXYRobot.r2d2.turn_left()
        TestXYRobot.r2d2.move_forward(50)
        self.assertEqual(expected_position, TestXYRobot.r2d2.position())
        self.assertEqual(expected_angle, TestXYRobot.r2d2.angle())

    def test_turn_right(self):
        forward = 50
        x, y = TestXYRobot.r2d2.position()
        expected_position = (x + 0, y + forward)
        TestXYRobot.r2d2.turn_right()
        expected_angle = TestXYRobot.r2d2.angle()
        TestXYRobot.r2d2.move_forward(forward)
        self.assertEqual(expected_position, TestXYRobot.r2d2.position())
        self.assertEqual(expected_angle, TestXYRobot.r2d2.angle())

    def test_square(self):
        """
        test pour faire un carré
        """
        forward = 50
        x, y = TestXYRobot.r2d2.position()
        expected_position = (x + 0, y + 0)
        expected_angle = TestXYRobot.r2d2.angle()
        for i in range(4):
            TestXYRobot.r2d2.move_forward(forward)
            TestXYRobot.r2d2.turn_right()
        self.assertEqual(expected_position, TestXYRobot.r2d2.position())
        self.assertEqual(expected_angle, TestXYRobot.r2d2.angle())

class TestRobot(unittest.TestCase):

    def test_history(self):
        a = TurtleBot("Toto")
        a.move_forward(50)
        a.turn_right()
        a.move_forward(50)

        b = XYRobot("Toto")
        b.move_forward(50)
        b.turn_right()
        b.move_forward(50)
        assert b.history() == [('move_forward', 50), ('turn_right', 90), ('move_forward', 50)]
        assert a.history() == [('move_forward', 50), ('turn_right', 90), ('move_forward', 50)]

    def test_unplay(self):
        a = TurtleBot("Toto")
        a.move_forward(50)
        a.turn_right()
        a.move_forward(50)
        a.unplay()

        b = XYRobot("Toto")
        b.move_forward(50)
        b.turn_right()
        b.move_forward(50)
        b.unplay()
        assert b.position() == (0, 0)
        assert a.position() == (0, 0)



if __name__ == '__main__':
    unittest.main(verbosity=2)
