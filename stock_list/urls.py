from django.urls import path

from . import views
app_name = 'stock_list'

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.getStockData, name='index'),
    path('news/<str:corpname>', views.getStockNews, name='news'),
    path('<str:corpname>/delete', views.deleteStock, name='delete_stock'),
    path('search/', views.searchStock, name='search_stock'),
    path('<str:corpname>/add', views.addStock, name='add_stock')
    # path()
    # path('mystock', views.getMyStock, name='mystock'),
]