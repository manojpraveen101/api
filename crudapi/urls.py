from django.conf.urls import url
from django.urls import path
from crudapi import views


urlpatterns = [
    url(r'^api/employee$', views.employee_list),
    path(r'scookie', views.setcookie),
    path(r'gcookie', views.getcookie)

]