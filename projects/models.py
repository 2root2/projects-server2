from django.db import models
from django.utils import timezone
import datetime
from random import randint

# Create your models here.

class Forms(models.Model):
    name = models.CharField(max_length=255, null=False)
    shape = models.CharField(max_length=255, null=False)
    updatedate = models.DateTimeField(default=datetime.datetime.now)
    createdon = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
    	return "{} - {} - {}".format(self.pk, self.name, self.shape)

class Users(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    age = models.IntegerField(null=False)
    imageUrl = models.URLField(max_length=255, null=False)
    updatedate = models.DateTimeField(default=datetime.datetime.now)
    createdon = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
    	return "{} - {} - {}".format(self.pk, self.firstname, self.lastname)

class Projects(models.Model):
    
    project = models.CharField(max_length=255, null=False)
    
    description = models.CharField(max_length=2000, null=False)

    total = models.IntegerField(default=randint(1,99))

    formsubmitted = models.IntegerField(default=randint(1,99))

    count = models.IntegerField(default=randint(1,99))

    # forms = models.ManyToManyField(Forms)
    # profile = models.ManyToManyField(Forms)

    createdon = models.DateTimeField(default=datetime.datetime.now)
    lastupdated = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "{} - {} - {}".format(self.pk, self.project, self.description)