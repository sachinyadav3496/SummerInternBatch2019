from django.shortcuts import render
from django.http import HttpResponse
from .forms import Blog
from django.views import View
from .models import AddBlog
from app1.models import AddUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddBlogSerializer
# Create your views here.
def index(request):
    return HttpResponse("<h1 style='color:red'>This is blog app</h1>")

def addblog(request):
    form = Blog()
    return render(request,"blog/blog.html",{'form':form})

class Blogpost(View):
    def get(self,request):
        error = "Invalid method"
        form = Blog()
        return render(request,"blog/blog.html",{'form':form,'error':error})
    def post(self,request):
        form = Blog(request.POST)
        if form.is_valid():
            data = {
            'author' : AddUser.objects.get(Email=request.session.get('email')),
            'title' : form.cleaned_data['title'],
            'post' : form.cleaned_data['post'],
            'date' : form.cleaned_data['date'],
            }
            new_blog = AddBlog.objects.create(**data)
            new_blog.save()
            return render(request,"app1/index1.html")

        else:
            error = "Your form is not valid..."
            form = Blog()
            return render(request,"blog/blog.html",{'form':form,'error':error})

def showblog(request):
    blogs = AddBlog.objects.all()
    print(blogs)
    data = []
    for var in blogs:
        dict = {
            'title' : var.title,
            'post' : var.post,
            'author' : var.author.Username,
        }
        data.append(dict)
    return render(request,"blog/blogfeed.html",{'data':data})
    #return HttpResponse("SUCCESS")

class Blogapi(APIView):
    def get(self,request):
        blog = AddBlog.objects.all()
        serializer = AddBlogSerializer(blog,many=True)
        return Response(serializer.data)