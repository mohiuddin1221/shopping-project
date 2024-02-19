from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 20,db_index = True)
    slug = models.SlugField(max_length =20, unique = True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self) :
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category,related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length =20,db_index=True)
    slug = models.SlugField(max_length =20 , unique = True)
    image = models.ImageField(upload_to='images/', blank=True)
    description =models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    avilable = models.BooleanField(default = True)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now = True) 
    
    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)
        
    def __str__(self) :
        return self.name