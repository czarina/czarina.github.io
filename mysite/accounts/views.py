from django.shortcuts import render
from .models import UserStore
from updates.models import Update, UpdateImage, Review
from orders.models import Order
from commissions.models import Product
from itertools import chain

# Create your views here.
def store(request, id):
	store = UserStore.objects.all().get(id = id)
	lastUpdateImages = store.updateimage_set.all().order_by('-update__created_at')[0:2]
	products = store.owner.product_set.all()
	productsAndVariants = []
	allActiveOrders = []
	for product in products:
		productVariants = product.productvariant_set.all()
		# get # of active orders
		activeOrders = product.order_set.all().filter(status="In Progress")
		numActiveOrders = activeOrders.count()
		numOpenOrders = product.slots - numActiveOrders
		productsAndVariants.append({'product': product, 'variants': productVariants, 'activeOrders': numActiveOrders, 'openOrders': numOpenOrders})
		allActiveOrders = list(chain(allActiveOrders, activeOrders))
	# get slots taken
	return render(request, 'stores/store_home.html', {'id': id, 'store': store, 'allActiveOrders': allActiveOrders, 'updates': lastUpdateImages, 'productsAndVariants': productsAndVariants}
	)

def store_portfolio(request, id):
	store = UserStore.objects.all().get(id = id)
	artist_id = UserStore.objects.all().get(id = id).owner.id
	orders = Order.objects.all().filter(artist__id = artist_id).order_by('-last_update_date')
	products = Product.objects.all().filter(owner__id = artist_id)
	ordersByProduct = []
	for product in products:
		ordersByProduct.append({'product': product, 'orders': orders.filter(product = product)})
	return render(request, 'stores/store_portfolio.html', {'id': id, 'orders': ordersByProduct, 'store': store}
	)

def store_feed(request, id):
	store = UserStore.objects.all().get(id = id)
	updates = store.update_set.all().filter(sender_is_artist = True).order_by('-created_at')
	updatesWithImages = []
	for update in updates:
		images = update.updateimage_set.all()
		updatesWithImages.append({'update': update, 'images': images})
	return render(request, 'stores/store_feed.html', {'id': id, 'updates': updatesWithImages, 'store': store}
	)

def store_reviews(request, id):
	store = UserStore.objects.all().get(id = id)
	reviews = Review.objects.all().filter(store__id = id)
	return render(request, 'stores/store_reviews.html', {'id': id, 'reviews': reviews, 'store': store}
	)

def store_about(request, id):
	store = UserStore.objects.all().get(id = id)
	return render(request, 'stores/store_about.html', {'id': id, 'store': store, 'store': store}
	)