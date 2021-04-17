from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.name, self.age)