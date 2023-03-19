from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib.admin.sites import site
from django.apps import apps

def app_list(request):
    models = [model.__name__ for model in apps.get_app_config('ecommerce_app').get_models()]
    return {'models': models}