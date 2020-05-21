from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.

def homepage(request,*args, **kwargs):
   # return HttpResponse("<h1>hello</h1>")
   return render(request, "home.html")


def yt(request,*args, **kwargs):
   # return HttpResponse("<h1>hello</h1>")
   return render(request, "yt.html")
