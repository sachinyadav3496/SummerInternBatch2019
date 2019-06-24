from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("hello/",views.hello,name="hello"),
    path("login/",views.login,name="login"),
    path("login1/",views.login1,name="lohin1"),
    path("signup/",views.signup,name="signup"),
    path("signup1/",views.Signedup.as_view(),name="signup1"),
    path("logout/",views.logout,name="logout"),
]