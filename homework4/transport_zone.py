class TransportZone:
    def __init__(self, id: int, remark: str):
        self.id = id
        self.remark = remark

    def get_id(self):
        return self.id

    def get_remark(self):
        return self.remark

    def set_remark(self, remark: str):
        self.remark = remark
