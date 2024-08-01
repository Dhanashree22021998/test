
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("a1/",include("app1.urls")),
    path("a2/",include("auth_app.urls"))
]
