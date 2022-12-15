from django.contrib import admin
from .models import Topping, FoodCategory, Food

admin.site.register(Topping)
admin.site.register(FoodCategory)
admin.site.register(Food)
