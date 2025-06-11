from rest_framework import viewsets
from .models import Timetable
from .serializers import TimetableSerializer
from .tasks import print_timetable

class TimetableViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Timetable instances.
    """
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    
    