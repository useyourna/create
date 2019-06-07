from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    description= models.TextField()
    price= models.IntegerField(null=True)
    view_count = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
# Create your models here.
