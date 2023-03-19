from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Product, Order, LineItem
from .forms import *
from . import cart
from .decorators import *

def index(request):
    active_offer = [offer for offer in Offer.objects.filter(on_display=True) if offer.is_active()]
    expiration = active_offer[0].expiration.strftime('%Y/%m/%d') if active_offer else None
    #my_queryset = MyModel.objects.all().order_by('name')
    context = {'banners': Banner.objects.all(),
               'offer': active_offer[0] if active_offer else None,
               'expiration' : expiration
               }
    return render(request, "index.html", context)

@login_required(login_url="/login")
def logoutPage(request):
    logout(request)
    return redirect("/")

@unauthenticated
def loginPage(request):
    
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,'Username or password incorrect')
            return render(request, "login.html")

    return render(request, "login.html")

@unauthenticated
def register(request):
    
    userForm = UserRegisterForm()

    if request.method == 'POST':
        userForm = UserRegisterForm(request.POST)

        if userForm.is_valid():
            user = userForm.save()
            user.groups.add(Group.objects.all()[0])
            messages.success(request,'Your account has been created')

    return render(request, "register.html",{'userForm':userForm})

def shop(request):
    all_products = Product.objects.all()
    return render(request,"shop.html",{'all_products': all_products,})

def show_product(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('show_cart')

    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'shop-details.html', {
                                            'product': product,
                                            'form': form,
                                            })

@login_required(login_url="/login")
def show_cart(request):

    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)

    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    return render(request, 'cart.html', {
                                            'cart_items': cart_items,
                                            'cart_subtotal': cart_subtotal,
                                            })

@admin_only
def admin_dashboard(request):
    return HttpResponse('this is admin page')

def loadStatic(request):
    return render(request,'base.html')


@login_required(login_url="/login")
@cart_has_items
def checkout(request):
    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    checkout = CheckOutDetails.objects.filter(user=request.user).first()
    
    if request.method == 'POST':
        form = CheckOutForm(request.POST)
        paymentForm = PayMentForm(request.POST)

        if form.is_valid() and paymentForm.is_valid():
            
            if checkout:
                checkout.__dict__.update(form.cleaned_data)
            else:
               checkout = CheckOutDetails.objects.create(user=request.user, **form.cleaned_data)

            checkout.save()
            cleaned_data = paymentForm.cleaned_data
            payment_status = True if cleaned_data.get('payment_method') not in ('cd', 'Cash On Delivery') else False

            o = Order(payment_method = cleaned_data.get('payment_method'), user = request.user, payment_status = payment_status)
            o.save()
            
            for cart_item in cart_items:
                li = LineItem(product_id = cart_item.product_id, price = cart_item.price, quantity = cart_item.quantity,order_id = o.id)
                li.save()

            cart.clear(request)
            request.session['order_id'] = o.id

            messages.add_message(request, messages.INFO, 'Order Placed!')
            
        return redirect('show_cart')

    form = CheckOutForm(instance=checkout)
    paymentForm = PayMentForm()
    return render(request, 'checkout.html', {'form': form, 'payment_form':paymentForm , 'cart_items': cart_items, 
                                             'cart_subtotal': cart_subtotal})

@login_required(login_url="/login")
def orders(request):
    orders = Order.objects.filter(user = request.user)
    print(orders.exists())
    return render(request, 'orders.html', {'orders': orders,})

@login_required(login_url="/login")
def show_order(request,order_id,):
    order = get_object_or_404(Order, id = order_id, user = request.user )
    form = CheckOutForm(instance=CheckOutDetails.objects.filter(user=request.user).first())
    return render(request, 'order-details.html', {'order': order,'form': form,})

def about(request):
    about = About.objects.all().first()
    context = {'about': about}
    return render(request,'about.html', context)

def privacy(request):
    policy = Policy.objects.get(policyName = 'privacy')
    context = {'policy': policy}
    return render(request,'privacy-policy.html', context)

def refund(request):
    policy = Policy.objects.get(policyName = 'refund')
    context = {'policy': policy}
    return render(request,'refund-policy.html', context)

def shipping(request):
    policy = Policy.objects.get(policyName = 'shipping')
    context = {'policy': policy}
    return render(request,'shipping-policy.html', context)

def serviceTerms(request):
    policy = Policy.objects.get(policyName = 'serviceterms')
    context = {'policy': policy}
    return render(request,'terms-of-service.html', context)

def blog(request):
    return render(request,'blog.html')

def contact(request):
    contact = Contact.objects.all().first()
    context = {'contact': contact}
    return render(request,'contact.html', context)

def blog_details(request):
    return render(request,'blog-details.html')

def accessdenied(request):
    return render(request, '403.html')