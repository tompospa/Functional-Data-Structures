from RealTimeDeque import Deque_0
from Deque import *
from tests import MyTests
from SimpleDeque import SimpleDeque, pop_left_simple, pop_right_simple, push_left_simple, push_right_simple
''''
x = new()
print(x)

#x = push_left(1,x)
#x = push_right(1,x)
#x = pop_left(x)
#x = pop_right(x)

x = push_right(1,x)
x = push_right(2,x)
x = push_right(3,x)
x = push_right(4,x)
x = push_right(5,x)
x = push_right(6,x)
x = push_right(7,x)
x = push_right(8,x)
x = push_right(9,x)
x = push_right(10,x)
x = push_right(11,x)


print(x)
#print(x.side)

mytest = MyTests()


SDQ = SimpleDeque()
RTDQ = new()


x2 = new()
#[34, 37, 47, 18, 42, 44, 19, 7]
x2 = push_left(18, x2)
x2 = push_left(47, x2)
x2 = push_left(37, x2)
x2 = push_left(34, x2)
print(x2)
x2 = push_right(42, x2)
x2 = push_right(44, x2)
x2 = push_right(19, x2)
x2 = push_right(7, x2)
print(x2)
print(x2.LHS_length)
print(x2.RHS_length)
v, x2 = pop_left(x2)
print(x2)'''

mytest = MyTests()
SDQ = SimpleDeque()
RTDQ = new()


print('validity')
print(mytest.check_realtimeDQ_validity(RTDQ,SDQ,10000))




#mytest.deque_1_test()

#mytest.stack_test()

#print("{} -> {} ....... {} <- {}".format(x1.LHS.value, x1.LHS.next.value, x1.RHS.next.value, x1.RHS.value ))

    

