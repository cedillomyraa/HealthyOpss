
from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse #allows us to build a url
#The following is our tables that will be used in the database
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)
        
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True) # slug for category models  in django.db import models class behind the url you can type/admin

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])
        
    def __str__(self):
        return self.name # thunderer for backwards compatibility

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator') #who is this product creator record
    title = models.CharField(max_length=255) # title for product
    author = models.CharField(max_length=255, default='admin') #category of sproduct
    description= models.TextField(blank=True) #discription of the product
    image = models.ImageField(upload_to='images/') #upload img and allow us to upload 
    slug = models.SlugField(max_length=255, unique=True) #
    price = models.DecimalField(max_digits=4, decimal_places=2)
    vegan = models.BooleanField(default=True)
    keto= models.BooleanField (default=True)
    lowCarb= models.BooleanField (default=True) #manages stock of product stock or out of stock
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)#used when we add a product
    updated = models.DateTimeField(auto_now=True)#used when we update a product and we want record
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'#how we want to order products and details
        ordering = ('-created',)

    #builds url to view prod details on click   
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])


    def __str__(self):
        return self.title # thunderer method