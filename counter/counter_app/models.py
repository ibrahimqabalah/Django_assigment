from django.db import models

# Create your models here.


class RootRouteView(models.Model):
    count = models.IntegerField(default=0)