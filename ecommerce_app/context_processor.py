from . import cart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import *

def cart_item_count(request):

    item_count = cart.item_count(request)
    return {'cart_item_count' : item_count }

def context_processor_1(request):
    navbar = Navbar.objects.all().first()
    #first_object = MyModel.objects.order_by('-created_at').first()
    footer = Footer.objects.all().first()
    return {'navbar' : navbar,'footer':footer }