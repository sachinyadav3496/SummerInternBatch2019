from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world <a href=/app1/>APP1</a>")

def home(request,user):
    return HttpResponse("<h1 style='color:red;font-size:30px'>Welcome to my first project {}".format(user))