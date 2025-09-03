from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
  id=models.BigAutoField(primary_key=True)
  name=models.CharField(max_length=250,blank=False,null=False,unique=True)
  description=models.TextField(max_length=500,blank=True)
  slug=models.SlugField(max_length=255)
  image=models.ImageField(upload_to="photos/categories",blank=True)

  class Meta:
    verbose_name="category"
    verbose_name_plural="categories"

  def __str__(self):
    return f"{self.name} {self.slug}"  
  
class Product(models.Model):
  product_name=models.CharField(max_length=255,unique=True)
  slug=models.SlugField(max_length=255,unique=True)
  description=models.TextField(max_length=255)
  price=models.FloatField()
  image=models.ImageField(upload_to="photos/products")
  stock=models.IntegerField()
  is_available=models.BooleanField(default=True)
  category=models.ForeignKey(Category,on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    # Met à jour automatiquement is_available selon le stock
    self.is_available = self.stock > 0
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.product_name} {self.stock}"

