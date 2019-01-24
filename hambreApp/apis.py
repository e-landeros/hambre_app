from django.http import JsonResponse

from hambreApp.models import Restaurant
from hambreApp.serializers import RestaurantSerializer

# function run on api calls. returns all of the restarants in the DB in json format
def customer_get_restaurant(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("-id"),
        many = True
    ).data

    return JsonResponse({"restaurants": restaurants})