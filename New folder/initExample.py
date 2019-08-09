class myini(object):
    def __init__(self):
        print("Today is a new day")
        self.val=0

    def inc(self):
        self.val=self.val+1

i=myini()
i.inc()
i.inc()
i.inc()
i.inc()
i.inc()
print(i.val)