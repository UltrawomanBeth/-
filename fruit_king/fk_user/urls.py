from django.conf.urls import url
import views

urlpatterns = [
    url('^cart/$', views.cart),
    url('^register/$', views.register),
    url('^register_handle/$', views.register_handle),
    url('^register_valid/$', views.register_valid),
    url('^login/$', views.login),
    url('^login_handle/$', views.login_handle),
    url('^loginout/$', views.loginout),
    # url('^detail/$', views.detail),
    # url('^index/$', views.index),
    # url('^list/$', views.list),

    # url('^place_order/$', views.place_order),
    url('^$', views.center),
    url('^order/$', views.order),
    url('^site/$', views.site),


]