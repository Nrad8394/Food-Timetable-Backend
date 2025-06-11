from django.db import models
from foodManager.models import Meal



class Timetable(models.Model):
    day_of_week_choices = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day_of_week = models.CharField(max_length=20, choices=day_of_week_choices)
    meal_type_choices = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]
    meal_type = models.CharField(max_length=20, choices=meal_type_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meals = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='timetables')
    class Meta:
        ordering = ['day_of_week', 'meal_type']
        verbose_name = 'Timetable'
        verbose_name_plural = 'Timetable'
        
    def __str__(self):
        return f"{self.day_of_week} - {self.meal_type} - {self.meals.name}"
   
