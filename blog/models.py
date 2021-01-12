from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORIES=(
    ('Bags','Bags'),('Shoes','Shoes'),
    ('Tops','Tops'),('Jeans','Jeans'),
    ('Pants','Pants'),('Mobile Phones','Mobile Phones'),
    ('HeadPhones','HeadPhones')
		)
    category=models.CharField(max_length=100,choices=CATEGORIES,default='none')
    title= models.CharField(max_length=100)
    content= models.TextField()
    header_image=models.ImageField(null=True, blank=True, upload_to="images/",default='/static/blog/product2')
    price=models.CharField(max_length=5)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    favourites=models.ManyToManyField(User,related_name='favourite',default='none',blank=True)
    date_posted = models.DateTimeField(default=timezone.now)	


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})

    def __str__(self):
        return self.title



		

class PostReview(models.Model):
    post = models.ForeignKey(Post, related_name='reviews', on_delete=models.CASCADE)
    author= models.ForeignKey(User,on_delete=models.CASCADE,default='')
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.post.title


class PostOrder(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank = True, null = True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length=200,null=True)

    def _str_(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        postorderitems = self.postorderitem_set.all()
        total = sum([int(item.get_total) for item in postorderitems])
        return total

    @property
    def get_cart_items(self):
        postorderitems = self.postorderitem_set.all()
        total = sum([int(item.quantity) for item in postorderitems])
        return total

class PostOrderItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, blank = True, null = True)
    postorder = models.ForeignKey(PostOrder, on_delete = models.SET_NULL, blank = True, null = True)
    quantity = models.IntegerField(default=0, blank = True, null = True)

    @property
    def get_total(self):
        total = int(self.post.price) * self.quantity
        return total

