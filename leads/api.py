from rest_framework import viewsets, permissions
from .models import Lead
from .serializers import LeadSerialiaers

# LeadViewset

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerialiaers