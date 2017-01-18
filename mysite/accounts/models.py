from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from commissions.models import Product, Category, Tag, Fandom
from django.db import models

# Create your models here.
class UserExtended(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	isArtist = models.BooleanField(default = False)
	def __unicode__(self):
		return str(self.user.username)

class UserStore(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)
	cover_image = models.ImageField(upload_to='static/images/', null=True, blank=True, default=None)
	category = models.ManyToManyField(Category, null=True, blank=True)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	fandom = models.ManyToManyField(Fandom, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)
	orders_completed = models.IntegerField(default=0)
	avg_rating = models.DecimalField(decimal_places=1, max_digits=4, default=0.0)
	followers = models.IntegerField(default=0)

	usage_policy = models.TextField(null=True, blank=True, default="")
	refund_policy = models.TextField(null=True, blank=True, default="")
	def get_absolute_url(self):
		return reverse("store", kwargs={"id": self.id})

	def __unicode__(self):
		return str(self.id)