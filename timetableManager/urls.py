from django.urls import path, include
from rest_framework import routers
from .views import TimetableViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# Register the TimetableViewSet with the router.
router.register(r'timetable', TimetableViewSet, basename='timetable')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]