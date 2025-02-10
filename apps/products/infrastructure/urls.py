from django.urls import path

from apps.products.presentation.views import ProductAPIView


urlpatterns = [
    path(
        "products",
        ProductAPIView.as_view(),
    ),
    path(
        "products/<uuid:product_id>",
        ProductAPIView.as_view(),
    ),
]
