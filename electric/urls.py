from django.urls import path
from .views import ElectricListView,ElectricDetailView,ElectronicsListView,ElectronicsDetailView
urlpatterns = [
   path('electric/', ElectricListView.as_view(), name='electric_list'),
   path('electric/<int:pk>', ElectricDetailView.as_view(),name='electric_detail'),
   path('electronics/', ElectronicsListView.as_view(), name='electronics_list'),
   path('electronics/<int:pk>', ElectronicsDetailView.as_view(),name='electronics_detail')
]