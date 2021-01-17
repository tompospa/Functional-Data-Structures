from Element import Element

class SimpleQueue(object):

    def __init__(self):
        self.qlist = []
        self.state = 3
        
def s_enqueue(q, value):
    n_q = SimpleQueue()
    n_q.qlist = q.qlist
    n_q.qlist.append(value)
    #print("simplequeue pridavam {0}".format(value))
    return n_q

def s_dequeue(q):
    if not q.qlist:
        #print("fronta prazdna nic nleze odebrat")
        return None, q #pro testovani 
    value = q.qlist[0]
    q.qlist.pop(0)
    n_q = SimpleQueue()
    n_q.qlist = q.qlist
    #print("simplequeue odebiram {0}".format(value))
    return value, n_q

"""
q = Queue()
enqueue(q, 3)
enqueue(q, 35)
enqueue(q, 9)
enqueue(q, 12)
enqueue(q, 6)
enqueue(q, 7)
enqueue(q, 11)
print(q.qlist)
dequeue(q)
print(q.qlist)
"""