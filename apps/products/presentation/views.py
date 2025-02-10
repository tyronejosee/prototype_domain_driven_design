from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.products.application.create_product import CreateProduct
from apps.products.application.update_price import UpdateProductPrice
from apps.products.infrastructure.product_repository import ProductRepository


class ProductAPIView(APIView):
    def get(self, request, product_id=None):
        repo = ProductRepository()

        if product_id:
            product = repo.get_by_id(product_id)
            return Response(
                {
                    "id": product.product_id.value,
                    "name": product.name,
                    "price": product.price,
                    "stock": product.stock,
                }
            )
        else:
            products = repo.get_all()
            return Response(
                [
                    {
                        "id": product.product_id.value,
                        "name": product.name,
                        "price": product.price,
                        "stock": product.stock,
                    }
                    for product in products
                ]
            )

    def post(self, request):
        repo = ProductRepository()
        use_case = CreateProduct(repo)
        product = use_case.execute(
            name=request.data["name"],
            price=request.data["price"],
            stock=request.data["stock"],
        )
        return Response(
            {
                "id": product.product_id.value,
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
            },
            status=status.HTTP_201_CREATED,
        )

    def put(self, request, product_id):
        repo = ProductRepository()
        use_case = UpdateProductPrice(repo)
        product = use_case.execute(
            product_id=product_id, new_price=request.data["price"]
        )
        return Response(
            {
                "id": product.product_id.value,
                "name": product.name,
                "price": product.price,
                "stock": product.stock,
            }
        )
