from django.urls import path

from . import views

urlpatterns = [

path('query/',views.QueryStrView.as_view()),

path('form/',views.FormDataView.as_view()),

path('json/',views.JsonDataView.as_view()),

path('response/',views.Response1View.as_view()),

path('json1/',views.JsonResponseView.as_view()),

path('redirect/',views.RedirectView.as_view()),

path('testredirect/',views.TestRedirectView.as_view()),

path('redirect1/',views.RedirectView1.as_view(),name='redirect'),

path('testredirect1/',views.TestRedirectView1.as_view()),


]