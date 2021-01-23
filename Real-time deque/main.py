from RealTimeDeque import Deque_0
from Deque import *
from tests import MyTests

x = Deque_0([1,2,3])

print(x)

x1 = push_right(4 ,x)

print(x1)

print("{} -> {} ....... {} <- {}".format(x1.LHS.get().value, x1.LHS.next().value, x1.RHS.next().value, x1.RHS.get().value ))

mytest = MyTests()

#mytest.stack_test()

#print("{} -> {} ....... {} <- {}".format(x1.LHS.value, x1.LHS.next.value, x1.RHS.next.value, x1.RHS.value ))

