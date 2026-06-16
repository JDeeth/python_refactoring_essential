from abc import ABC

class Requester(ABC):
    def getShippingDataByID(self, order_id) -> dict:
        return {}
