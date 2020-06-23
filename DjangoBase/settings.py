"""
Django settings for DjangoBase project.

Generated by 'django-admin startproject' using Django 1.11.29.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
# 导入python标准库中的操作系统模块：使用os模块可以操作系统文件，配置文件中会用到
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 默认是当前工程的根目录=找到当前的配置文件的绝对路径，再取取他的上两级目录路径（BASE_DIR是根据settings.py所在目录的变化而变化的）
# 作用：就是用于在工程内部构建、拼接文件路径的。说明：需要用到就看一下，没有什么可拼接的路径，就不管他

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('BASE_DIR : %s' , BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# # 密钥='很长的一个没有任何规律的复杂的字符串组成的'
#
# # 作用：Django工程中，如果需要用到一些加密处理，那么加密时，默认的秘钥就是这个配置项

SECRET_KEY = 'u^=6f+khgb(a@&0z#aowtp7_x+y8&9!3a8gt2h-ulq5$q=zrld'

# SECURITY WARNING: don't run with debug turned on in production!

# # 指定开发阶段的调试模式。在开发阶段，属于调试，所以DEBUG = True
#
# # 提示：部署时，我们一定要将DEBUG = False (在生产环境下，不要使用DEBUG模式运行过程)
#
# # 好处：如果DEBUG = True，那么在开发阶段，如果成功报错，就会精准的定位到错误的位置和原因
DEBUG = True


# 允许访问该程序的域名：允许哪个计算机访问Django程序，就把那个计算机的IP、域名写进去
ALLOWED_HOSTS = []


# Application definition
# 注册Django的子应用的
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',

]
# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 路由的入口（miniweb项目我们是自己实现的）
ROOT_URLCONF = 'DjangoBase.urls'

# 配置模板模块的：MVT当中的T(Templat)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# wsgi协议的入口（miniweb项目我们是自己实现的）
WSGI_APPLICATION = 'DjangoBase.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# 如果使用Django开发注册和登录，需要使用的密码加密和验证的方案
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# 语言
LANGUAGE_CODE = 'zh-hans'
# 时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 加载静态文件的地址前缀
STATIC_URL = '/static/'
