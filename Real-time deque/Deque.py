from RealTimeDeque import Deque_0, Deque_1
from Element import Element
from Stack import Stack, stack_to_array

def push_left(value, dq):
    if dq.state == 0:
        return push_left_0(value, dq)

    if dq.state == 1:
        return push_left_1(value, dq)
  

def push_right(value, dq):
    if dq.state == 0:
        return push_right_0(value, dq)

    if dq.state == 1:
        return push_right_1(value, dq)        


def pop_left(dq):
    if dq.state == 0:
        return pop_left_0(dq)

    if dq.state == 1:
        return pop_left_1(dq)    

def pop_right(dq):
    if dq.state == 0:
        return pop_right_0(dq)

    if dq.state == 1:
        return pop_right_1(dq)        



 

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
    if (3*n_length) < dq.RHS_length or (3*dq.RHS_length) < n_length:
        # prechod do 2 
        print("prechod 2")
        pass

    return Deque_1(n_LHS, dq.RHS, n_length, dq.RHS_length)

def push_right_1(value, dq):
    
    n_RHS = Stack( Element(value, dq.RHS.first), dq.RHS.second )
    n_length = dq.RHS_length + 1
    # přidání prvku do pravého stacku a zvětšení délky pravého stacku

    # invariant 3*|S| >= |B|
    if (3*n_length) < dq.LHS_length or (3*dq.LHS_length) < n_length:
        # prechod do 2 
        print("prechod 2")
        pass

    return Deque_1(dq.LHS, n_RHS, dq.LHS_length, n_length)

def pop_left_1(dq):
    
    value = dq.LHS.get().value
    n_LHS = dq.LHS.next()
    n_length = dq.LHS_length - 1
    
    # invariant 3*|S| >= |B|
    if (3*n_length) < dq.RHS_length or (3*dq.RHS_length) < n_length:
        # prechod do 2 
        print("prechod 2")
        pass    

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
    if (3*n_length) < dq.LHS_length or (3*dq.LHS_length) < n_length:
        # prechod do 2 
        print("prechod 2")
        pass

    if n_length == 0:
        # prechod do 0
        return value, Deque_0(stack_to_array(dq.LHS))    

    return value, Deque_1(dq.LHS, n_RHS, dq.LHS_length, n_length)    
#---------------------------------------------------------------------