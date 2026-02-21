from django.db import models

# Create your models here.

class Book(models.Model):
    
    book_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="home/images", blank=True, null=True)
    slug = models.CharField(max_length=1000, default="")
    sellername = models.CharField(max_length=100, default="")
    pickuplocation = models.CharField(max_length=1000, default="")
    college = models.CharField(max_length=200)  

    def __str__(self):
        return self.book_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=50000)
    name = models.CharField(max_length=900)
    email = models.CharField(max_length=1101)
    address = models.CharField(max_length=1101)
    city = models.CharField(max_length=1101)
    state = models.CharField(max_length=1101)
    zip_code = models.CharField(max_length=1011)
    phone = models.CharField(max_length=1011, default="")
    def __str__(self):
        return "ORDER ID: "+str(self.order_id) +", from - "+ str(self.state)+ ", city: " +str(self.city)

class TrackUpdate(models.Model):
    order_id = models.CharField(max_length=900,default="")     
    update = models.CharField(max_length=9000,default="")     
    daysleft = models.CharField(max_length=9000,default="")  
    def __str__(self):
        return self.order_id
class Chat(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver}"
    