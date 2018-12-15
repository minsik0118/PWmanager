from django.db import models

# Create your models here.
class webpage(models.Model):
	owner=models.CharField(max_length=30)
	name=models.CharField(max_length=10)
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	intro=models.CharField(max_length=100)
	urls=models.CharField(max_length=1000)
	idid=models.CharField(max_length=40)
	pwid=models.CharField(max_length=40)
	btid=models.CharField(max_length=40)
	def __str__(self):
		return self.name

class member(models.Model):
	memberid=models.CharField(max_length=30)
	name=models.CharField(max_length=10)
	voiceitID=models.CharField(max_length=30)
	voiceitPW=models.CharField(max_length=30)
	def __str__(self):
		return self.memberid