from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hyderabad(request):
    return render(request,'hyderabad.html')
def charminar(request):
    response="<h1>Welcome to Charminar</h1>"
    return HttpResponse(response)