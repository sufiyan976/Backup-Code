from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    path('logout/', views.logoutUser),
    path('login/', views.loginUSER),
    path('home/', views.home),
    path('women/', views.women),
    path('men/', views.men),
    path('kid/', views.kid),
    path('contact/', views.contact),
    path('about/', views.about),
    path('service/', views.service),
    path('help/', views.help),
    path('settings/', views.settings),
    path('accessories/', views.accessories)
]