from django.urls import path

from . import views
app_name = 'stock_list'

urlpatterns = [
    path('', views.index, name='index')
]