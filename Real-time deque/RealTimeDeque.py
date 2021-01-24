
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

class Deque_2(object):

    def __init__(self, side, S, B, S_origin, B_origin, aux_S, aux_B, extra_S, extra_B, copy_S, copy_B, extra_S_size, extra_B_size, aux_counter):

        self.side = side# True znameba S - B False znamena B - S
        self.S = S
        self.B = B
        self.S_origin = S_origin
        self.B_origin = B_origin
        self.aux_S = aux_S
        self.aux_B = aux_B
        self.extra_S = extra_S
        self.extra_B = extra_B
        self.copy_S = copy_S
        self.copy_B = copy_B
        self.extra_S_size = extra_S_size
        self.extra_B_size = extra_B_size
        self.aux_counter = aux_counter
        

        self.state = 2
        

class Deque_3(object):
    
    def __init__(self, side, B, S_origin, B_origin, aux_S, aux_B, extra_S, extra_B, copy_S, copy_B, extra_S_size, extra_B_size, new_S, new_B, S_size, B_size):

        self.side = side# True znameba S - B False znamena B - S
        self.B = B
        self.S_origin = S_origin
        self.B_origin = B_origin
        self.aux_S = aux_S
        self.aux_B = aux_B
        self.extra_S = extra_S
        self.extra_B = extra_B
        self.copy_S = copy_S
        self.copy_B = copy_B
        self.extra_S_size = extra_S_size
        self.extra_B_size = extra_B_size
        self.new_S = new_S
        self.new_B = new_B
        self.S_size = S_size
        self.B_size = B_size
        
        
        self.state = 3