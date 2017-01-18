from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
import uuid
from django.utils.text import slugify
from django.conf import settings
import datetime

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	featured = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

class Fandom(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	featured = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

class Tag(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	featured = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	num_commissions = models.IntegerField(default=0)
	def __unicode__(self):
		return self.title

# T-Shirt 1
# Active Wear 2
# Women's Clothing 3

class Product(models.Model):
	title = models.CharField(max_length=120)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	description = models.TextField(null=True, blank=True)
	category = models.ManyToManyField(Category, null=True, blank=True)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	fandom = models.ManyToManyField(Fandom, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True, null=True)
	revisions = models.IntegerField(default=0, null=True, blank=True)
	wont_draw = models.TextField(null=True, blank=True)

	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	featured = models.BooleanField(default=False)

	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	# 0 = off, 1 = on
	status = models.IntegerField(default=1)
	slots = models.IntegerField(null=True, blank = True)
	
	cover_image = models.ImageField(upload_to='static/images/')

	orders_completed = models.IntegerField(default=0)

	time_min_weeks = models.IntegerField(default=0, null=True, blank=True)
	time_max_weeks = models.IntegerField(default=0, null=True, blank=True)

	request_detail_prompt = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.owner.username + "_" +  self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("commission", kwargs={"id": self.id})

	def save(self, *args, **kwargs):
		if not self.id:
			# Newly created object, so set slug
			self.slug = slugify(self.title)

		super(Product, self).save(*args, **kwargs)

class ProductVariant(models.Model):
	title = models.CharField(max_length=120)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	cover_image = models.ImageField(upload_to='static/images/')

	def __unicode__(self):
		return self.product.owner.username + "_" + self.product.title + "_" +  self.title


class ProductAddOn(models.Model):
	title = models.CharField(max_length=120)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.product.title + "_" +  self.title

