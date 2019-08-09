class Myclass(object):
    def get_value(self,val):
        self.value=val

    def set_val(self):
        return self.value

m=Myclass()
m.get_value(10)
m.set_val()
print(m.value)
m.value='hello'
print(m.value)