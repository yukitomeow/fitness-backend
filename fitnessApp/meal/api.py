from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Meal, FoodItem, Nutrition
from .serializers import MealSerializer, FoodItemSerializer, NutritionSerializer
# This was views.py Instead of view set

class MealListCreateView(ListCreateAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

class MealDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

class FoodItemListCreateView(ListCreateAPIView):
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()

class FoodItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()

class NutritionListCreateView(ListCreateAPIView):
    serializer_class = NutritionSerializer
    queryset = Nutrition.objects.all()

class NutritionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = NutritionSerializer
    queryset = Nutrition.objects.all()