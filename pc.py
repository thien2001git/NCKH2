import datetime
import json

from sklearn.cluster import MeanShift

from datetime import datetime


class UpdateStr:
    def __init__(self, id_user, noi_dung, thoi_gian) -> None:
        self.id_user = id_user
        self.noi_dung = noi_dung
        self.thoi_gian = thoi_gian
    def __str__(self) -> str:
        return "UpdateStrObj(id_user={}, noi_dung={}, thoi_gian={})".format(self.id_user, self.noi_dung, self.thoi_gian)
d = datetime.now()
m = UpdateStr(1,"Mở trang học tiếng anh", "{}".format(d))
a = [m.__dict__, m.__dict__, m.__dict__, m.__dict__]
j = json.dumps(m.__dict__)
print(type(j))
print(j)

# jj = json.loads(j)

# for i in jj:
#     print(i)
#     print(type(i))