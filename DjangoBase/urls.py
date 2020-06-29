"""DjangoBase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


# 总路由的所有信息
from django.urls import path, include

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # path('admin/', admin.site.urls),
    #注册子路由     
    path('',include('user.urls')),

    path('',include('request_response.urls')),

    # 请求和响应
    # path('', include(('子路由', '子应用名字'),
    # namespace='总路由别名，可以随便命名')),
    path('',include(('request_response.urls','request_response'),namespace='request_response1')),

    path('',include('book.urls')),

]
