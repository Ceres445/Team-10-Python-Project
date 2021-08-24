from django.db import models

# Create your models here.
from home.models import Classes


class ClassTime(models.Model):
    key_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.TextField(max_length=50)
    permanent = models.BooleanField(default=True)

    class Day(models.IntegerChoices):
        Monday = 0
        Tuesday = 1
        Wednesday = 2
        Thursday = 3
        Friday = 4
        Saturday = 5
        Sunday = 6

    day = models.IntegerField(choices=Day.choices)
    time = models.TimeField(auto_now=False)
    link = models.TextField(max_length=400)