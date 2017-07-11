#encoding=utf-8
from django.conf.urls import url
import views

# 配置应用下的url
urlpatterns = [
    url('^$', views.index)
]

