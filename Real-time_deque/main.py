from RealTimeDeque import Deque_0
from Deque import *
from tests import MyTests
from SimpleDeque import SimpleDeque, pop_left_simple, pop_right_simple, push_left_simple, push_right_simple


def test_cas():
    pocet_operaci = [625000,1250000,2500000,5000000,10000000,20000000,40000000] 

    for x in pocet_operaci:

        mytest = MyTests()
        SDQ = SimpleDeque()
        RTDQ = new()
        print("počet operací: {} {} ".format(x, mytest.check_realtimeDQ_time(RTDQ,SDQ,x)))


#print('validity')
#print(mytest.check_realtimeDQ_validity(RTDQ,SDQ,100000))


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
print(x2)


mytest = MyTests()
SDQ = SimpleDeque()
RTDQ = new()


#print('validity')
#print(mytest.check_realtimeDQ_validity(RTDQ,SDQ,100000))

print(mytest.check_realtimeDQ_time(RTDQ,SDQ,625000))
print(mytest.check_realtimeDQ_time(RTDQ,SDQ,1250000))
print(mytest.check_realtimeDQ_time(RTDQ,SDQ,2500000))
print(mytest.check_realtimeDQ_time(RTDQ,SDQ,5000000))
print(mytest.check_realtimeDQ_time(RTDQ,SDQ,10000000))
print(mytest.check_realtimeDQ_time(RTDQ,SDQ,20000000))
print(mytest.check_realtimeDQ_time(RTDQ,SDQ,40000000))
'''


test_cas()



#mytest.deque_1_test()

#mytest.stack_test()

#print("{} -> {} ....... {} <- {}".format(x1.LHS.value, x1.LHS.next.value, x1.RHS.next.value, x1.RHS.value ))

    

