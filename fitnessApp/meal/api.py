from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Meal, FoodItem, Nutrition
from .serializers import MealSerializer, FoodItemSerializer, NutritionSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


# This was views.py Instead of view set

class MealListCreateView(ListCreateAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
class MealDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class FoodItemListCreateView(ListCreateAPIView):
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()
    permission_classes = [IsAuthenticated]

class FoodItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()
    permission_classes = [IsAuthenticated]

class NutritionListCreateView(ListCreateAPIView):
    serializer_class = NutritionSerializer
    queryset = Nutrition.objects.all()
    permission_classes = [IsAuthenticated ]

class NutritionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = NutritionSerializer
    queryset = Nutrition.objects.all()
    permission_classes = [IsAuthenticated ]