from django.db import models
from sqlite3 import DatabaseError
from django.utils import timezone

class Asset(models.Model):
    Type = models.CharField(max_length=50, blank=True, null=True)
    Name = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    Hire_Date = models.DateTimeField(default=timezone.now)
    Due_Date = models.DateField(blank=True, null=True)
    requested = models.BooleanField(default=False)  # Add this line

    def __str__(self):
        return f"{self.Name} - {self.Type}"

    @property
    def status(self):
        if self.Due_Date and self.Due_Date < timezone.now().date():
            return 'overdue'
        return 'hired'

class teacher(models.Model):

    Name = models.CharField(max_length=25)

    Area = models.CharField(max_length=30)
