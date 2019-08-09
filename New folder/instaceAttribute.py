import random

class test(object):
    def doThis(self):
        self.rand_val=random.randint(1,10)


t=test()
t.doThis()
print(t.rand_val)
print(t)