from apps.products.domain.product import Product, ProductId
from apps.products.infrastructure.product_repository import ProductRepository


class CreateProduct:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, name: str, price: float, stock: int):
        product = Product(
            product_id=ProductId(),
            name=name,
            price=price,
            stock=stock,
        )
        self.repository.save(product)
        return product
