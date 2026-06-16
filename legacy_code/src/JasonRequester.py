from legacy_code.src.Requester import Requester
import requests

class JasonRequester(Requester):
    def getShippingDataByID(self, order_id):
        url = f"https://codemanship.co.uk/api/orders.php?orderId={order_id}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        return data