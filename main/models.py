from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=10, blank=True, null=True)

class DonatedMeds(models.Model):
    medicine_name = models.CharField(max_length=30)
    donated_by = models.CharField(max_length=70)
    received = models.BooleanField()
    location1 = models.CharField(max_length=100)
    location2 = models.CharField(max_length=100)
    location3 = models.CharField(max_length=100)
    full_name = models.CharField(max_length=70)
    email = models.CharField(max_length=33)
    phone = models.CharField(max_length=10)
    med_photo = models.ImageField(upload_to ='uploads/', height_field=None, width_field=None, max_length=100)   
    expiry_date = models.CharField(max_length=50)    

    def __str__(self):
        return self.medicine_name + " donated by " + self.full_name

class GetMeds(models.Model):
    medicine_name = models.CharField(max_length=30)
    received = models.BooleanField()
    location1 = models.CharField(max_length=100)
    location2 = models.CharField(max_length=100)
    location3 = models.CharField(max_length=100)
    full_name = models.CharField(max_length=70)
    email = models.CharField(max_length=33)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name + " wants to buy " + self.medicine_name