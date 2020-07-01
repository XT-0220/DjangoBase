from django import http
from django.db.models import F, Q, Sum
from django.shortcuts import render

# Create your views here.
from django.views import View

from book.models import BookInfo, HeroInfo


class AddView(View):
    def get(self,request):

        # 1.save()
        # book = BookInfo()
        #
        # book.btitle = '1'
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

        # return http.HttpResponse('增删改查-增')



        # 5. 模型类对象delete
        # book = BookInfo.objects.filter(btitle = 'manyman')
        # book.delete()

        # 6.is_delete()
        book = BookInfo.objects.get(id=9)
        book.is_delete = True
        book.save()


        return http.HttpResponse('增删改查-删')


class QueryView(View):

    def get(self,request):


        ################### 基本查询 #################
        # 1.get()单一查询
        # book = BookInfo.objects.get(id = 9)
        # print(book)

        # 2. 查询表中所有记录
        # book = BookInfo.objects.all()
        # print(book)

        # 3. 查询记录的个数：查询表中所有记录的个数
        # book = BookInfo.objects.all().count()
        # print(book)

        # 4.查询记录的个数：查询满足条件记录个数，查询未被逻辑删除的记录的个数
        # book = BookInfo.objects.filter(is_delete = True).count()
        # print(book)


        ################### 过滤查询 #################
        # 过滤查询的语法：模型类.objects.filter(属性__条件表达式=值)
        # 1.查询书名为'天龙八部'的书籍 (相等)
        # book = BookInfo.objects.filter(btitle__exact = '天龙八部')
        # 判断相等的表达式可以简写的，而且是唯一可以简写的条件表达式
        # book = BookInfo.objects.filter(btitle='天龙八部')
        # print(book)

        # 2.查询书名包含'湖'的书籍 (模糊查询)
        # 原生SQL伪代码:select * from tb_bookinfo where btitle like %湖%
        # book = BookInfo.objects.filter(btitle__contains = '湖')
        # print(book)

        # 3.查询书名以'部'结尾的书籍 (模糊查询) (endswith、startswith)
        # 原生SQL伪代码:select * from tb_bookinfo where btitle like %部
        # book = BookInfo.objects.filter(btitle__endswith = '部')
        # print(book)
        # 4.查询书名不为空的书籍 (空查询)，特别特别容易出错
        # book = BookInfo.objects.filter(btitle__isnull = False)
        # print(book)

        # 5.查询编号为1或3或5的书籍 (范围查询)，特别容易误解
        # book = BookInfo.objects.filter(id__in = [1,3,7])
        # 查询编号为1或5的书籍 (范围查询)
        # book = BookInfo.objects.filter(id__in = [1,5])
        # print(book)


        # 6.查询编号大于3的书籍 (比较查询)
        # gt 大于 (greater than)
        # gte 大于等于 (greater than equal)
        # lt 小于 (less than)
        # lte 小于等于 (less than equal)
        # book = BookInfo.objects.filter(id__gt = 5)
        # print(book)
        # 7. 查询id不等于3的书籍 (不相等)
        # exclude():跟filter一样的，也是一种过滤查询
        # exclude()：查询指定的条件以外的数据
        # filter()：查询满足指定条件的数据
        # books = BookInfo.objects.exclude(id=3)
        # print(books)

        # 8.查询1990年1月1日后发表的书籍
        # books = BookInfo.objects.filter(bpub_date__gt='1990-1-1')
        #
        # from datetime import date
        # books = BookInfo.objects.filter(bpub_date__gt=date(1990,1,1))
        # print(books)

        ################### F和Q查询 #################
        # F查询
        # 1.查询阅读量大于评论量的书籍
        # book = BookInfo.objects.filter(bread__gt = F('bcomment'))
        # print(book)



        # Q查询：逻辑或、逻辑非
        # 先演示逻辑与：查询阅读量大于10，并且发布时间在1980年1月1号之后
        # book = BookInfo.objects.filter(bread__gt = 10 , bpub_date__gt = '1980-1-1')
        # print(book)

        # Q查询：逻辑或，给N个条件，只有有其中任何一个是满足的，都会被找到
        # 1.查询阅读量大于20，或编号小于3的图书
        # book = BookInfo.objects.filter(Q(bread__gt = 20) | Q(id__lt = 3))
        # print(book)



        ################### 一对多关联查询 #################
        # 1.一查多：查询编号为1的图书中所有人物信息
        # # 先查询出一方模型对象
        # book = BookInfo.objects.get(id = 1)


        # 再使用一方模型对象调用关联的多方模型类名小写_set  (固定的语法)
        # hero = book.heroinfo_set.all()
        # print(hero)

        # 2.多查一：查询编号为1的英雄出自的书籍
        # 先查询出多方模型对象
        hero = HeroInfo.objects.get(id=1)
        # 在使用多方模型对象调用多方模型类中的关联的外键属性名 (固定的语法)
        book = hero.hbook
        print(book)


        ################### 排序查询 #################
        # 正序（默认）模型类.objects.filter('条件').order_by('模型属性')
        # 倒序：模型类.objects.filter('条件').order_by('-模型属性')

        # 查询书名不为空的图书，并且按照阅读量正序
        # 正序：升序，有小到大
        # book = BookInfo.objects.filter(btitle__isnull = False).order_by('bread')

        # 查询书名不为空的图书，并且按照阅读量倒序
        # 倒序：降序，有大到小
        # book = BookInfo.objects.filter(btitle__isnull = False).order_by('-bread')
        # print(book)
        ################## 聚合查询 #################
        # Avg 求平均值、Count 求数量、Max 求最大值、Min 求最小值、Sum 求和
        # 1.统计图书信息总的阅读量:对本表中所有的阅读量进行求和  # ret = {'bread__sum': 146}
        # ret = BookInfo.objects.aggregate(Sum('bread'))
        # print(ret.get('bread__sum'))


        return http.HttpResponse('查询')