from django.db import models

# Create your models here.

class Targets(models.Model):
    index_key = models.CharField(max_length=15, primary_key=True)
    url = models.URLField(max_length=200, null=False)

class Response(models.Model):
    target = models.ForeignKey(Targets, on_delete=models.CASCADE)
    respondent = models.CharField(max_length=15, null=True)
    date = models.DateTimeField('response date')
