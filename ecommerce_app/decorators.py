from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from . import cart

def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users (allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/404')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('403')
        elif request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('403')
    return wrapper_function

def cart_has_items(view_func):
    def wrapper_function(request, *args, **kwargs):
        if cart.item_count(request) > 0:
            return view_func(request,*args,**kwargs)
        else:
            return HttpResponse("your cart is empty")
    return wrapper_function
