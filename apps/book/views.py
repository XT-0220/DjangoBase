from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View

from book.models import BookInfo, HeroInfo


class AddView(View):
    def get(self,request):

        # 1.save()
        # book = BookInfo()
        #
        # book.btitle = 'MANYMAN'
        # book.bcomment = 20
        # book.bpub_date = '2020-6-29'
        # book.bread = 33
        #
        # book.save()

        # 2.create() 模型类.objects.create()

        # BookInfo.objects.create(
        #     btitle = 'MANYMALE',
        #     bcomment = 20,
        #     bread = 55,
        #     bpub_date = '2020-6-29'
        #
        # )


        # 3.save()修改
        # book = BookInfo.objects.get(btitle = 'MANYMALE')
        # book.btitle = 'manymale'
        # book.save()


        # 4.update()  模型类.objects.filter().update()
        # BookInfo.objects.filter(btitle = 'MANYMAN').update(btitle='manyman')





        return http.HttpResponse('增删改查-增')