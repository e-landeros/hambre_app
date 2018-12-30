from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hambreApp.forms import UserForm, RestaurantForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return redirect(restaurant_home)

@login_required(login_url='login')
def restaurant_home(request):
    return render(request, 'restaurant/home.html', {})

def restaurant_registration(request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()

    return render(request, 'restaurant/register.html', {
        "user_form": user_form,
        "restaurant_form":restaurant_form
    })