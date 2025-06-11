from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='meals') # Many-to-many relationship with Ingredient

    def __str__(self):
        return self.name
