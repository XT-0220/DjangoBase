from django.views import View
from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare1(MiddlewareMixin):


    def process_request(self,request):
        print('process_request1 被调用')
    def process_view(self,request,view_func,view_args,view_kwargs):
        print('process_view1 被调用')
    def process_response(self,request,response):
        return response

class TestMiddleWare2(MiddlewareMixin):

    def process_request(self,request):
        print('process_request2 被调用')
    def process_view(self,request,view_func,view_args,view_kwargs):
        print('process_view2 被调用')
    def process_response(self,request,response):
        return response
