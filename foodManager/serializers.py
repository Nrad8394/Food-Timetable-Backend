from rest_framework import serializers
from .models import Ingredient, Meal

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'description', 'price']

class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    class Meta:
        model = Meal
        fields = ['id', 'name', 'description', 'ingredients']

class MealCreateUpdateSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingredient.objects.all()
    )

    class Meta:
        model = Meal
        fields = ['id', 'name', 'description', 'ingredients']
