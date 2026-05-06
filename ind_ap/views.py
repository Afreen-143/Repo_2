from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Create your views here.
def chittoor(request):
    return render(request,'chittoor.html')
def kadapa(request):
    response="<h1>Welcome to Kadapa District</h1>"
    return HttpResponse(response)