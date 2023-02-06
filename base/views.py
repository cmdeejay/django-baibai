from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
from django.db.models import Count
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import *
from collections import namedtuple
# Create your views here.
Home = namedtuple('Home', ('category', 'mid_category', 'product'))


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerilizer

    def get_queryset(self):
        if (self.kwargs['brand_slug'] == Products.objects.filter(brand__slug=self.kwargs['brand_slug'])[0].brand.slug) and \
                (self.kwargs['mid_category_slug'] == Products.objects.filter(brand__slug=self.kwargs['brand_slug'])[0].brand.mid_category.slug) and \
                (self.kwargs['category_slug'] == Products.objects.filter(brand__slug=self.kwargs['brand_slug'])[0].brand.mid_category.category.slug):
            return Products.objects.filter(model_number__slug=self.kwargs['model_number_slug'])


class HomeListView(viewsets.ViewSet):

    def list(self, request):
        home = Home(
            category=Categories.objects.all(),
            mid_category=MidCategories.objects.all(),
            product=Products.objects.all()
        )
        serializer_class = HomeSerilizer(home)
        return Response(serializer_class.data)


class MidCategoryListView(generics.ListAPIView):
    serializer_class = MidCategorySerilizer

    def get_queryset(self):
        if (self.kwargs['category_slug'] == MidCategories.objects.filter(category__slug=self.kwargs['category_slug'])[0].category.slug):
            return MidCategories.objects.filter(category__slug=self.kwargs['category_slug'])


class BrandListView(generics.ListAPIView):
    serializer_class = BrandSerilizer

    def get_queryset(self):
        if (self.kwargs['category_slug'] == Brands.objects.filter(mid_category__slug=self.kwargs['mid_category_slug'])[0].mid_category.category.slug) and \
                (self.kwargs['mid_category_slug'] == Brands.objects.filter(mid_category__slug=self.kwargs['mid_category_slug'])[0].mid_category.slug):
            return Brands.objects.filter(mid_category__slug=self.kwargs['mid_category_slug'])


class ModelNumberListView(generics.ListAPIView):
    serializer_class = ModelNumberSerilizer

    def get_queryset(self):
        if (self.kwargs['category_slug'] == ModelNumbers.objects.filter(brand__slug=self.kwargs['brand_slug'])[0].brand.mid_category.category.slug) and \
            (self.kwargs['mid_category_slug'] == ModelNumbers.objects.filter(brand__slug=self.kwargs['brand_slug'])[0].brand.mid_category.slug) and \
                (self.kwargs['brand_slug'] == ModelNumbers.objects.filter(brand__slug=self.kwargs['brand_slug'])[0].brand.slug):
            return ModelNumbers.objects.filter(brand__slug=self.kwargs['brand_slug'])


class ProductsView(generics.ListAPIView):
    serializer_class = ProductSerilizer

    def get_queryset(self):
        if (self.kwargs['model_number_slug'] == Products.objects.filter(id=self.kwargs['id'])[0].model_number.slug) and \
            (self.kwargs['brand_slug'] == Products.objects.filter(id=self.kwargs['id'])[0].model_number.brand.slug) and \
            (self.kwargs['mid_category_slug'] == Products.objects.filter(id=self.kwargs['id'])[0].model_number.brand.mid_category.slug) and \
                (self.kwargs['category_slug'] == Products.objects.filter(id=self.kwargs['id'])[0].model_number.brand.mid_category.category.slug):
            return Products.objects.filter(id=self.kwargs['id'])
