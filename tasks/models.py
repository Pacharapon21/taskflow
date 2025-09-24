
from django.db import models


class Task(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	deadline = models.DateTimeField(null=True, blank=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title
