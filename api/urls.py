from django.contrib import admin
from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()
router.register("api/cakes",views.CakesView,basename="cakes")
router.register("api/register",views.UserView,basename="register")
router.register("api/carts",views.CartsListView,basename="carts")
router.register("api/order",views.OrderListView,basename="order")






urlpatterns = [
   
    path("token/",ObtainAuthToken.as_view()),
    path("api/cakes/<int:pk>/cart/add",views.AddtoCart.as_view(),name="add-cart"),
    path("api/cakes/<int:pk>/order/",views.OrderView.as_view(),name="order-placed"),
    path("cakes/<int:pk>/review/",views.ReviewView.as_view(),name="review")
]+router.urls

