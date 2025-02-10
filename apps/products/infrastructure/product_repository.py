from apps.products.domain.product import Product, ProductId
from apps.products.infrastructure.product_model import ProductModel


class ProductRepository:
    def get_all(self):
        product_models = ProductModel.objects.all()
        return [
            Product(
                product_id=ProductId(product_model.id),
                name=product_model.name,
                price=product_model.price,
                stock=product_model.stock,
            )
            for product_model in product_models
        ]

    def save(self, product: Product):
        ProductModel.objects.update_or_create(
            id=product.product_id.value,
            defaults={
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
            },
        )

    def get_by_id(self, product_id: str) -> Product:
        product_model = ProductModel.objects.get(id=product_id)
        return Product(
            product_id=ProductId(product_model.id),
            name=product_model.name,
            price=product_model.price,
            stock=product_model.stock,
        )
