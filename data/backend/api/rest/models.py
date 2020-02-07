from django.db import models

class Person(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="person's name",
        help_text="Please insert your full name",
    )
    
    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=1, 
        choices=( ('0', 'Male'), ('1', 'Female'), )
    )