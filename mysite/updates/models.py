from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
import uuid
from django.utils.text import slugify
from django.conf import settings
import datetime
from commissions.models import Product
from orders.models import Order
from accounts.models import UserStore
from django.contrib.auth.models import User

UPDATE_TYPES = (
		("Request Created", "Request Created"),
		("Request Accepted", "Request Accepted"),
		("Work In Progress", "Work In Progress"),
		("Revision", "Revision"),
		("Chat", "Chat"),
		("Completed", "Completed"),
		("Blog post", "Blog post"),
		("Store announcement", "Store announcement"),
	)

IMAGE_TYPES = (
		("Reference", "Reference"),
		("Work in Progress", "Work in Progress"),
		("Final Product", "Final Product"),
	)

# Create your models here.
class Update(models.Model):
	text = models.TextField()
	order = models.ForeignKey(Order, null=True, blank=True, default=None)
	store = models.ForeignKey(UserStore, null=True, blank=True)
	update_type =  models.CharField(max_length=120, choices=UPDATE_TYPES, default="Request Created")
	sender_is_artist = models.BooleanField()
	created_at = models.DateTimeField(default=datetime.datetime.now)

	def get_absolute_url(self):
		return reverse("update", kwargs={"id": self.id})

	def __unicode__(self):
		return str(self.store.id) + "_" + str(self.created_at)

class UpdateImage(models.Model):
	image = models.ImageField(upload_to='static/images/')
	order = models.ForeignKey(Order, null=True, blank=True, default=None)
	update = models.ForeignKey(Update)
	store = models.ForeignKey(UserStore, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	image_type = models.CharField(max_length=120, choices=IMAGE_TYPES, default="Reference")
	def __unicode__(self):
		return str(self.update.id) + "_" + str(self.created_at)

	def get_absolute_url(self):
		return reverse("updateimage", kwargs={"id": self.id})

class Review(models.Model):	
	rating = models.DecimalField(decimal_places=1, max_digits=100, default=0.0)
	rating_quality  = models.DecimalField(decimal_places=1, max_digits=100, default=0.0)
	rating_communication  = models.DecimalField(decimal_places=1, max_digits=100, default=0.0)
	rating_professionalism  = models.DecimalField(decimal_places=1, max_digits=100, default=0.0)
	rating_timeliness  = models.DecimalField(decimal_places=1, max_digits=100, default=0.0)
	text = models.TextField()
	store = models.ForeignKey(UserStore, null=True, blank=True)
	order = models.ForeignKey(Order)
	created_at = models.DateTimeField(default=datetime.datetime.now)

	def get_absolute_url(self):
		return reverse("review", kwargs={"id": self.id})

	def __unicode__(self):
		return str(self.order.id) + "_" + str(self.created_at)