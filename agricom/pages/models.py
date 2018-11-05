from django.db import models


# Create your models here.
class Movers(models.Model):
	name=models.CharField(max_length=20)
	location=models.CharField(max_length=20)

	def _unicode_(self):
		return self.name
	class Meta:
		verbose_name_plural ="Movers"