from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Dish(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='dish_category')
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='dishes/')
    price = models.FloatField()

    def __str__(self):
        return self.name