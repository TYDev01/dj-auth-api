from django.db import models

# Create your models here.
class NewUsers(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}{" "}{self.last_name}"