from django.db import models

# Create your models here.
class SignUpEmail(models.Model):

	date_added = models.DateTimeField(auto_now_add=True)
	email = models.EmailField(blank=True)

	def __unicode__(self):
		return self.email

class SignUpInfo(models.Model):

	date_added = models.DateTimeField(auto_now_add=True)
	# email = models.ForeignKey(SignUpEmail)
	phone = models.CharField('phone', max_length=20, blank=True)
	first_name = models.CharField('first name', max_length=30, blank=True)
	last_name = models.CharField('last name', max_length=30, blank=True)

	def __unicode__(self):
		return self.phone
