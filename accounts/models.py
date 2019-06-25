from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	foto = models.ImageField(upload_to = 'images/', blank = True, default = None)
	def __str__(self):
		return '{} - {}'.format(self.username, self.email)
