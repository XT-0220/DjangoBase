from django.urls import path

from . import views

urlpatterns = [

path('query/',views.QueryStrView.as_view()),

path('form/',views.FormDataView.as_view()),
]