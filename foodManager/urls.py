from django.urls import path, include
from rest_framework import routers
from .views import MealViewSet, IngredientViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'meal', MealViewSet, basename='meal')
router.register(r'ingredient', IngredientViewSet, basename='ingredient')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]