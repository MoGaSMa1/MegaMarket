from django.db import models

# Create your models here.



class Author(models.Model):
    Author = models.CharField(max_length=20)
    def __str__(self):
        return self.Author

class Series(models.Model):
    Series = models.CharField(max_length=20)
    def __str__(self):
        return self.Series

class Gener(models.Model):
    Gener = models.CharField(max_length=20)
    def __str__(self):
        return self.Gener

class Publish(models.Model):
    Publish = models.CharField(max_length=20)
    def __str__(self):
        return self.Publish

