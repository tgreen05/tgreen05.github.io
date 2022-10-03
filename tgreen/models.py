from django.db import models

# Create your models here.

class UploadFile(models.Model):

	nama_file = models.CharField(max_length=50)
	file = models.FileField()

	def __str__(self):
		return self.nama_file