from django.shortcuts import render
from api.serializers import cakeserializer,UserSerializer,CartSerializers,OrderSerializer,ReviewSerializer
from api.models import Carts,Cakes,Order,Review
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions,authentication
from django.views.generic import View
from rest_framework.response import Response

# Create your views here.


class CakesView(ModelViewSet):
    model=Cakes
    queryset=Cakes.objects.all()
    serializer_class=cakeserializer
   
#for filtering
    def get_queryset(self):
        queryset = Cakes.objects.all()
        cake_layer = self.request.query_params.get('layers')
        cake_shape = self.request.query_params.get('shape')
        #if "layers in self.request.query.params:
        # lay=self.re.get("layers")"
        #qs=qs.filter(layer=lay)
        if cake_layer:
            queryset = queryset.filter(layers=cake_layer)
        if cake_shape:
            queryset=queryset.filter(shape=cake_shape)
        return queryset
    
    
# In Django REST Framework, query parameters can be extracted from the request object using the query_params attribute, 
# which is a dictionary-like object that contains all the query parameters of the request.
#  To retrieve the value of a specific query parameter, you can use the get method of the query_params attribute 
# and pass in the name of the query parameter as the argument.

class UserView(ModelViewSet):
    model=User
    queryset=User.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

#localhost:8000/api/carts/1/cart/add
class AddtoCart(APIView):
    serializer_class=CartSerializers
    queryset=Carts.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):
        user=request.user
        id=kwargs.get("pk")
        Cakes_obj=Cakes.objects.get(id=id)
        serializer=CartSerializers(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data.get("quantity")
            qs=Carts.objects.create(name=Cakes_obj,user=user,quantity=quantity)
            serializer=CartSerializers(qs)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
class CartsListView(ModelViewSet):
    serializer_class=CartSerializers
    queryset=Carts.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)

#localhost:8000/api/cake/1/order
class OrderView(APIView):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user=request.user
        carts=Carts.objects.get(id=id)
        serializer=OrderSerializer(data=request.data)
        address=request.POST.get("address")
        if serializer.is_valid():
            address= serializer.validated_data.get("address")
            qs=Order.objects.create(name=carts.name,user=user,address=address)
            serializer=OrderSerializer(qs)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
#localhost:8000/api/order
class OrderListView(ModelViewSet):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

#localhost:8000/cakes/<int:pk>/review
class ReviewView(APIView):
    serializer_class=ReviewSerializer
    queryset=Review.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        user=request.user
        cake_review=Cakes.objects.get(id=id)
        serializer=ReviewSerializer(data=request.data)
        comment=request.POST.get("comment")
        rating=request.POST.get("rating")
        if serializer.is_valid():
            comment= serializer.validated_data.get("comment")
            rating= serializer.validated_data.get("rating")
            qs=Review.objects.create(name=cake_review,user=user,comment=comment,rating=rating)
            serializer=ReviewSerializer(qs)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
