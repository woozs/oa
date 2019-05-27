#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2019/5/27 21:09 
# @Author : wuzushun 
# @File : urls.py
from django.urls import path

from hrs import views

urlpatterns = [
    path('', views.index, name='index'),
]