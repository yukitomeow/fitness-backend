from django.urls import path
from .api import MealListCreateView, MealDetailView, FoodItemDetailView, FoodItemListCreateView, NutritionDetailView, NutritionListCreateView

urlpatterns = [
   path('meal/', MealListCreateView.as_view(), name='meal-list'),
   path('meal/<int:pk>/', MealDetailView.as_view(), name='meal-detail'),
   path('food-item/', FoodItemListCreateView.as_view(), name='food-item-list'),
   path('food-item/<int:pk>/', FoodItemDetailView.as_view(), name='food-item-detail'),
   path('nutrition/', NutritionListCreateView.as_view(), name='nutrition-list'),
   path('nutrition/<int:pk>/', NutritionDetailView.as_view(), name='nutrition-detail'),
]