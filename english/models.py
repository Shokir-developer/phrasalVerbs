from django.db import models

class EnglishPhrases(models.Model):
	english = models.CharField(max_length=200, null=True)
	uzbek = models.CharField(max_length=200, null=True)
	definition = models.CharField(max_length=200, null=True)
	example = models.TextField(max_length=300)

	def __str__(self):
		return self.english
