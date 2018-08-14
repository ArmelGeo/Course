from django.db import models
from django.urls import reverse


# Create your models here.

class Courses(models.Model):
    """ course list class"""

    title = models.CharField(max_length = 200)
    body = models.TextField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.title


