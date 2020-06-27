from django.urls import path, re_path

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),

    # path('login/', views.LoginView.as_view()),

    re_path(r'^login/$', views.LoginView.as_view()),

]