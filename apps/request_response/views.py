import json

from django import http
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View


class QueryStrView(View):
    def get(self,request):
        name = request.GET.get('name','xt')
        age = request.GET.get('age',20)

        return http.HttpResponse('查询的字符串：%s--%s' % (name,age))

# 表单类型请求体数据(Form Data)
class FormDataView(View):

    def post(self,request):

        username = request.POST.get('username')
        password = request.POST.get('password')

        return http.HttpResponse('表单数据：%s-%s' % (username,password ))

# 非表单类型请求体数据(Non-Form Data)：JSON
# 非表单类型的请求体数据，Django无法自动解析，可以通过request.body属性获取最原始的请求体数据
# 然后自己按照具体请求体原始数据的格式（JSON等）进行解析
# request.body获取的是bytes类型的请求体原始数据

class JsonDataView(View):

    def post(self,request):

        json_str = request.body
        json_dict = json.loads(json_str)

        username = request.POST.get('username')
        password = request.POST.get('password')

        return http.HttpResponse('json数据：%s--%s' % (username,password))



# HttpResponse

class Response1View(View):
    """测试HttpResponse
    http://127.0.0.1:8000/response1/
    """

    def get(self, request):
        # 使用HttpResponse构造响应数据
        # return http.HttpResponse(content='itcast python', status=200)
        # 可简写
        # return http.HttpResponse('itcast python')

        # 另外一种写法
        response = http.HttpResponse('itcast python')
        return response

# JsonResponse：响应JSON
class JsonResponseView(View):

    def get(self,request):

        dist_data = {
            'username': 'xt',
            'age': 20
        }
        return http.JsonResponse(dist_data)


# redirect()：重定向

class RedirectView(View):


    def get(self,request):

        return http.HttpResponse('重定向')


class TestRedirectView(View):

    def post(self,request):

        return redirect('/redirect/')


# reverse()：重定向反向解析

class RedirectView1(View):


    def get(self,request):

        return http.HttpResponse('重定向1')


class TestRedirectView1(View):

    def post(self,request):

        # 将用户通过重定向引导到首页
        # return redirect('/index/')

        # ret_url = reverse('总路由别名:子路由别名')

        red = reverse('request_response1:redirect')

        return redirect(red)