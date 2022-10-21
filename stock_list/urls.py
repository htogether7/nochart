from django.urls import path

from . import views
app_name = 'stock_list'

urlpatterns = [
    # path('', views.index, name='index')
    path('stock/', views.getStockData, name='index'),
    # path('mystock', views.getMyStock, name='mystock'),
]