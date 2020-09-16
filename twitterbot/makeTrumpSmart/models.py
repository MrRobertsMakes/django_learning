from django.db import models

# Create your models here.


class TargetTwitter(models.Model):
    handle = models.CharField(max_length=200)
    tweet_number = models.IntegerField(default=0)
