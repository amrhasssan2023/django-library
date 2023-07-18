from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    status_book = [
        ('avalible','avalible'),
        ('sold','sold'),
        ('rental','rental'),
    ]
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250, blank=True, null= True)
    photo_book = models.ImageField(upload_to='photo', blank=True, null= True)
    photo_author = models.ImageField(upload_to='photo', blank=True, null= True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rental_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rental_periud = models.IntegerField( blank=True, null=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=250, choices=status_book, blank=True, null=True)
    active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)



@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created,**kwargs):
    if created:
        Token.objects.create(user=instance)