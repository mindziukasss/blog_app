from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_lenght=140)
	body = models.TextFiled()
	date = models.DateTimeField()

	def __str__(self):
			return self.title

