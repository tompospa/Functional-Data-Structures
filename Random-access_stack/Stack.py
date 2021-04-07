from Element import Element

class Stack(object):

    def __init__(self, top):
        self.top = top

    def __str__(self):
        return "top: {}".format(self.top)

def NEW():
    return Stack(Element(None, 0, None, None))

def EMPTY(s):
    if s.top.value is None:
        return True
    else:
        return False

def TOP(s):
    return s.top

def POP(s):
    return s.top.value, Stack(s.next)

def PUSH(s, x):
    if EMPTY(s):
        n_top = Element(x, s.top.index+1, s.top, s.top)
        return Stack(n_top)
    
    jump1 = s.top.jump
    jump2 = jump1.jump
    n_jump = None

    if jump2 is None:#pouze jeden prvek ve stacku
        n_jump = s.top
    elif jump1.index-s.top.index == jump2.index-jump1.index:
        n_jump = jump2
    else:
        n_jump = s.top

    n_top = Element(x, s.top.index+1, s.top, n_jump)
    return Stack(n_top)

def LENGTH(s):
    return s.top.index

def FIND(s, k):
    if s.top.index == k:
        return s.top.value
    if s.top.index < k:
        return None#vyjímka
    pom = s.top
    while(True):
        if pom.jump.index>=k:
            pom = pom.jump
            if pom.index == k:
                return pom.value
        else:
            pom = pom.next
            if pom.index == k:
                return pom.value
            
def POP_MULTI(s, k):
    if s.top.index == k:
        return Stack(s.top)
    if s.top.index < k:
        return None#vyjímka    
    pom = s.top
    while(True):
        if pom.jump.index>=k:
            pom = pom.jump
            if pom.index == k:
                return Stack(pom)
        else:
            pom = pom.next
            if pom.index == k:
                return Stack(pom)    
        


