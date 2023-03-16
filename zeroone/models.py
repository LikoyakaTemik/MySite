import uuid
from django.db import models
from django.conf import settings
import os
# Create your models here.


class counter(models.Model):
    ip_user = models.TextField(default="127.0.0.1")
    ind = models.IntegerField(default=0)
    last_click = models.DateTimeField(auto_now=True)
