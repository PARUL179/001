class animal(object):
    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print('{0} eats {1}'.format(self.name,food))

class dog(animal):
    def fetch(self,thing):
        print('{0} goes after {1}'.format(self.name, thing))

    def show_aff(self):
        print('{0} talls for'.format(self.name))

class cat(animal):
    def sw(self,thing):
        print('{0} shat for'.format(self.name))

    def show_aff(self):
        print('{0} purrs for'.format(self.name))

for a in (dog('r'),cat('c'),dog('p'),cat('s')):
    a.show_aff()

