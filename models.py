from sqlite3 import DatabaseError
from django.db import models
from django.utils import timezone

class Asset(models.Model):
   Type = models.CharField(max_length=50, blank=True, null=True)
   Name = models.CharField(max_length=50, blank=True, null=True)
   Email = models.CharField(max_length=50, blank=True, null=True)
   Hire_Date = models.DateTimeField (default = timezone.now)

   def __str__(self):
       return self.code + '-' + self.Type
