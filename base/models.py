from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, default=1)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class MidCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, default=1)

    class Meta:
        verbose_name_plural = 'Mid Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Brands(models.Model):
    mid_category = models.ForeignKey(MidCategories, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, default=1)

    class Meta:
        verbose_name_plural = 'Brands'
        ordering = ['name']

    def __str__(self):
        return self.name

class ModelNumbers(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50, default=1)

    class Meta:
        verbose_name_plural = 'Models'
        ordering = ['name']

    def __str__(self):
        return self.name

class Products(models.Model):
    model_number = models.ForeignKey(ModelNumbers, on_delete=models.CASCADE, default=1)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, default=1)
    price = models.PositiveIntegerField()
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    descriptions = models.TextField(null=True, blank=True)
    
    class Color(models.TextChoices):
        黑色 = '黑色'
        白色 = '白色'
        金色 = '金色'
        银色 = '银色'
        其他 = '其他'

    class Useage(models.TextChoices):
        全新未拆封 = '全新未拆封'
        拆封九新 = '拆封九新' 
        经常使用 = '经常使用' 
        日常使用 = '日常使用'
    
    class Condition(models.TextChoices):
        全新 = '全新'
        有包装无磨损 = '有包装/无磨损'
        有包装轻微磨损 = '有包装/轻微磨损'
        无包装轻微磨损 =  '无包装/轻微磨损'
        无包装磨损较严重 =  '无包装/磨损较严重'

    class Age(models.TextChoices):
        三个月内 = '三个月内'
        六个月内 = '六个月内'
        一年以内 = '一年以内'
        两年以内 = '两年以内'
        两年以上 = '两年以上'
 
    color = models.CharField(max_length=4, choices=Color.choices, default='黑色')
    useage = models.CharField(max_length=10, choices=Useage.choices, default='全新未拆封')
    condition = models.CharField(max_length=20, choices=Condition.choices, default='全新')
    age = models.CharField(max_length=10, choices=Age.choices, default='三个月内')
    warranty = models.BooleanField()
    

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['created_date']

    def __str__(self):
        return self.name