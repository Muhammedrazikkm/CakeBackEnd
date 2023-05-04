from rest_framework import serializers
from api.models import Carts,Cakes,Order,Review
from django.contrib.auth.models import User






class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["username","email","password","id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    #When using token authentication, the user's password needs to be hashed for security reasons.
    # This is because the password is sent to the server to obtain a token, and if the password is not hashed, 
    # it could be intercepted and used by an attacker to gain access to the user's account.

class CartSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    quantity=serializers.IntegerField(required=True, min_value=1)
    name=serializers.CharField(read_only=True)
    class Meta:
        model=Carts
        fields=["user","name","status","quantity","created_date","id"]
#if notnull error add to serializer
    
class OrderSerializer(serializers.ModelSerializer):
    name=serializers.CharField(read_only=True)
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    expected_Delivary_Date=serializers.DateField(read_only=True)
    class Meta:
        model=Order
        fields=["user","name","status","expected_Delivary_Date","created_date","id"]

class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    name=serializers.CharField(read_only=True)
    class Meta:
        model=Review
        fields=["id","name","user","rating","comment"]

    
class cakeserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    cake_review=ReviewSerializer(read_only=True,many=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Cakes
        fields=["id","name","user","shape","customized","layers","image","weight","price","cake_review"]