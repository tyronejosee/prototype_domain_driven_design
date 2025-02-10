import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class ProductId:
    value: str

    def __init__(self, value=None):
        if value is None:
            value = str(uuid.uuid4())
        object.__setattr__(self, "value", value)

    def __str__(self) -> str:
        return self.value


class Product:
    def __init__(
        self,
        product_id: ProductId,
        name: str,
        price: float,
        stock: int,
    ):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price: float):
        if new_price <= 0:
            raise ValueError("Price must be greater than zero")
        self.price = new_price

    def decrease_stock(self, quantity: int):
        if quantity > self.stock:
            raise ValueError("Not enough stock available")
        self.stock -= quantity
