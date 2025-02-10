from django.db import models

from apps.products.domain.product import ProductId


class ProductModel(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=36,
        default=str(ProductId()),
        editable=False,
    )
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(ProductId())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
