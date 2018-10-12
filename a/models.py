from django.db import models

# Create your models here.

class Targets(models.Model):
    index = models.IntegerField(primary_key=True)
    url = models.URLField(max_length=200, null=False)

class Response(models.Model):
    target = models.ForeignKey(Targets, on_delete=models.CASCADE)
    respondent = models.CharField(max_length=15)
    c = {
        "message": "Welcome to w8d!",
    }
    date = models.DateTimeField('response date')
