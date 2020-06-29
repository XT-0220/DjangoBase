from django.urls import path

from . import views

urlpatterns=[

    path('add/',views.AddView.as_view()),

    path('querystr/',views.QueryView.as_view()),


]