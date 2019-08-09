class Date(object):
    def get_date(self):
        return '2019-09-17'

class time(Date):
    def get_time(self):
        return '08:08:08'

dt=Date()
print(dt.get_date())

dc=time()
print(dc.get_time())
print(dc.get_date())

