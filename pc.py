import datetime
import json

from sklearn.cluster import MeanShift

class Mess:
    def __init__(self, type, data, date) -> None:
        self.type = type
        # self.id = id
        self.data = data
        self.date = date
    def __str__(self) -> str:
        return "messObj(type={}, data={}, date={})".format(self.type, self.data, self.date)


m = Mess("ok","okok", "okko")
a = [m.__dict__,m.__dict__,m.__dict__,m.__dict__]
j = json.dumps(a)
# print(type(j))

jj = json.loads(j)

for i in jj:
    print(i)
    print(type(i))