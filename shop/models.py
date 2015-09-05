from django.db import models
from django.contrib.auth.models import AbstractUser


class Unit(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AppUser(AbstractUser):
    login_email = models.CharField(max_length=200)

    def __str__(self):
        return self.login_email


class Products(models.Model):
    name = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit)
    quantity = models.FloatField()

class Address(models.Model):
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200)
    zip = models.IntegerField()

    def __str__(self):
        return self.country + " , " + self.city + "," + self.address_line1


class Buyer(AppUser):
    addresses = models.ManyToManyField(Address, related_name="+")
    active_address = models.ForeignKey(Address, related_name="+")

    class Meta:
        verbose_name = "Buyer"

    def __str__(self):
        return self.login_email


class Offers(models.Model):
    price_per_quantity = models.FloatField()
    product = models.ForeignKey(Products, related_name="+")


class Seller(AppUser):
    addresses = models.ManyToManyField(Address, related_name="+")
    active_address = models.ForeignKey(Address, related_name="+")
    products = models.ManyToManyField(Products, related_name="+")
    offers = models.ManyToManyField(Offers, related_name="+")

    class Meta:
        verbose_name = "Seller"

    def __str__(self):
        return self.login_email