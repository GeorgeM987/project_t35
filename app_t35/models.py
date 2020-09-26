from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Directions(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    from_loc = models.CharField(max_length=100, null=True)
    to_loc = models.CharField(max_length=100, null=True)
    best_route = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.best_route