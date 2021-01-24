from RealTimeDeque import Deque_0, Deque_1, Deque_2, Deque_3
from Element import Element
from Stack import Stack, stack_to_array

def push_left(value, dq):
    if dq.state == 0:
        return push_left_0(value, dq)

    if dq.state == 1:
        return push_left_1(value, dq)
  
    if dq.state == 2 or dq.state == 3:
        return push_left_transfer(value, dq)

def push_right(value, dq):
    if dq.state == 0:
        return push_right_0(value, dq)

    if dq.state == 1:
        return push_right_1(value, dq)   

    if dq.state == 2 or dq.state == 3:
        return push_right_transfer(value, dq)

def pop_left(dq):
    if dq.state == 0:
        return pop_left_0(dq)

    if dq.state == 1:
        return pop_left_1(dq)    

    if dq.state == 2 or dq.state == 3:
        return pop_left_transfer(dq)        

def pop_right(dq):
    if dq.state == 0:
        return pop_right_0(dq)

    if dq.state == 1:
        return pop_right_1(dq)     

    if dq.state == 2 or dq.state == 3:
        return pop_right_transfer(dq)           



 

def new():
    return Deque_0([])

def is_empty(q):
    if q.state == 0:
        if len(q.list) == 0:
            return True
        return False
    return False 

# deque_0 operations
#---------------------------------------------------------------------
def push_left_0(value, dq):

    n_dq_list = []
    n_dq_list.append(value)
    for x in dq.list:
        n_dq_list.append(x)
    # vytváření nového listu [value, dq.list[0], ... dq.listp[n]]

    if len(n_dq_list) == 4:
        LHS = Stack( Element(n_dq_list[0], Element(n_dq_list[1], None)), None )
        RHS = Stack( Element(n_dq_list[2], Element(n_dq_list[2], None)), None )

        return Deque_1(LHS, RHS, 2, 2)

    return Deque_0(n_dq_list) 

def push_right_0(value, dq):
    
    n_dq_list = []
    for x in dq.list:
        n_dq_list.append(x)
    n_dq_list.append(value)
    # vytváření nového listu [value, dq.list[0], ... dq.listp[n]]

    if len(n_dq_list) == 4:
        LHS = Stack( Element(n_dq_list[0], Element(n_dq_list[1], None)), None )
        RHS = Stack( Element(n_dq_list[3], Element(n_dq_list[2], None)), None )

        return Deque_1(LHS, RHS, 2, 2)

    return Deque_0(n_dq_list) 

def pop_left_0(dq):
    if len(dq.list) == 0:
        return None, dq
    
    n_dq_list = []
    for i in range(len(dq.list)):
        if i == 0:
            continue
        n_dq_list.append(dq.list[i])

    return dq.list[0], Deque_0(n_dq_list) 


def pop_right_0(dq):
    if len(dq.list) == 0:
        return None, dq
    
    n_dq_list = []
    for i in range(len(dq.list)-1):
        n_dq_list.append(dq.list[i])

    return dq.list[-1], Deque_0(n_dq_list) 
#---------------------------------------------------------------------


# deque_1 operations
#---------------------------------------------------------------------
def push_left_1(value, dq):

    n_LHS = Stack( Element(value, dq.LHS.first), dq.LHS.second )
    n_length = dq.LHS_length + 1
    # přidání prvku do levého stacku a zvětšení délky levého stacku

    # invariant 3*|S| >= |B|
    if (3*dq.RHS_length) < n_length:
        # prechod do 2 
        # Small je RHS a Big je LHS
        print("prechod 2")

        k = n_length%3
        counter = 2*dq.RHS_length + k - 1
        n_dq = Deque_2(False, dq.RHS, n_LHS, dq.RHS, n_LHS, None, None, None, None, 0, 0, 0, 0, counter)
        for x in range(6):
            n_dq = do_steps(n_dq)
            if n_dq.state == 1:
                return n_dq

        return n_dq
        #Deque_2        side   S        B     S_ori   B_ori  auxS  auxB  ex_S  ex_B CS CB SS  BS  counter)



    return Deque_1(n_LHS, dq.RHS, n_length, dq.RHS_length)

