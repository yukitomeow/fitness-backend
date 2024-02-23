from django.contrib import admin
from .models import Meal, FoodItem, Nutrition

class MealAdminSettings(admin.ModelAdmin):
    list_display = ('pk', 'user','meal_type', 'created_at', 'hungry_when_eating', 'stop_eating_not_hungry')

class FoodItemAdminSettings(admin.ModelAdmin):
    list_display = ('pk', 'meal','name', 'nutrition')

class NutritionAdminSettings(admin.ModelAdmin):
    list_display = ('calories', 'protein','carbohydrates', 'fats')

# Register your models here.
admin.site.register(Meal, MealAdminSettings)
admin.site.register(FoodItem, FoodItemAdminSettings)
admin.site.register(Nutrition, NutritionAdminSettings)