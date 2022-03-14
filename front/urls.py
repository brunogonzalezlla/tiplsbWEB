from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check-initialized', views.check_initialized, name='check_initialized'),
    path('init-add', views.init_and_add, name='init_add'),
    path('add', views.add, name='add'),
    path('get_path', views.get_path, name='get_path'),
]