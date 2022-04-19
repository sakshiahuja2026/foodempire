from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models.query_utils import Q
from a_food.models import food

class User(AbstractUser):

# Create your models here.

    username = models.CharField(max_length = 99, unique = True)
    email = models.EmailField(_('email address') ,max_length=150, unique=True)
    phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must be entered in the format: '999999999'")
    phone_number = models.CharField(validators=[phone_regex],max_length=10,unique=True,null=False)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_deleted = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email" , "phone_number"]
    
    class Meta:
        db_table = "User"


    def __str__(self):
        return self.username

class userdetail(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    class Meta:
        db_table = "userdetail"

    def __str__(self):
        return self.name

class location(models.Model):
    
    lname = models.CharField(max_length=50)
    class Meta:
        db_table = "location"

    def __str__(self):
        return self.lname

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fid = models.ForeignKey(food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    #price = models.FloatField()
    class Meta:
        db_table = "cart"

    def __str__(self):
        return f"{self.quantity} of {self.fid} for {self.user}"

    @property
    def get_cart_item(self):
        orderitem_1 = cart.objects.filter(Q(user__username = self.user))
        orderitem = list(orderitem_1)
        return orderitem

    @property
    def get_cart_total(self):
        total = self.fid.price * int(self.quantity)
        return total

    @property
    def get_total(self):
        orderitems = self.get_cart_item
        total_1 = sum([items.get_cart_total for items in orderitems])    
        total = "%.2f" % (total_1 + float(0.18 * total_1))
        return total
    
        


class status(models.Model):

    uid=models.ForeignKey(User, on_delete=models.CASCADE)
    fid = models.ForeignKey(food, on_delete=models.CASCADE)
    cid=models.ForeignKey(cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    class Meta:
        db_table = "status"

    def __str__(self):
        return self.status

class userfooddetail(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    fid = models.ForeignKey(food, on_delete=models.CASCADE)
    cid = models.ForeignKey(cart, on_delete=models.CASCADE)
    sid = models.ForeignKey(status, on_delete=models.CASCADE)
    #lid=models.ForeignKey(location, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    class Meta:
        db_table = "userfooddetail"

    def __str__(self):
        return self.fid