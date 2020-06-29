from django.urls import path

from . import views

urlpatterns=[

    path('add/',views.AddView.as_view())
]