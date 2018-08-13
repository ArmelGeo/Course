from django.db import models
from django.urls import reverse


# Create your models here.

class Courses(models.Model):
    """ course list class"""

    title = models.CharField(max_length = 200)
    body = models.TextField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    # @classmethod
    # def create_course(cls, title):
    #     course = cls(title=title)
    #     # do something with the book
    #     return course

    def __str__(self):
        return self.__str__


