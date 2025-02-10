from django.contrib import admin

from apps.products.application.create_product import CreateProduct
from apps.products.infrastructure.product_model import ProductModel
from apps.products.infrastructure.product_repository import ProductRepository


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "stock"]
    search_fields = ["name"]
    list_filter = ["price"]
    ordering = ["-price"]
    fields = ["name", "price", "stock"]

    def save_model(self, request, obj, form, change):
        if not obj.id:
            create_product = CreateProduct(ProductRepository())
            create_product.execute(
                name=obj.name,
                price=obj.price,
                stock=obj.stock,
            )
        super().save_model(request, obj, form, change)
