from django.shortcuts import render
from .models import Restaurant
from django.http import JsonResponse

def restaurant_list(request):

	my_restaurants= []
	for rest in Restaurant.objects.all():
		my_restaurants.append({
			'name': rest.name,
			'description': rest.description,
			})
	return JsonResponse (my_restaurants, safe=False)


def restaurant_detail(request, rest_id):
	restaurant_object= Restaurant.objects.get(id=rest_id)
	my_restaurant= {
		'name' : restaurant_object.name,
		'description': restaurant_object.description,
		'opening_time': restaurant_object.opening_time,
		'closing_time': restaurant_object.closing_time,
	}
	return JsonResponse(my_restaurant)

	
