from django.db import models

# Create your models here.
class emailEnquiry(models.Model):
    email_id=models.EmailField(max_length=50)