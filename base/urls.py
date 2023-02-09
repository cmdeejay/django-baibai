"""second URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('api/home',
         views.HomeListView.as_view({'get': 'list'}), name='home_api'),
    path('api/category/', views.CategoryListView.as_view(),
         name='category_post_api'),
    path('api/<slug:category_slug>/',
         views.MidCategoryListView.as_view(), name='mid_category_api'),
    path('api/<slug:category_slug>/<slug:mid_category_slug>/',
         views.BrandListView.as_view(), name='brand_api'),
    path('api/<slug:category_slug>/<slug:mid_category_slug>/<slug:brand_slug>/',
         views.ModelNumberListView.as_view(), name='model_number_api'),
    path('api/<slug:category_slug>/<slug:mid_category_slug>/<slug:brand_slug>/<slug:model_number_slug>',
         views.ProductListView.as_view(), name='product_list_api'),
    path('api/<slug:category_slug>/<slug:mid_category_slug>/<slug:brand_slug>/<slug:model_number_slug>/<int:id>',
         views.ProductsView.as_view(), name='single_product_api'),

]
