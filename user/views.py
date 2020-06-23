from django.shortcuts import render

# Create your views here.
from django import http

def register(request):

    return http.HttpResponse('注册')