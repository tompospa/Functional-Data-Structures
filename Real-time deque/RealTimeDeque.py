
class Deque_0(object):

    def __init__(self, list):
        self.list = list
        self.state = 0

    def __str__(self):
        return "list: {} state: {}".format(self.list, self.state)


class Deque_1(object):
    
    def __init__(self, LHS, RHS, LHS_length, RHS_length):
        self.LHS = LHS # levý stack
        self.RHS = RHS # pravý stack
        # délky stacků
        self.LHS_length = LHS_length
        self.RHS_length = RHS_length

        self.state = 1

    def __str__(self):
        return "LHS: {} RHS: {} LHS_length: {} RHS_length: {} state: {}".format(self.LHS, self.RHS, self.LHS_length, self.RHS_length, self.state)
