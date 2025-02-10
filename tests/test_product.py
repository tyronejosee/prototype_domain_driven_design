from apps.products.domain.product import Product, ProductId


def test_product_creation():
    product = Product(
        product_id=ProductId(),
        name="Laptop",
        price=1000,
        stock=10,
    )
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.stock == 10


def test_update_price():
    product = Product(
        product_id=ProductId(),
        name="Laptop",
        price=1000,
        stock=10,
    )
    product.update_price(1200)
    assert product.price == 1200
