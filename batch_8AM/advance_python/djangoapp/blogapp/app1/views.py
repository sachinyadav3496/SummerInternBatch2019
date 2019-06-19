from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"app1/index.html")
    #return HttpResponse("<h1 style='color:blue'>Welcome to app1</h1>")
