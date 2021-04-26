
class Deque_0(object):

    def __init__(self, list):
        self.list = list
        self.state = 0

    def __str__(self):
        return "{} state: {}".format(self.list, self.state)


class Deque_1(object):
    
    def __init__(self, LHS, RHS, LHS_length, RHS_length):
        self.LHS = LHS # levý stack
        self.RHS = RHS # pravý stack
        # délky stacků
        self.LHS_length = LHS_length
        self.RHS_length = RHS_length

        self.state = 1

    def __str__(self):
        arr = []
        LHS = self.LHS
        while True:
            if LHS.get() is None:
                break
            arr.append(LHS.get().value)
            LHS = LHS.next()

        arr2 = []
        RHS = self.RHS
        while True:
            if RHS.get() is None:
                break
            arr2.append(RHS.get().value)
            RHS = RHS.next()

        arr2 = arr2[::-1]
        arr3 = arr + arr2

        return "{} state: {}".format(arr3, self.state)


        #return "LHS: {} RHS: {} LHS_length: {} RHS_length: {} state: {}".format(self.LHS, self.RHS, self.LHS_length, self.RHS_length, self.state)

class Deque_2(object):

    def __init__(self, side, S, B, S_origin, B_origin, aux_S, aux_B, extra_S, extra_B, copy_S, copy_B, extra_S_size, extra_B_size, aux_counter):

        self.side = side# True znamená S - B False znamená B - S
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

    def __str__(self):

        if self.side:
            arr1 = []
            extra_S = self.extra_S
            while True:
                if extra_S is None:
                    break
                arr1.append(extra_S.value)
                extra_S = extra_S.next    

            arr2 = []
            S = self.S_origin
            while True:
                if S.get() is None:
                    break
                arr2.append(S.get().value)
                S = S.next()             


            arr3 = []
            B = self.B_origin
            while True:
                if B.get() is None:
                    break
                arr3.append(B.get().value)
                B = B.next() 
            arr3 = arr3[::-1]

            arr4 = []
            extra_B = self.extra_B
            while True:
                if extra_B is None:
                    break
                arr4.append(extra_B.value)
                extra_B = extra_B.next      
            arr4 = arr4[::-1]         

            arr = arr1 + arr2 + arr3 + arr4

        else:
            arr1 = []
            extra_S = self.extra_S
            while True:
                if extra_S is None:
                    break
                arr1.append(extra_S.value)
                extra_S = extra_S.next    
            arr1 = arr1[::-1]

            arr2 = []
            S = self.S_origin
            while True:
                if S.get() is None:
                    break
                arr2.append(S.get().value)
                S = S.next()             
            arr2 = arr2[::-1]

            arr3 = []
            B = self.B_origin
            while True:
                if B.get() is None:
                    break
                arr3.append(B.get().value)
                B = B.next() 


            arr4 = []
            extra_B = self.extra_B
            while True:
                if extra_B is None:
                    break
                arr4.append(extra_B.value)
                extra_B = extra_B.next      
      

            arr = arr4 + arr3 + arr2 + arr1

        return "{} state: {}".format(arr, self.state)

                                      
            

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

    def __str__(self):
    
        if self.side:
            arr1 = []
            extra_S = self.extra_S
            while True:
                if extra_S is None:
                    break
                arr1.append(extra_S.value)
                extra_S = extra_S.next    

            arr2 = []
            S = self.S_origin
            while True:
                if S.get() is None:
                    break
                arr2.append(S.get().value)
                S = S.next()             


            arr3 = []
            B = self.B_origin
            while True:
                if B.get() is None:
                    break
                arr3.append(B.get().value)
                B = B.next() 
            arr3 = arr3[::-1]

            arr4 = []
            extra_B = self.extra_B
            while True:
                if extra_B is None:
                    break
                arr4.append(extra_B.value)
                extra_B = extra_B.next      
            arr4 = arr4[::-1]         

            arr = arr1 + arr2 + arr3 + arr4

        else:
            arr1 = []
            extra_S = self.extra_S
            while True:
                if extra_S is None:
                    break
                arr1.append(extra_S.value)
                extra_S = extra_S.next    
            arr1 = arr1[::-1]

            arr2 = []
            S = self.S_origin
            while True:
                if S.get() is None:
                    break
                arr2.append(S.get().value)
                S = S.next()             
            arr2 = arr2[::-1]

            arr3 = []
            B = self.B_origin
            while True:
                if B.get() is None:
                    break
                arr3.append(B.get().value)
                B = B.next() 


            arr4 = []
            extra_B = self.extra_B
            while True:
                if extra_B is None:
                    break
                arr4.append(extra_B.value)
                extra_B = extra_B.next      
      

            arr = arr4 + arr3 + arr2 + arr1

        return "{} state: {}".format(arr, self.state)    