from datetime import datetime


class UpdateStr:
    def __init__(self, id_user, noi_dung, thoi_gian: datetime) -> None:
        self.id_user = id_user
        self.noi_dung = noi_dung
        self.thoi_gian = thoi_gian
    def __str__(self) -> str:
        return "UpdateStrObj(id_user={}, noi_dung={}, thoi_gian={})".format(self.id_user, self.noi_dung, self.thoi_gian)