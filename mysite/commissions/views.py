from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Tag, Fandom
from mysite.forms import SearchForm, SalePaymentForm
from orders.models import Order, Payment
from accounts.models import UserStore
from django.contrib.auth.decorators import login_required


def index(request):

	# Category 1: recently completed commissions
	# Get 4 most recently updated commissions, in order of recency
	orders = Order.objects.all()
	mostRecentOrders = Order.objects.order_by('-updated')[:4]

	# Category 2: popular commission slots
	# Get 4 top commissions based on # of completed orders
	mostPopularCommissions = Product.objects.order_by('-orders_completed')[:4]

	# Category 3: popular tags
	# Get 4 m ost popular tags based on # of commissions attached to them
	# Also get most popular commission associated with each tag
	mostPopularTags = Tag.objects.order_by('-num_commissions')[:4]
	mostPopularTagCommissions = []
	for tag in mostPopularTags:
		mostPopularTagCommissions.append(Product.objects.filter(tags__title=tag).order_by('-orders_completed')[0])

	# Category 4: new commission slots 
	# Get 4 most recently created commission slots 
	mostRecentCommissions = Product.objects.order_by('-created_at')[:4]

	return render(request, 'index.html', 
		{'form': SearchForm(), 
		'resultsRecentlyUpdatedOrders': mostRecentOrders,
		'resultsMostPopularCommissions': mostPopularCommissions,
		'resultsMostPopularTags': mostPopularTags,
		'resultsMostPopularTagCommissions': mostPopularTagCommissions,
		'resultsMostRecentCommissions': mostRecentCommissions
		}
	)

def commission(request, id):
	commission = Product.objects.all().get(id = id)
	artist_id = commission.owner.id
	store = UserStore.objects.all().get(owner__id=artist_id)
	latest_orders = Order.objects.all().filter(artist__id = artist_id).order_by('-last_update_date')[0:4]
	active_orders = Order.objects.all().filter(artist__id = artist_id).filter(status = "In Progress").order_by('-last_update_date')

	return render(request, 'products/commission_info.html', {'id': id, 'store': store, 'latest_orders': latest_orders, 'commission': commission, 'active_orders': active_orders});

def create_request(request, id):
	commission = Product.objects.all().get(id = id)
	
	if request.method == 'POST':
		request_form = SalePaymentForm(request.POST)

		if request_form.is_valid(): # charges the card
			return render(request, 'checkout/order_confirmation.html', {'message': 'SUCCESS'});
		else:
			return render(request, 'checkout/order_confirmation.html', {'message': 'FAILURE'});
	else:	
		request_form = SalePaymentForm()

	return render(request, 'checkout/order_form_1.html', {'id': id, 'commission': commission, 'request_form': request_form});

def request_confirmation(request, id):
	commission = Product.objects.all().get(id = id)
	return render(request, 'checkout/order_confirmation.html', {'message': 'SUCCESS'});


# Create your views here.

def search(request):
	
	context = {}
	context['categories'] = Category.objects.all()
	context['fandoms'] = Fandom.objects.all()

	results, searchingOnProduct = initialize_results(request, context)
	context, results = filter_results(results, request, context, searchingOnProduct)

	order_by = request.GET.get('order_by', None)
	if order_by == "popular":
		if searchingOnProduct:
			results = results.order_by('-orders_completed')
		else:
			results = results.order_by('-product__orders_completed')
	elif order_by == "new":
		results = results.order_by('-id')	
	context['order_by'] = order_by

	context['results'] =  results	
	context['form'] = SearchForm()
	
	return render(request, 'products/search.html', context)

def initialize_results(request, context):
	
	# get search for objects
	results = Product.objects.all()
	searchingOnProduct = True
	if 'search_for' in request.GET:
		context['search_for'] = request.GET['search_for']
		if context['search_for'] == "commission":
			results = Product.objects.all()
		elif context['search_for'] == "order":
			results = Order.objects.all()
			searchingOnProduct = False

	return results, searchingOnProduct

def update_context_and_results(request, param, subfield, operation, context, results, paramToMatch = None):
	if param in request.GET:
		value = request.GET[param]
		context[param] = value
		if paramToMatch is not None:
			param = paramToMatch
		results = filter_results_helper(results, param, value, operation, subfield)
	return context, results

def filter_results_helper(results, param, value, operation, field=None):

	if field is not None:
		kwargs = {
			'{0}__{1}__{2}'.format(param, field, operation): value
		}
	else:
		kwargs = {
			'{0}__{1}'.format(param, operation): value
		}
	return results.filter(**kwargs)

def filter_results(results, request, context, searchingOnProduct):
	valid_fields_for_filter = ['category', 'fandom', 'query', 'priceMin', 'priceMax']
	sub_fields_for_filter = ['title', 'title', None, None, None]
	operations_for_filter = ['iexact', 'iexact', 'icontains', 'gte', 'lte']
	params_for_match = [None, None, 'title', 'price', 'price']
	query_on_product = [True, True, False, True, True]
	for i in range(len(valid_fields_for_filter)):
		if query_on_product[i] and not searchingOnProduct:
			params_for_match[i] = "product__" + valid_fields_for_filter[i]
		context, results = update_context_and_results(
			request, 
			valid_fields_for_filter[i], 
			sub_fields_for_filter[i], 
			operations_for_filter[i],
			context, 
			results,
			params_for_match[i]
		)
	return context, results