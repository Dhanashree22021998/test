from django.urls import path
from . views import *

urlpatterns = [
    path("av/",Addview.as_view(),name = "add"),
    path("sv/",Showview.as_view(),name = "show"),
    path("uv/<int:id>/",Updateview.as_view(),name = "update"),
    path("dv/<int:id>/",Deleteview.as_view(),name = "delete")

]