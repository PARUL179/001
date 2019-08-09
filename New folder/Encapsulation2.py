class Myclass(object):
    def getVal(self,val):
        try:
            self.value=int(val)
        except ValueError:
            return
        self.value=val

    def setVal(self):
        return self.value

    def inc(self):
        self.value=self.value+1

i=Myclass()
i.getVal(10)
print(i.value)
i.inc()
print(i.value)
i.getVal('Hello')
i.setVal()
print(i.value)