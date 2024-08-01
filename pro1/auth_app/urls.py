from django.urls import path
from . views import *

urlpatterns = [
    path("suv/",signupview),
    path("lv/",loginview),
    path("lo/",logoutview)
]