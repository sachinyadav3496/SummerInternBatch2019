from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("addblog/",views.addblog,name="addblog"),
    path("postblog/",views.Blogpost.as_view(),name="postblog"),
]