class Robot:
    def __init__(self, nom):
        self.__nom = nom
        self.__action = []

    def add_action(self, act, d_or_a):
        self.__action.append((act, d_or_a))

    def history(self):
        return self.__action

    def reversed(self, lst):
        from copy import copy
        cop = copy(lst)
        cop.reverse()
        return cop

    def unplay(self):
        reversed_lst = self.reversed(self.history())
        for word in reversed_lst:
            if word[0] == 'move_forward':
                self.move_backward(word[1])
            elif word[0] == 'move_backward':
                self.move_forward(word[1])
            elif word[0] == 'turn_right':
                self.turn_left()
            else:
                self.turn_right()
        self.history().clear()

    def nom(self):
        return self.__nom

    def move_forward(self, distance):
        pass

    def move_backward(self, distance):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def angle(self):
        pass