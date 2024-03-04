from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from  django.dispatch import receiver


GENDER_COICES = (
    ('Male','Male'),
    ('Female','Female')
)
class Digizilla(models.Model):
    name = models.CharField( max_length=50, default='default name')
    gender = models.CharField( max_length=50, choices=GENDER_COICES)
    country = models.CharField( max_length=50, default='default country')
    joining_date = models.DateField(default=timezone.now)
    tags = models.ManyToManyField('Tag',blank=True) 
    customers = models.ManyToManyField(User,blank=True) 
    company = models.ForeignKey("Company", related_name='company_digizilla', on_delete=models.CASCADE)
    notes = models.TextField(max_length=5000, default='default note')
    comments = models.CharField( max_length=400, default='default comment')

    class Meta:
        verbose_name = "Digizilla"
        verbose_name_plural = "Digizilla"

    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField( max_length=50, default='default name')

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField( max_length=50, default='default name')

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name




