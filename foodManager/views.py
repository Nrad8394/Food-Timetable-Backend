from rest_framework import viewsets
from .models import Meal, Ingredient
from .serializers import IngredientSerializer, MealSerializer
from typing import Type

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    search_fields = ['name']
    filterset_fields = ['name']
    ordering_fields = ['name']

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    search_fields = ['name', 'description']
    filterset_fields = ['name', 'description', 'ingredients']
    ordering_fields = ['name','description', 'ingredients']
    
    def get_serializer_class(self) -> type:
        if self.action in ['create', 'update', 'partial_update']:
            from .serializers import MealCreateUpdateSerializer
            return MealCreateUpdateSerializer
        return super().get_serializer_class()
