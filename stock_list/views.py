from django.shortcuts import render
from .models import Stocktbl, Mystock
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StockDataSerializer, MyStockSerializer

# Create your views here.

@api_view(['GET'])
def getStockData(request):
    entire_stock = Stocktbl.objects.all()
    entire_stock_serializer = StockDataSerializer(entire_stock, many=True)
    my_stock = Mystock.objects.filter(username=request.user)
    my_stock_serializer = MyStockSerializer(my_stock, many=True)
    context = {'entire_stock' : entire_stock_serializer.data, 'my_stock' : my_stock_serializer.data}
    return render(request, 'index.html', context)

# def index(request):
#     stock_list = Stocktbl.objects.order_by('id')
#     context = {'stock_list': stock_list}
#     return render(request, 'index.html', context)
