from django.db import models

# Create your models here.
class Voters(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=False)
    voter_id_no = models.CharField(max_length=15)


    def __str__(self):
        return f"Voter: {self.name}"


