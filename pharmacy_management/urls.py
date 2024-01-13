from django.urls import path,register_converter
from . import views
# import dateconverter  
# import datetime

# register_converter(dateconverter.DateConverter, 'date')

urlpatterns = [
    path('customer/<int:pk>/', views.customer),
    path('medicine/<str:med>/', views.medicine),
    path('get_date/<str:date_t>/', views.get_date),
]