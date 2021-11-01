# coding:utf-8

from django.urls import path

from . import views

app_name = "demoapp"

urlpatterns = [
    path("my", views.MyView.as_view(), name="my")
]