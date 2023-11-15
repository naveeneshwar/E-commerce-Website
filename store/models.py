from django.db import models
import datetime

class Category(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='categories' #changes the default display of categorys to categories
    
class Customer(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    phone=models.IntegerField()
    email=models.EmailField(max_length=64)
    password=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Product(models.Model):
    name=models.CharField(max_length=64)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=10) # default indicates if it does not contain any value it's gonna be free
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=250,default='',blank=True,null=True)
    image=models.ImageField(upload_to='upload/product/')
    
    #sale
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,decimal_places=2,max_digits=10)

    def __str__(self):
        return self.name

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)    
    customer=models.ForeignKey(Category,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=150,default='',blank=True)
    phone=models.IntegerField(default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product