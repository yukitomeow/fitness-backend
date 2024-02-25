from django.contrib import admin
from .models import Meal, FoodItem, Nutrition

class MealAdminSettings(admin.ModelAdmin):
    list_display = ('pk', 'user','meal_type', 'created_at', 'hungry_when_eating', 'stop_eating_not_hungry')

class FoodItemAdminSettings(admin.ModelAdmin):
    list_display = ('pk', 'meal','name', 'nutrition')
    # actions = ['custom_task']
    # def custom_task(self, request, queryset):
    #     for food_item in queryset:
    #         print(food_item.name)
    #     self.message_user(request, f"Finished doing custom task on food items")
    # custom_task.short_description = "Do custom task"
   


class NutritionAdminSettings(admin.ModelAdmin):
    list_display = ('calories', 'protein','carbohydrates', 'fats')

# Register your models here.
admin.site.register(Meal, MealAdminSettings)
admin.site.register(FoodItem, FoodItemAdminSettings)
admin.site.register(Nutrition, NutritionAdminSettings)