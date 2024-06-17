from django.db import models
import hashlib


# Create your models here.
#login Credential for custom authendicated login  
class LoginUsers(models.Model):
    username = models.CharField(max_length=50, unique=True)
    pass_wd = models.CharField(max_length=100)
    mail_id = models.EmailField()

    def hash_passwrd(self, password):
        self.password = hashlib.encode(password.encode()).hexgigist()
