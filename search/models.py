from django.db import models
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.


class search(models.Model):
    name = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    image = models.ImageField(upload_to="pics/docs/",
                              default="pics/default.jpg")
    phone = PhoneNumberField()
    isgad = models.BooleanField(default=True, editable=False)
    lat = models.FloatField()
    lng = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name+' || ' + self.house


class Member(models.Model):
    name = models.CharField(max_length=100)
    house = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="pics/members/", default="pics/default.jpg")
    phone = PhoneNumberField()
    isgad = models.BooleanField(default=False, editable=False)
    retaled_to = models.ForeignKey(
        search, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
