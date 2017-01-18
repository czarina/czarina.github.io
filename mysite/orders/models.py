from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from accounts.models import UserExtended
from commissions.models import Product, ProductAddOn
from django.core.urlresolvers import reverse

STATUS_CHOICES = (
		("Requested", "Requested"),
		("In Progress", "In Progress"),
		("Completed", "Completed"),
		("Abandoned", "Abandoned"),
	)
# Create your models here.
class Order(models.Model):
	title = models.CharField(max_length=120)
	customer = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name="customer")
	artist = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name="artist")
	product = models.ForeignKey(Product)
	#order_id = models.CharField(max_length=120, default='ABC', unique=True)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")
	#shipping_address = models.ForeignKey(UserAddress, related_name='shipping_address', default=1)
	#billing_address = models.ForeignKey(UserAddress, related_name='billing_address', default=1)
	#sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	#tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
	#final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	#timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	start_date = models.DateTimeField(default = None)
	complete_date = models.DateTimeField(default = None, null=True, blank=True)
	last_update_date = models.DateTimeField(default = None, null=True, blank=True)
	cover_image = models.ImageField(upload_to='static/images/')
	price = models.DecimalField(default=10.00, decimal_places=2, max_digits = 10, null=True, blank=True)
	addon_1_value = models.BooleanField(default=False)
	addon_2_value = models.BooleanField(default=False)
	addon_3_value = models.BooleanField(default=False)
	addon_4_value = models.BooleanField(default=False)
	addon_5_value = models.BooleanField(default=False)
	addon_6_value = models.BooleanField(default=False)
	extra_notes = models.TextField(default=None, null=True, blank=True)

	def __unicode__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse("order", kwargs={"id": self.id})

class Payment(models.Model):
	def __init__(self, *args, **kwargs):
		super(Payment, self).__init__(*args, **kwargs)
 
		# bring in stripe, and get the api key from settings.py
		import stripe
		stripe.api_key = settings.STRIPE_API_KEY
 
		self.stripe = stripe
 
	# store the stripe charge id for this sale
	charge_id = models.CharField(max_length=32)
 
	# you could also store other information about the sale
	# but I'll leave that to you!
 
	def charge(self, price_in_cents, number, exp_month, exp_year, cvc):
		"""
		Takes a the price and credit card details: number, exp_month,
		exp_year, cvc.
 
		Returns a tuple: (Boolean, Class) where the boolean is if
		the charge was successful, and the class is response (or error)
		instance.
		"""
 
		if self.charge_id: # don't let this be charged twice!
			return False, Exception(message="Already charged.")
 
		try:
			response = self.stripe.Charge.create(
				amount = price_in_cents,
				currency = "usd",
				card = {
					"number" : number,
					"exp_month" : exp_month,
					"exp_year" : exp_year,
					"cvc" : cvc,
 
					#### it is recommended to include the address!
					#"address_line1" : self.address1,
					#"address_line2" : self.address2,
					#"daddress_zip" : self.zip_code,
					#"address_state" : self.state,
				},
				description='Thank you for your purchase!')
 
			self.charge_id = response.id
 
		except self.stripe.CardError, ce:
			# charge failed
			return False, ce
		return True, response