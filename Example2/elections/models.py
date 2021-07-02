from django.db import models
from django.db.models.base import Model
from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=1)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class Poll(models.Model):
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    area = models.CharField(max_length = 15)
    id = models.AutoField(primary_key=True)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE,)
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE,)
    votes = models.IntegerField(default = 0)
    id = models.AutoField(primary_key=True)