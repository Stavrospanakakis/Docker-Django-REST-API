from rest.models import Person
from rest_framework import viewsets, permissions
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ] 

    serializer_class = PersonSerializer