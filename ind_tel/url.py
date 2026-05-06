from django.urls import path
from . import views

urlpatterns = [
    path('hyderabad/',views.hyderabad,name='hyderabad'),
    path('charminar/',views.charminar,name='charminar'),
]