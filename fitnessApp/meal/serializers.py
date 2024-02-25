from rest_framework import serializers
from .models import Meal, FoodItem, Nutrition

class NutritionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nutrition 
        fields = ["id","calories", "protein", "carbohydrates", "fats"] 


class FoodItemSerializer(serializers.ModelSerializer):
    # nutrition = NutritionSerializer(many=False, read_only=True)

    class Meta:
        model = FoodItem
        fields = ["id","meal", "name", "nutrition"]

class MealSerializer(serializers.ModelSerializer):
    # food_item = FoodItemSerializer(many=True, read_only=True)
    class Meta:
        model = Meal
        fields = ["id","user", "created_at", "meal_type", "hungry_when_eating", "stop_eating_not_hungry", "food_item"]






