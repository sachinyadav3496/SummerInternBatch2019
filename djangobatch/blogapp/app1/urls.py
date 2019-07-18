from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('home/',views.home),
    path('login/',views.login),
    path('signup/',views.signup),
    path('signup1/',views.Signnedup.as_view()),
    path('login1/',views.login1),
    path('logout/',views.logout),
]