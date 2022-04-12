import datetime


class Mess:
    def __init__(self, type, data, date: datetime) -> None:
        self.type = type
        # self.id = id
        self.data = data
        self.date = date
    def __str__(self) -> str:
        return "messObj(type={}, data={}, date={})".format(self.type, self.data, self.date)