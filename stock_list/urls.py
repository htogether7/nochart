from django.urls import path

from . import views
app_name = 'stock_list'

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.getStockData, name='index'),
    path('news/<str:corpname>', views.getStockNews, name='news'),
    # path('mystock', views.getMyStock, name='mystock'),
]