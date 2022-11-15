from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE,
                             related_name="customer")
	address = models.CharField(max_length=200, null=True)
	phone_no = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.address
