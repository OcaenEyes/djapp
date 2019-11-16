from rest_framework import serializers
from .models import Zhihu

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zhihu
        fields = ('username','ctime')