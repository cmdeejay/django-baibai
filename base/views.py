from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count

# Create your views here.
def home(request):
    categories = Categories.objects.all()
    mid_categories = MidCategories.objects.all().annotate(total=Count('id')).order_by('total')
    products = Products.objects.all().order_by('created_date')[:4]
    context = {'categories': categories, 
               'mid_categories': mid_categories,
               'products': products,
    }
    return render(request, 'home.html', context)

def category(request, category_slug):
    try:
        Categories.objects.get(slug=category_slug).slug
        mid_categories = MidCategories.objects.filter(category__slug__icontains=category_slug)
        context = {'mid_categories': mid_categories}
        return render(request, 'category.html', context)
    except:
        return redirect('home')

def mid_category(request, category_slug, mid_category_slug):
    try:
        matching_mid_category_slug = MidCategories.objects.get(slug=mid_category_slug).slug
        matching_category_slug = Categories.objects.get(slug=category_slug).slug
        brands = Brands.objects.filter(mid_category__slug__icontains=mid_category_slug)
        context = {'brands': brands,
                'mid_category_slug': matching_mid_category_slug,
                'category_slug': matching_category_slug
        }
        return render(request, 'mid_category.html', context)
    except:
        return redirect('home')
    
def brand(request, category_slug, mid_category_slug, brand_slug):
    try: 
        matching_mid_category_slug = MidCategories.objects.get(slug=mid_category_slug).slug
        matching_category_slug = Categories.objects.get(slug=category_slug).slug
        matching_brand_slug = Brands.objects.get(slug=brand_slug).slug
        models= ModelNumbers.objects.filter(brand__slug__icontains=brand_slug)
        context = {'models': models,
                   'mid_category_slug': matching_mid_category_slug,
                   'category_slug': matching_category_slug,
                   'brand_slug': matching_brand_slug
        }
        return render(request, 'brand.html', context)
    except:
        return redirect('home')

def model(request, category_slug, mid_category_slug, brand_slug, model_slug):
    try: 
        matching_mid_category_slug = MidCategories.objects.get(slug=mid_category_slug).slug
        matching_category_slug = Categories.objects.get(slug=category_slug).slug
        matching_brand_slug = Brands.objects.get(slug=brand_slug).slug
        matching_model_slug = ModelNumbers.objects.get(slug=model_slug).slug
        models= ModelNumbers.objects.filter(brand__slug__icontains=brand_slug)
        products = Products.objects.filter(model_number__slug__icontains=model_slug)
        context = {'models': models,
                   'products': products,
                   'mid_category_slug': matching_mid_category_slug,
                   'category_slug': matching_category_slug,
                   'brand_slug': matching_brand_slug,
                   'model_slug': matching_model_slug
        }
        return render(request, 'model.html', context)
    except:
        return redirect('home')

def product(request, category_slug, mid_category_slug, brand_slug, model_slug, name):
    try:
        matching_mid_category_slug = MidCategories.objects.get(slug=mid_category_slug).slug
        matching_category_slug = Categories.objects.get(slug=category_slug).slug
        matching_brand_slug = Brands.objects.get(slug=brand_slug).slug
        matching_model_slug = ModelNumbers.objects.get(slug=model_slug)

        models= ModelNumbers.objects.filter(brand__slug__icontains=brand_slug)
        product = Products.objects.get(name=name)

        context = {'models': models,
                   'product': product,
                   'mid_category_slug': matching_mid_category_slug,
                   'category_slug': matching_category_slug,
                   'brand_slug': matching_brand_slug,
                   'model_slug': matching_model_slug,
        }
        return render(request, 'product.html', context)
    except:
        return redirect('home')