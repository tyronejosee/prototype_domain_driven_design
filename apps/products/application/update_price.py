from apps.products.infrastructure.product_repository import ProductRepository


class UpdateProductPrice:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, product_id: str, new_price: float):
        product = self.repository.get_by_id(product_id)
        product.update_price(new_price)
        self.repository.save(product)
        return product
