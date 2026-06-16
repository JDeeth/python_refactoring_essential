import json

import pytest

from legacy_code.src.Requester import Requester
from legacy_code.src.ShippingCalculator import ShippingCalculator


class MockRequester(Requester):
    def getShippingDataByID(self, order_id) -> dict:
        match order_id:
            case 1001:
                return json.loads(
                    """{"orderId":1001,"shippingType":"STANDARD","weightKg":5,"distanceKm":120,"fragile":false}"""
                )
            case 1002:
                return json.loads(
                    """{"orderId":1002,"shippingType":"EXPRESS","weightKg":8.5,"distanceKm":300,"fragile":true}"""
                )
            case 1003:
                return json.loads(
                    """{"orderId":1003,"shippingType":"OVERNIGHT","weightKg":2,"distanceKm":50,"fragile":false}"""
                )
            case 1004:
                return json.loads(
                    """{"orderId":1004,"shippingType":"INTERNATIONAL","weightKg":10,"distanceKm":50,"fragile":false}"""
                )


@pytest.mark.parametrize(
    "order_id,expected",
    [
        (1001, 2.5),
        (1002, 36.8),
        (1003, 27.4),
        pytest.param(1004, 15, marks=pytest.mark.xfail(reason="Not implemented yet")),
    ],
)
def test_calculate_shipping(order_id, expected):
    calc = ShippingCalculator(MockRequester())

    assert calc.calculate_shipping(order_id) == expected
