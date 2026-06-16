from dataclasses import dataclass

from legacy_code.src.Requester import Requester

@dataclass(frozen=True)
class Order:
    orderId: int
    shippingType: str
    weightKg: float
    distanceKm: float
    fragile: bool


class ShippingCalculator:

    def __init__(self, _req: Requester):
        self.requester = _req

    def calculate_shipping(self, order_id: int) -> float:
        try:
            data = self.requester.getShippingDataByID(order_id)

            order = Order(
                orderId=data["orderId"],
                shippingType=data["shippingType"],
                weightKg=data["weightKg"],
                distanceKm=data["distanceKm"],
                fragile=data["fragile"]
            )

            if order.shippingType == "STANDARD":
                return order.weightKg * 0.5

            elif order.shippingType == "EXPRESS":
                return order.weightKg * 0.8 + order.distanceKm * 0.1

            elif order.shippingType == "OVERNIGHT":
                return order.weightKg * 1.2 + 25

            else:
                raise RuntimeError(f"Unknown shipping type: {order.shippingType}")

        except Exception as e:
            print(e)
            return -1.0