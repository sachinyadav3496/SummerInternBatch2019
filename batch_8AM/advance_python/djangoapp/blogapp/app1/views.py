from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from django.views import View
# Create your views here.
def index(request):
    return render(request,"app1/index.html")
    #return HttpResponse("<h1 style='color:blue'>Welcome to app1</h1>")

def hello(request):
    return HttpResponse("<h1 style='color:red'>Hello world</h1>")

def login(request):
    form = Login()
    return render(request,"app1/login.html",{'form':form})

def login1(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            #print(form)
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            return HttpResponse("<h1 style='color:red'>Welcome user {} with password {}".format(email,password))
        else:
            error = "Form is not valid...Try again"
            return render(request,"app1/login.html",{'error':error})
    else:
        error = "Incorrect method used"
        return render(request,"app1/login.html",{'error':error})

def signup(request):
    form = Signup()
    return render(request,"app1/signup.html",{'form':form})

class Signedup(View):
    def get(self,request):
        form = Signup()
        error = "Your method is incorrect..."
        return render(request,"app1/signup.html",{'form':form,'error':error})
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            pass1 = form.cleaned_data['Password']
            pass2 = form.cleaned_data['Confirm_password']
            if pass1 == pass2:
                dict = {
                    'username' : form.cleaned_data['Username'],
                    'email' : form.cleaned_data['Email'],
                    'password' : form.cleaned_data['Password'],
                    'profile' : form.cleaned_data['Profile'],
                }
                return render(request,"app1/data.html",{'data':dict})
            else:
                error = "Password does not match...Try again"
                form = Signup()
                return render(request,"app1/signup.html",{'form':form,'error':error})
        else:
            error = "Your form is invalid...try again"
            form = Signup()
            return render(request,"app1/signup.html",{'form':form,'error':error})
