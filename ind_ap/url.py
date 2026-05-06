from django.urls import path
from . import views

urlpatterns = [
    path('chittoor/',views.chittoor,name='chittoor'),
    path('kadapa/',views.kadapa,name='kadapa'),
]