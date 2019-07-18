from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from django.views import View
from .models import AddUser
# Create your views here.
def index(request):
    return render(request,"app1/header.html")
    #return HttpResponse("<h1 style='color:red'>Welcome to my app1</h1>")

def home(request):
    return render(request,"app1/index.html")

def login(request):
    if request.session.get('email'):
        error = "Already logged in"
        return render(request,"app1/afterlogin.html",{'error':error})
    else:
        form = Login()
        return render(request,"app1/login.html",{'form':form})

def signup(request):
    form = Signup()
    return render(request,"app1/signup.html",{'form':form})


class Signnedup(View):
    def get(self,request):
        error = "Invalid method"
        form = Signup()
        return render(request,"app1/signup.html",{'form':form,'error':error})
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            mail = form.cleaned_data['email']
            try:
                AddUser.objects.get(email=mail)
            except AddUser.DoesNotExist as e:
                p1 = form.cleaned_data['password']
                p2 = form.cleaned_data['confirm_password']
                if p1 == p2:
                    dict = {
                    'username' : form.cleaned_data['username'],
                    'email' : form.cleaned_data['email'],
                    'password':form.cleaned_data['password'],
                    'pic' : form.cleaned_data['pic'],

                    }
                    new_user = AddUser.objects.create(**dict)
                    new_user.save()
                    return render(request,"app1/data.html",{'dict':dict})
                else:
                    error = "Password does not match...Try again"
                    form = Signup()
                    return render(request,"app1/signup.html",{'form':form,'error':error})
            else:
                error = "User already exist..."
                form = Signup()
                return render(request,"app1/signup.html",{'form':form,'error':error})

        else:
                error = "Invalid Form"
                form = Signup()
                return render(request,"app1/signup.html",{'form':form,'error':error})

def login1(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = AddUser.objects.get(email=email)
            if password == user.password:
                request.session['email'] = email
                return render(request,"app1/afterlogin.html")
                #return HttpResponse("success")
            else:
                error = "Password does not match.."
                form = Login()
                return render(request,"app1/login.html",{'form':form,'error':error})
        
        else:
            error = "invalid form"
            form = Login()
            return render(request,"app1/login.html",{'error':error,'form':form})
    else:
        error = "invalid method"
        form = Login()
        return render(request,"app1/login.html",{'error':error,'form':form})        


def logout(request):
    del request.session['email']
    return render(request,"app1/header.html")