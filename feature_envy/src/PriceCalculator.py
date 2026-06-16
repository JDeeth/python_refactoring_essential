from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    _price: float
    _on_sale: bool

    def final_price(self) -> float:
        price = self._price

        if self._on_sale:
            price *= 0.8

        return price

class PriceCalculator:
    def calculate_final_price(self, product: Product) -> float:
        return product.final_price()
