from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE_CHOICES=[
    ("BR", "Breakfast"),
    ("MO","Morning Snack"),
    ("LU", "Lunch"),
    ("AF","Afternoon Snack"),
    ("DI", "Dinner"),
    ("EV","Evening Snack")
]
# Create your models here.
class Meal(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPE_CHOICES, null=True)
    hungry_when_eating= models.BooleanField(default=False) #Did you start eating when you feel hungry? "Y"/"N"
    stop_eating_not_hungry= models.BooleanField(default=False)# Did you finish eating when you feel not hungry ? "Y"/"N"

    def __str__(self):
        return self.meal_type
    
class FoodItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name= "food_item")
    name =models.CharField(max_length=100)
    nutrition = models.ForeignKey("Nutrition", on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name
    
class Nutrition(models.Model):
    calories = models.IntegerField(null=True, blank=True)
    protein =models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
    carbohydrates= models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
    fats= models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)