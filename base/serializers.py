from rest_framework import serializers, permissions
from .models import *


class ProductSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class ProductListSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['name']


class CategorySerilizer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class MidCategorySerilizer(serializers.ModelSerializer):

    class Meta:
        model = MidCategories
        fields = '__all__'


class BrandSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Brands
        fields = '__all__'


class ModelNumberSerilizer(serializers.ModelSerializer):

    class Meta:
        model = ModelNumbers
        fields = '__all__'


class HomeSerilizer(serializers.Serializer):
    category = CategorySerilizer(many=True)
    mid_category = MidCategorySerilizer(many=True)
    product = ProductListSerilizer(many=True)
