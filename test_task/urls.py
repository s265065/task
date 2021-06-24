from django.contrib import admin
from django.urls import path, re_path

from task import views

urlpatterns = [

    re_path(r'^get/', views.get),
    path('', views.index),
    path('admin/', admin.site.urls),

]
