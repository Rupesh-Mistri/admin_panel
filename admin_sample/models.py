from django.db import models

# Create your models here.
class OrderDetailsModel(models.Model):
    order_no=models.CharField( max_length=50)
    name =models.CharField(max_length=50)
    quantity =models.IntegerField()
    price= models.DecimalField(decimal_places =2,max_digits=10)
    pin= models.CharField(max_length=50)
    class Meta:
        db_table='tbl_order_details'


class UserDetailsModel(models.Model):
    username_name =models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    username =models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    class Meta:
        db_table='tbl_user'

class SellerDetailsModel(models.Model):
    seller_name =models.CharField(max_length=50)
    state_name= models.CharField(max_length=50)
    pin  = models.CharField(max_length=50)
    username =models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    class Meta:
        db_table='tbl_seller'

class OrderStatusModel(models.Model):
    order= models.ForeignKey(OrderDetailsModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetailsModel, on_delete=models.CASCADE)
    seller  = models.ForeignKey(SellerDetailsModel, on_delete=models.CASCADE)
    seller_action = models.SmallIntegerField( null=True)
    remark = models.CharField(max_length=50, null=True)

    class Meta:
        db_table ='tbl_order_status'