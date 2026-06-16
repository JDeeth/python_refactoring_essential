import sys

from legacy_code.src.ShippingCalculator import ShippingCalculator

from legacy_code.src.JasonRequester import JasonRequester

class ShippingApp:
    @staticmethod
    def main():
        if len(sys.argv) != 2:
            print("Usage: python shipping_app.py <orderId>")
            return

        try:
            order_id = int(sys.argv[1])

            jason_requester = JasonRequester()
            calculator = ShippingCalculator(jason_requester)
            cost = calculator.calculate_shipping(order_id)

            print(f"Order ID: {order_id}")
            print(f"Shipping cost: {cost}")

        except ValueError:
            print("orderId must be an integer")

        except Exception as e:
            print(f"Failed to calculate shipping for order {sys.argv[1]}")
            raise


if __name__ == "__main__":
    ShippingApp.main()