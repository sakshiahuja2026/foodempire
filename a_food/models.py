import email
from email.message import Message
from tokenize import Name
from django.db import models
from datetime import datetime

# Create your models here.
class food(models.Model):
    #fid=models.IntegerField()
    fname=models.CharField(max_length=50)
    price=models.FloatField()
    quantity=models.IntegerField()
    Description=models.CharField(max_length=300)

    Cost=models.FloatField()

    class Meta:
        db_table="a_food"



class category(models.Model):
    cname=models.CharField(max_length=50)
    cid=models.IntegerField()
    
    class Meta:
        db_table="category"

class removefood(models.Model):
    cid=models.ForeignKey(category,on_delete=models.CASCADE)
    fid=models.ForeignKey(food, on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    class Meta:
        db_table="removefood"