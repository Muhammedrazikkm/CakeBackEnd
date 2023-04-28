from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Cakes(models.Model):
    name=models.CharField(max_length=25)
    shape_choices=(
        ("circle","circle"),
        ("rectangle","rectangle"),
        ("oval","oval"),
        ("customized","customized")
    )
    customized=models.CharField(max_length=25,null=True,blank=True)
    shape=models.CharField(max_length=25,choices=shape_choices)
    layer_choices=(
        ("one","one"),
        ("two","two"),
        ("three","three")
    )
    layers=models.CharField(max_length=10,choices=layer_choices)
    image=models.ImageField(upload_to="images",blank=True,null=True)
    weight=models.PositiveIntegerField()
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Carts(models.Model):
    name=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=options)
    quantity=models.PositiveIntegerField(default=1)

class Order(models.Model):
    name=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("shipped","shipped"),
        ("order-placed","order-placed"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    currentDate=datetime.date.today()
    expectedDate=currentDate+datetime.timedelta(days=5)
    expected_Delivery_Date=models.DateField(default=expectedDate)
    address=models.CharField(max_length=200,null=True)

class Review(models.Model):
    name=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=250)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.comment