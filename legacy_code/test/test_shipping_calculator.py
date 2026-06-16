import json

from legacy_code.src.Requester import Requester
from legacy_code.src.ShippingCalculator import ShippingCalculator

class MockRequester(Requester): 
    def getShippingDataByID(self, order_id) -> dict:
        match order_id:
            case 1001: 
                return json.loads("""{"orderId":1001,"shippingType":"STANDARD","weightKg":5,"distanceKm":120,"fragile":false}""")

def test_calculate_shipping():
    calc = ShippingCalculator(MockRequester())

    assert calc.calculate_shipping(1001) == 2.5

