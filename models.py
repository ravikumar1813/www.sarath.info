from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=200)
    address=models.CharField(max_length=45)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name