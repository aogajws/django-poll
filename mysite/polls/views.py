from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
