from traceback import print_exception
from unicodedata import name
from django.db import models


class FoodModel(models.Model):
    name = models.CharField(max_length=50, default='No name')
    details = models.CharField(max_length=500, default="NoDetails")
    price = models.IntegerField(default=0)
    allergens = models.CharField(max_length=250, default='No allergens')
    image = models.ImageField(null=True, blank=True, upload_to='foodapp/static/uploaded_images/')
    orderedCount = models.IntegerField(default=0)
    ratesSum = models.IntegerField(default=0)
    ratesCounter = models.IntegerField(default=0)


class CustomModel(models.Model):
    userid = models.IntegerField(default=-1)
    phoneno = models.CharField(max_length=12, default='noPhoneno')
    requestToBeDeleted = models.BooleanField(default=False)
    givenRatesCounter = models.IntegerField(default=0)
    givenRatesSum = models.IntegerField(default=0)


class OrderModel(models.Model):
    username = models.CharField(max_length=20, default='noUser')
    phoneno = models.CharField(max_length=15, default='noPhoneno')
    address = models.CharField(max_length=50, default='noAddress')
    billingAddress = models.CharField(max_length=50, default='noBillingAddress')
    orderitems = models.CharField(max_length=200, default='noOrderitems')
    total = models.CharField(max_length=10, default='0')
    status = models.CharField(max_length=10, default='pend')
    rate = models.CharField(max_length=20, default='notRated')

    def ratedFoodNamesFromOrderitemsList(self):
        ratedfoodsList = []
        tempList = self.orderitems.split(";")
        for item in tempList:
            ratedfoodsList.append(item.split(",")[0])
        ratedfoodsList.pop()
        return ratedfoodsList


class Logger(models.Model):
    user = models.CharField(max_length=20, default='NoUser')
    datetime = models.CharField(max_length=30, default='NoDate')
    ipaddress = models.CharField(max_length=20, default='NoIpAddress')
    requestMethod = models.CharField(max_length=20, default='NoMethod')
    viewFunctionCalled =  models.CharField(max_length=50, default='NoFunction')
    priorityInt = models.IntegerField(default=0)
    priorityString = models.CharField(max_length=20, default='NoPriority')
    message =  models.CharField(max_length=500, default='NoMessage')