def push_right_1(value, dq):
    
    n_RHS = Stack( Element(value, dq.RHS.first), dq.RHS.second )
    n_length = dq.RHS_length + 1
    # přidání prvku do pravého stacku a zvětšení délky pravého stacku

    # invariant 3*|S| >= |B|
    if (3*dq.LHS_length) < n_length:
        # prechod do 2 
        # Small je LHS a Big je RHS
        print("prechod 2")

        k = n_length%3
        counter = 2*dq.LHS_length + k - 1
        n_dq = Deque_2(True, dq.LHS, n_RHS, dq.LHS, n_RHS, None, None, None, None, 0, 0, 0, 0, counter)
        for x in range(6):
            n_dq = do_steps(n_dq)
            if n_dq.state == 1:
                return n_dq

        return n_dq        


    return Deque_1(dq.LHS, n_RHS, dq.LHS_length, n_length)

def pop_left_1(dq):
    
    value = dq.LHS.get().value
    n_LHS = dq.LHS.next()
    n_length = dq.LHS_length - 1
    
    # invariant 3*|S| >= |B|
    if (3*n_length) < dq.RHS_length:
        # prechod do 2 
        # Small je LHS a Big je RHS
        print("prechod 2")

        k = dq.RHS_length%3
        counter = 2*n_length + k - 1
        n_dq = Deque_2(True, n_LHS, dq.RHS, n_LHS, dq.RHS, None, None, None, None, 0, 0, 0, 0, counter)
        for x in range(6):
            n_dq = do_steps(n_dq)
            if n_dq.state == 1:
                return value, n_dq

        return value, n_dq        

    if n_length == 0:
        # prechod do 0
        arr = stack_to_array(dq.RHS)
        arr = arr[::-1]
        return value, Deque_0(arr)

    return value, Deque_1(n_LHS, dq.RHS, n_length, dq.RHS_length)


def pop_right_1(dq):
    
    value = dq.RHS.get().value
    n_RHS = dq.RHS.next()
    n_length = dq.RHS_length - 1

    # invariant 3*|S| >= |B|
    if (3*n_length) < dq.LHS_length:
        # prechod do 2 
        # Small je RHS a Big je LHS   
        print("prechod 2")

        k = dq.LHS_length%3
        counter = 2*n_length + k - 1
        n_dq = Deque_2(False, n_RHS, dq.LHS, n_RHS, dq.LHS, None, None, None, None, 0, 0, 0, 0, counter) 
        for x in range(6):
            n_dq = do_steps(n_dq)
            if n_dq.state == 1:
                return value, n_dq

        return value, n_dq     

    if n_length == 0:
        # prechod do 0
        return value, Deque_0(stack_to_array(dq.LHS))    

    return value, Deque_1(dq.LHS, n_RHS, dq.LHS_length, n_length)    
#---------------------------------------------------------------------

# deque_transfer operations
#---------------------------------------------------------------------
def push_left_transfer(value, dq):

    n_extra_S = dq.extra_S
    n_extra_S_size = dq.extra_S_size  
    n_extra_B = dq.extra_B
    n_extra_B_size = dq.extra_B_size         
    
    if dq.side:
        n_extra_S = Element(value, dq.extra_S)
        n_extra_S_size = dq.extra_S_size + 1
    else:
        n_extra_B = Element(value, dq.extra_B)
        n_extra_B_size = dq.extra_B_size + 1  

    if dq.state == 2:
        n_dq = Deque_2(dq.side, dq.S, dq.B, dq.S_origin, dq.B_origin, dq.aux_S, dq.aux_B, n_extra_S, n_extra_B, dq.copy_S, dq.copy_B, n_extra_S_size, n_extra_B_size, dq.aux_counter)
    if dq.state == 3:
        n_dq = Deque_3(dq.side, dq.B, dq.S_origin, dq.B_origin, dq.aux_S, dq.aux_B, n_extra_S, n_extra_B, dq.copy_S, dq.copy_B, n_extra_S_size, n_extra_B_size, dq.new_S, dq.new_B, dq.S_size, dq.B_size)   

    for x in range(4):
        n_dq = do_steps(n_dq)
        if n_dq.state == 1:
            return n_dq

    return n_dq     
        
