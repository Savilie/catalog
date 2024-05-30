from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    image = serializers.ImageField(allow_empty_file=False, allow_null=False)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        return instance
