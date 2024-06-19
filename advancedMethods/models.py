from django.db import models
import hashlib


# Create your models here.
#login Credential for custom authendicated login  
class LoginCredUsers(models.Model):
    username = models.CharField(max_length=50, unique=True)
    pass_wd = models.CharField(max_length=100)
    mail_id = models.EmailField()

    def hash_passwrd(self, password):
        self.pass_wd = hashlib.sha256(password.encode()).hexdigest()
        return self.pass_wd

    def __str__(self):
        return f"User : {self.username}"

#for file upload
class FileUpload(models.Model):
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
