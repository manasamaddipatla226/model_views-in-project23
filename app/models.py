from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=100)
    book_publisher=models.CharField(max_length=100)
    book_cost=models.IntegerField()
    def __str__(self):
        return self.book_name


class Topic(models.Model):
    topic_name=models.CharField(max_length=100)
    content=models.CharField(max_length=100)
    def __str__(self):
        return self.topic_name
