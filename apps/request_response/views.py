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
    def get(self):

        return http.HttpResponse()