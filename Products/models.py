from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)



    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    make = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='Products/', blank=True, null=True)