def push_right_transfer(value, dq):
    
    n_extra_S = dq.extra_S
    n_extra_S_size = dq.extra_S_size  
    n_extra_B = dq.extra_B
    n_extra_B_size = dq.extra_B_size     
    
    if not dq.side:
        n_extra_S = Element(value, dq.extra_S)
        n_extra_S_size = dq.extra_S_size + 1
    else:
        n_extra_B = Element(value, dq.extra_B)
        n_extra_B_size = dq.extra_B_size + 1  
    
    if dq.state == 2:
        n_dq = Deque_2(dq.side, dq.S, dq.B, dq.S_origin, dq.B_origin, dq.aux_S, dq.aux_B, n_extra_S, n_extra_B, dq.copy_S, dq.copy_B, n_extra_S_size, n_extra_B_size, dq.aux_counter)
    if dq.state == 3:
        n_dq = Deque_3(dq.side, dq.B, dq.S_origin, dq.B_origin, dq.aux_S, dq.aux_B, n_extra_S, n_extra_B, dq.copy_S, dq.copy_B, n_extra_S_size, n_extra_B_size, dq.new_S, dq.new_B, dq.S_size, dq.B_size)   

    for x in range(4):
        n_dq = do_steps(n_dq)
        if n_dq.state == 1:
            return n_dq

    return n_dq      


def pop_left_transfer(dq):
    
    if False:#dq.side:
        if dq.extra_S is None:
            pass
        value = dq.extra_S.value
        n_extra_S = dq.extra_S.next
        n_extra_S_size = dq.extra_S_size - 1 

def pop_right_transfer(dq):
    pass
     
#---------------------------------------------------------------------

def do_steps(dq):
    
    if dq.state == 2:
        
        n_aux_S = dq.aux_S
        n_copy_S = dq.copy_S
        n_S = dq.S 

        if dq.S.get() is not None:
            n_aux_S = Element(dq.S.get().value, dq.aux_S)
            n_copy_S = dq.copy_S + 1
            n_S = dq.S.next() 

        n_aux_B = Element(dq.B.get().value, dq.aux_B)
        n_copy_B = dq.copy_B + 1
        n_B = dq.B.next()
        n_counter = dq.aux_counter-1

        if n_counter == 0:
            return Deque_3(dq.side, n_B, dq.S_origin, dq.B_origin, n_aux_S, n_aux_B, dq.extra_S, dq.extra_B, n_copy_S, n_copy_B, dq.extra_S_size, dq.extra_B_size, None, None, 0, 0)#return Deque_3

        return Deque_2(dq.side, n_S, n_B, dq.S_origin, dq.B_origin, n_aux_S, n_aux_B, dq.extra_S, dq.extra_B, n_copy_S, n_copy_B, dq.extra_S_size, dq.extra_B_size, n_counter)                    

    if dq.state == 3:

        n_copy_S = dq.copy_S
        n_copy_B = dq.copy_B
        n_new_S = dq.new_S
        n_new_B = dq.new_B
        n_S_size = dq.S_size
        n_B_size = dq.B_size
        n_B = dq.B
        n_aux_S = dq.aux_S
        n_aux_B = dq.aux_B

        if dq.copy_B != 0:
            n_new_B = Element(dq.aux_B.value,dq.new_B)
            n_copy_B = dq.copy_B - 1
            n_B_size = dq.B_size + 1
            n_aux_B = dq.aux_B.next

        if dq.B.get() is None:
            n_new_S = Element(dq.aux_S.value, dq.new_S)
            n_copy_S = dq.copy_S - 1
            n_S_size = dq.S_size + 1
            n_aux_S = dq.aux_S.next
        
        if dq.B.get() is not None:
            n_new_S = Element(dq.B.get().value, dq.new_S)
            n_S_size = dq.S_size + 1
            n_B = dq.B.next()

        if n_copy_S == 0 and n_copy_B == 0:
            LHS = Stack(dq.extra_S, n_new_S)
            RHS = Stack(dq.extra_B, n_new_B)
            LHS_length = n_S_size + dq.extra_S_size
            RHS_length = n_B_size + dq.extra_B_size
            if dq.side:
                return Deque_1(LHS, RHS, LHS_length, RHS_length)
            return Deque_1(RHS, LHS, RHS_length, LHS_length)

        return Deque_3(dq.side, n_B, dq.S_origin, dq.B_origin, n_aux_S, n_aux_B, dq.extra_S, dq.extra_B, n_copy_S, n_copy_B, dq.extra_S_size, dq.extra_B_size, n_new_S, n_new_B, n_S_size, n_B_size)



