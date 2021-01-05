from django.db import models
from django.utils import timezone as tz

class User(models.Model):
    temp = models.DecimalField(max_digits=5,decimal_places=2)
    img=models.ImageField(upload_to='pics')
    datetime = models.DateTimeField(default=tz.now)
