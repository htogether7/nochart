from http.client import HTTPResponse
from django.shortcuts import render
from .models import Stocktbl
# Create your views here.
def index(request):
    stock_list = Stocktbl.objects.order_by('id')
    context = {'stock_list': stock_list}
    return render(request, 'index.html', context)
