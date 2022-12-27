from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=40)


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
