from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Bank(models.Model):
    owner = models.ForeignKey(to=User, on_delete=CASCADE)
    name = models.CharField(max_length=200)
    swift_code = models.CharField(max_length=200)
    inst_num = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class Branch(models.Model):
    name = models.CharField(max_length=200)
    transit_num = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(default='admin@utoronto.ca')
    capacity = models.PositiveIntegerField(blank=True, null=True)
    bank = models.ForeignKey(to=Bank, on_delete=CASCADE, null=True)
    last_modified = models.DateTimeField(auto_now=True)
