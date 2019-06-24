from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login,Signup
from django.views import View
from .models import AddUser
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
            try:
                u = AddUser.objects.get(Email=email)
            except AddUser.DoesNotExist as e:
                error = "No such user...signup to login"
                form = Signup()
                return render(request,"app1/signup.html",{'error':error,'form':form})
            else:
                password = form.cleaned_data['Password']
                p = u.Password
                if password == p:
                    request.session['email'] = email
                    request.session['password'] = p
                    return render(request,"app1/index1.html")
                    #return HttpResponse("<h1 style='color:red'>Welcome user {} with password {}".format(email,password))
                else:
                    error= "Password does not matched..."
                    form = Login()
                    return render(request,"app1/login.html",{'error':error,'form':form})
        else:
            error = "Form is not valid...Try again"
            form = Login()
            return render(request,"app1/login.html",{'error':error,'form':form})
    else:
        error = "Incorrect method used"
        form = Login()
        return render(request,"app1/login.html",{'error':error,'form':form})

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
            email = form.cleaned_data['Email']
            try:
                AddUser.objects.get(Email=email)
            except AddUser.DoesNotExist as e:
                pass1 = form.cleaned_data['Password']
                pass2 = form.cleaned_data['Confirm_password']
                if pass1 == pass2:
                    dict = {
                        'Email' : form.cleaned_data['Email'],
                        'Username' : form.cleaned_data['Username'],
                        'Password' : form.cleaned_data['Password'],
                        'Profile' : form.cleaned_data['Profile'],
                    }
                    new_user = AddUser.objects.create(**dict)
                    new_user.save()
                    return render(request,"app1/data.html",{'data':dict})
                else:
                    error = "Password does not match...Try again"
                    form = Signup()
                    return render(request,"app1/signup.html",{'form':form,'error':error})
            else:
                error = "Already this user exists..."
                form = Signup()
                return render(request,"app1/signup.html",{'error':error,'form':form})
                
        else:
            error = "Your form is invalid...try again"
            form = Signup()
            return render(request,"app1/signup.html",{'form':form,'error':error})


def logout(request):
    del request.session['email']
    del request.session['password']
    return render(request,"app1/index.html")