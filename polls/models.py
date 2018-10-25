from django.db import models
import datetime
from ckeditor.fields import RichTextField



# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.text


class Letter(models.Model):
    alpha = models.CharField(max_length=200,default='')
    alpha.alphabetic_filter = True

    def __str__(self):
        return self.alpha



class Word(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE,default='',related_name = 'connect')
    word = models.CharField(max_length=200,default='')
    word_exp = models.TextField()

    def __str__(self):
        return self.word

class About(models.Model):
    title_a = models.CharField( max_length=100)
    content_a = models.TextField()
    title_a = RichTextField()
    content_a  =RichTextField()

    def __str__(self):
        return self.title_a

class Services(models.Model):
    title_s = models.CharField(max_length = 100)
    content_s = models.TextField()

    def __str__(self):
        return  self.title_s

class Learn(models.Model):
    title_l= models.CharField(max_length = 100)
    content_l = models.TextField()
    content_l = RichTextField()

    def __str__(self):
        return  self.title_l
