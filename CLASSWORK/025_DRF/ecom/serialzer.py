from rest_framework import serializers
from ecom.models import *

class CategorySerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
            model=Product
            # fields=['id','name']
            # exclude=['name']
            fields='__all__'
    
    def validate(self, attrs):
        if attrs['qty']<1:
            raise serializers.ValidationError({"qty":"Qty must not be 0"})
        
        return attrs
            