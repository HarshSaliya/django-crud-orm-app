from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurant(models.Model):
    class TypeChoice(models.TextChoices):
        Indian ='IN' , 'Indian'
        Chinese = 'CH', 'Chinese'
        Italian = 'IT', 'Italian'
        Mexican = 'MX', 'Mexican'
        Japanese = 'JP', 'Japanese'
        Korean = 'KR', 'Korean'
        Other = 'OT', 'Other'
        American = 'AM', 'American'





    name=models.CharField(max_length=100)
    website=models.URLField(default='')
    date_opened=models.DateField()
    latitude=models.FloatField()
    longitude=models.FloatField()
    restaurant_choice=models.CharField(max_length=2 , choices=TypeChoice.choices)


    def __str__(self):
        return self.name


class Rating(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant , on_delete=models.CASCADE)
    rating=models.PositiveSmallIntegerField()


    def __str__(self):
        return f"Rating. {self.rating}"
    


class Sale(models.Model):
    restaurant=models.ForeignKey(Restaurant , on_delete=models.CASCADE ,related_name="incomes")
    income=models.DecimalField(max_digits=8 , decimal_places=2)
    datetime=models.DateTimeField()



class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name