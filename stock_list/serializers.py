from tkinter.filedialog import FileDialog
from rest_framework.serializers import ModelSerializer
from .models import Stocktbl, Mystock

class StockDataSerializer(ModelSerializer):
    class Meta:
        model = Stocktbl
        fields = '__all__'


class MyStockSerializer(ModelSerializer):
    class Meta:
        model = Mystock
        fields = '__all__'