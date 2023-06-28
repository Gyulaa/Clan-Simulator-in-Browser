from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=25)
    vitality = models.IntegerField()
    resilience = models.IntegerField()
    health = models.IntegerField(default=100)
    age = models.IntegerField(default=0)
    pcn = models.IntegerField()
    childnumber = models.IntegerField()
    position = models.TextField(max_length=20) #pawn, citizen, baron, count, king
    balance = models.IntegerField()
    alive = models.BooleanField(default=True)
    fatherid = models.IntegerField()
