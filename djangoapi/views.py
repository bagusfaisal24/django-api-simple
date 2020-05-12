from rest_framework import viewsets
from .serializers import BukuSerializer
from .models.Buku import Buku

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all().order_by('id')
    serializer_class = BukuSerializer