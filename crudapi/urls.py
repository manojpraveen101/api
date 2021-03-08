from django.conf.urls import url

from crudapi import views


urlpatterns = [
    url(r'^api/employee$', views.employee_list),
]