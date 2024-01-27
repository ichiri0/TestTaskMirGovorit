from django.contrib import admin
from .models import Product, Recipe, RecipeIngredient

admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
