from django.shortcuts import render
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
    entire_stock = Stocktbl.objects.all()
    entire_stock_serializer = StockDataSerializer(entire_stock, many=True)
    # print(entire_stock_serializer.data)
    context = {'entire_stock' : entire_stock_serializer.data, 'my_stock' : my_stock_serializer.data}
    return render(request, 'index.html', context)

@api_view(['GET'])
def getStockNews(request, corpname):
    # print(corpname=="APPL")
    # news = Newstbl.objects.all()
    corp_info = Stocktbl.objects.filter(symbol=corpname)
    corp_info_serializer = StockDataSerializer(corp_info, many=True)
    news = Newstbl.objects.filter(corp=corpname)
    # print(news)
    # news = Newstbl.objects.all()
    news_serializer = NewsSerializer(news, many=True)
    context = {'news_list' : news_serializer.data, 'corp_info': corp_info_serializer.data}
    print(corp_info_serializer.data)
    return render(request, 'stock_list/stock_news.html', context)


# def index(request):
#     stock_list = Stocktbl.objects.order_by('id')
#     context = {'stock_list': stock_list}
#     return render(request, 'index.html', context)
