class p(object):
    def __init__(self):
        print("parent")

class p2(object):
    def __init__(self):
        print("parent2")

class c(p2,p):
    def __init__(self):
        print("child")
        super().__init__()


ch=c()