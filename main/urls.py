from django.urls import path

from main.models import DonatedMeds
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('handlesignup', views.HandleSignUp, name="handlesignup"),
    path('signup', views.SignUp, name="signup"),
    path('handlelogin', views.HandleLogin, name="handlelogin"),
    path('login', views.Login, name="login"),
    path('logout', views.Logout, name="logout"),
    path('getmed', views.getmedtemplate, name="getmedtemplate"),
    path('getmedwork', views.getmed, name="getmedwork"),
    path('donate', views.donatetemplate, name="donatetemplate"),
    path('donatework', views.donatemed, name="donate"),
] 
