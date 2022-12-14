from django.shortcuts import render
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import ElectricSerializer,ElectronicsSerializer
# Create your views here.
from .models import Electric,Electronics
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly

class ElectricListView(ListCreateAPIView):
    queryset=Electric.objects.all()
    serializer_class= ElectricSerializer
    # permission_classes=[IsOwnerOrReadOnly]

class ElectricDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Electric.objects.all()
    serializer_class= ElectricSerializer
    permission_classes=[IsOwnerOrReadOnly]



class ElectronicsListView(ListCreateAPIView):
    queryset=Electronics.objects.all()
    serializer_class= ElectronicsSerializer
    permission_classes=[AllowAny]


class ElectronicsDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Electronics.objects.all()
    serializer_class= ElectronicsSerializer
    permission_classes=[AllowAny]