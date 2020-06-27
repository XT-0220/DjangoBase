from django.shortcuts import render

# Create your views here.
from django import http
from django.views import View


class RegisterView(View):

    def get(self,request):

        return http.HttpResponse('注册')