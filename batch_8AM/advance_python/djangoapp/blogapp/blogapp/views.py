from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world welcome to my first project <a href='/app1/'>APP1</a>d")

def hello(request):
    return HttpResponse("<h1 style='color:blue;font-size:40px;'>Hey hello world</h1>")

def marks(request,user,value):
    return HttpResponse("<h1 style='color:coral'>Marks for {} is {}".format(user,value))
