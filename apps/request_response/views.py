import json

from django import http
from django.shortcuts import render

# Create your views here.
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