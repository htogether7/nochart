from django.shortcuts import render, redirect
from .models import Stocktbl, Mystock, Newstbl
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StockDataSerializer, MyStockSerializer, NewsSerializer

# Create your views here.

@api_view(['GET'])
def getStockData(request):
    
    my_stock = Mystock.objects.filter(username=request.user)
    my_stock_serializer = MyStockSerializer(my_stock, many=True)
    # print(my_stock_serializer.data)
    
    # print(entire_stock_serializer.data)
    context = {'my_stock' : my_stock_serializer.data}
    return render(request, 'index.html', context)

@api_view(['GET'])
def getStockNews(request, corpname):
    # print(corpname=="APPL")
    # news = Newstbl.objects.all()
    corp_info = Stocktbl.objects.filter(symbol=corpname)
    corp_info_serializer = StockDataSerializer(corp_info, many=True)

    news = Newstbl.objects.filter(corp=corpname)
    news_serializer = NewsSerializer(news, many=True)

    my_stock = Mystock.objects.filter(username=request.user)
    my_stock_serializer = MyStockSerializer(my_stock, many=True)

    check_stock_in_my_stock = False
    for stock in my_stock_serializer.data:
        if stock['symbol'] == corpname.upper():
            check_stock_in_my_stock = True
            break

    context = {'news_list' : news_serializer.data, 'corp_info': corp_info_serializer.data, 'check_stock_in_my_stock': check_stock_in_my_stock}
    # print(corp_info_serializer.data)
    return render(request, 'stock_list/stock_news.html', context)


def deleteStock(request, corpname):
    deleted_stock = Mystock.objects.filter(symbol=corpname) & Mystock.objects.filter(username=request.user)
    deleted_stock.delete()
    return redirect('stock_list:index')

def searchStock(request):
    stock_name = request.GET['stock_name']
    entire_stock = Stocktbl.objects.all()
    entire_stock_serializer = StockDataSerializer(entire_stock, many=True)
    for data in entire_stock_serializer.data:
        if data['symbol'] == stock_name.upper():
            return redirect('stock_list:news', corpname=stock_name)
    if stock_name:
        return render(request, 'stock_list/stock_not_exist.html')
    else:
        return render(request, 'index.html')

def addStock(request, corpname):
    if request.user.is_authenticated:
        new_stock = Mystock(username=request.user, symbol=corpname)
        new_stock.save()
    # print(request.user)
    return redirect('stock_list:news', corpname=corpname)

# def index(request):
#     stock_list = Stocktbl.objects.order_by('id')
#     context = {'stock_list': stock_list}
#     return render(request, 'index.html', context)
