from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
	topic_name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.topic_name

class Entry(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	content = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural="entries"

	def __str__(self):
		if len(self.content) > 50:
			return f"{self.content[:50]}..."
		return self.content
