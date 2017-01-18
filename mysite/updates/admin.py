from django.contrib import admin

# Register your models here.
from .models import Update, UpdateImage, Review

admin.site.register(Update)
admin.site.register(Review)
admin.site.register(UpdateImage)