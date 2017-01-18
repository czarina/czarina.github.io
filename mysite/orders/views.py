from django.shortcuts import render
from django.http import HttpResponse
from commissions.models import Product, Category, Tag, Fandom
from accounts.models import UserStore
from mysite.forms import SearchForm
from .models import Order
from django.urls import reverse
from updates.models import Review
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def order(request, id):
	order = Order.objects.get(id = id)
	artist = order.artist
	updates = order.update_set.all()
	owner_id = Order.objects.get(id = id).artist.id
	try:
		prev_order = reverse('order', args=[Order.get_previous_by_start_date(order, artist=artist).id])
	except ObjectDoesNotExist:
		prev_order = None 
	try:
		next_order = reverse('order', args=[Order.get_next_by_start_date(order, artist=artist).id])
	except ObjectDoesNotExist:
		next_order = None
	review = Review.objects.get(order__id = order.id)
	store = UserStore.objects.all().get(owner__id = owner_id)

	add_ons = []
	if order.addon_1_value:
		add_ons.append(order.product.addon_1.title)
	if order.addon_2_value:
		add_ons.append(order.product.addon_2.title)
	if order.addon_3_value:
		add_ons.append(order.product.addon_3.title)
	if order.addon_4_value:
		add_ons.append(order.product.addon_4.title)
	if order.addon_5_value:
		add_ons.append(order.product.addon_5.title)
	if order.addon_6_value:
		add_ons.append(order.product.addon_6.title)
	if len(add_ons) == 0:
		add_ons = None
	# # Category 1: recently completed commissions
	# # Get 4 most recently updated commissions, in order of recency
	# orders = Order.objects.all()
	# mostRecentOrders = Order.objects.order_by('-updated')[:4]

	# # Category 2: popular commission slots
	# # Get 4 top commissions based on # of completed orders
	# mostPopularCommissions = Product.objects.order_by('-orders_completed')[:4]

	# # Category 3: popular tags
	# # Get 4 m ost popular tags based on # of commissions attached to them
	# # Also get most popular commission associated with each tag
	# mostPopularTags = Tag.objects.order_by('-num_commissions')[:4]
	# mostPopularTagCommissions = []
	# for tag in mostPopularTags:
	# 	mostPopularTagCommissions.append(Product.objects.filter(tags__title=tag).order_by('-orders_completed')[0])

	# # Category 4: new commission slots 
	# # Get 4 most recently created commission slots 
	# mostRecentCommissions = Product.objects.order_by('-created_at')[:4]

	return render(request, 'orders/order.html', {'store': store, 'add_ons': add_ons, 'review': review, 'order': order, 'updates': updates, 'prev_order': prev_order, 'next_order': next_order}
	)