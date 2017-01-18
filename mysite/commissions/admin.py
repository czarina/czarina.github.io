from django.contrib import admin

# Register your models here.

from .models import Product, Category, Tag, ProductVariant, Fandom, ProductAddOn

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Fandom)
admin.site.register(Tag)
admin.site.register(ProductAddOn)
admin.site.register(ProductVariant)
