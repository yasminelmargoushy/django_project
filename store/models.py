from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import DateTimeField

CATEGORY_CHOICES= (
('E','Electronics'),
('S','Short'),
('OW','Fashion'),
('Bg','Bags'),
('Sh','Shoes'),
('SW','SportsWear'),
('F','Furniture'),
)
TYPE_CHOICES=(
    ('H', 'Headphones'),
    ('M','Mobiles'))



class Product(models.Model):
    name =models.CharField(max_length=200 , null=True)
    price = models.FloatField()
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2,blank=True,null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=200, blank=True, null=True)
    description=models.TextField()
    favourites=models.ManyToManyField(User,related_name='fav',default='none',blank=True)
    date = models.DateTimeField(default=timezone.now)
    brand=models.CharField(max_length=200 , null=True)
    def __str__(self):
       return self.name

    class Meta:
        ordering = ['-date',]



    def get_rating(self):
        total = sum(int(review['stars']) for review in self.reviews.values())

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0

    @property
    def imageURL(self):
       try:
          url=self.image.url
       except:
          url=' '
       return url


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank = True, null = True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank = True, null = True)
    quantity = models.IntegerField(default=0, blank = True, null = True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete = models.SET_NULL, blank = True, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, blank = True, null = True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.address

class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    

