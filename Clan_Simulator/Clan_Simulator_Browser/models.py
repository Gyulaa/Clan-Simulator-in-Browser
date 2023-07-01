from django.db import models
from django.core.validators import MaxValueValidator


class Member(models.Model):
    name = models.CharField(max_length=25)
    vitality = models.IntegerField(validators=[MaxValueValidator(100)])
    resilience = models.IntegerField(validators=[MaxValueValidator(100)])
    health = models.IntegerField(default=100)
    age = models.IntegerField(default=0)
    pcn = models.IntegerField(validators=[MaxValueValidator(5)])
    childnumber = models.IntegerField()
    position = models.TextField(max_length=20) #pawn, citizen, baron, count, king
    balance = models.IntegerField()
    alive = models.BooleanField(default=True)
    fatherid = models.IntegerField()
