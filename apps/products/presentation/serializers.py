from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    price = serializers.FloatField()
    stock = serializers.IntegerField()
