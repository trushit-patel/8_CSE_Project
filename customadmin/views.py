from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.admin.sites import site
from ecommerce_app.models import *
from ecommerce_app.forms import *
from ecommerce_app.decorators import *
from django.forms.models import modelform_factory
from django.conf import settings
# Create your views here.

def get_form_class(model):
    return modelform_factory(model, exclude=[])

def login_page(request):

    try:
        if request.user.is_authenticated:
            return redirect('dashboard')
        # messages.info(request, 'Account not found')
        if request.method == 'POST':
            username = request. POST.get('username')
            password = request. POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, 'Account not found')
                return redirect(request. META.get('HTTP_REFERER'))
            user_obj = authenticate(username = username, password=password)
            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('dashboard')
            messages.info(request, 'Invalid password')
            return redirect('signin')
        return render (request, 'admin/login.html')
    except Exception as e:
        print (e)
    return render(request, 'admin/login.html')

@admin_only
def dashboard(request):
    users = User.objects.count()
    orders_count = Order.objects.count()
    orders_with_payment = Order.objects.filter(payment_status = True).count()
    bounce_rate = int(orders_with_payment/orders_count * 100)
    orders = [ int(order.total_cost()) for order in Order.objects.all()]
    print(orders)
    context = {'orders':orders, 'users':users, 'orders_count':orders_count, 'bounce_rate':bounce_rate}
    return render(request, 'admin/dashboard.html', context)

@admin_only
def products(request):
    products = Product.objects.all()
    productForm = ProductForm()
    id = None
    product = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        product = Product.objects.get(id = id)
        productForm = ProductForm(instance=product)

    elif request.GET.get('func') == 'delete':
        product = Product.objects.get(id = request.GET.get('id'))
        product.delete()

        return redirect('Product')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            product = Product.objects.get(id = request.GET.get('id'))
            productForm = ProductForm(request.POST, instance= product)
        else:
            productForm = ProductForm(request.POST)
        if productForm.is_valid():
            print('valid')
            product =  productForm.save(commit=False)
            product.image = request.FILES.get('image')
            product.save()
            return redirect('Product')
        else:
            print(productForm.errors)

    context = {'products': products, 'productForm':productForm ,'id':id}
    return render(request, 'admin/products.html', context)

@admin_only
def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'admin/users.html', context)

@admin_only
def orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'admin/orders.html', context)

@admin_only
def logo(request):
    logos = Logo.objects.all()
    form = get_form_class(model=Logo)
    id = None
    logo = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        logo = Logo.objects.get(id = id)
        form = form(instance=logo)

    elif request.GET.get('func') == 'delete':
        logo = Logo.objects.get(id = request.GET.get('id'))
        logo.delete()

        return redirect('Logo')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            logo = Logo.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= logo)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            logo =  form.save(commit=False)
            logo.logo = request.FILES.get('logo')
            logo.save()
            return redirect('Logo')
        else:
            print(form.errors)

    context = {'logos': logos, 'form':form, 'id':id}
    return render(request, 'admin/logos.html', context)

@admin_only
def links(request):
    objects = Link.objects.all()
    form = get_form_class(model=Link)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = Link.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = Link.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('Link')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = Link.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('Link')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/links.html', context)

@admin_only
def navbar(request):
    objects = Navbar.objects.all()
    form = get_form_class(model=Navbar)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = Navbar.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = Navbar.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('Navbar')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = Navbar.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('Navbar')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/navbar.html', context)

@admin_only
def widget(request):
    objects = Widget.objects.all()
    form = get_form_class(model=Widget)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = Widget.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = Widget.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('Widget')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = Widget.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('Widget')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/widgets.html', context)

@admin_only
def paymentPartners(request):
    objects = PaymentPartners.objects.all()
    form = get_form_class(model=PaymentPartners)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = PaymentPartners.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = PaymentPartners.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('PaymentPartners')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = PaymentPartners.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            object =  form.save(commit=False)
            object.partner = request.FILES.get('partner')
            object.save()
            return redirect('PaymentPartners')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/payment-partners.html', context)

@admin_only
def newsletterWidget(request):
    objects = WidgetNewsLetter.objects.all()
    form = get_form_class(model=WidgetNewsLetter)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = WidgetNewsLetter.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = WidgetNewsLetter.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('WidgetNewsLetter')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = WidgetNewsLetter.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('WidgetNewsLetter')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/newsletter-widget.html', context)

@admin_only
def checkoutDetails(request):
    objects = CheckOutDetails.objects.all()
    form = get_form_class(model=CheckOutDetails)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = CheckOutDetails.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = CheckOutDetails.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('CheckOutDetails')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = CheckOutDetails.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('CheckOutDetails')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/checkout-details.html', context)

@admin_only
def footer(request):
    objects = Footer.objects.all()
    form = get_form_class(model=Footer)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = Footer.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = Footer.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('Footer')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = Footer.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('Footer')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/footer.html', context)

@admin_only
def category(request):
    objects = Category.objects.all()
    form = get_form_class(model=Category)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = Category.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = Category.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('Category')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = Category.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('Category')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/categories.html', context)

@admin_only
def policy(request):
    objects = Policy.objects.all()
    form = get_form_class(model=Policy)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = Policy.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = Policy.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('Policy')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = Policy.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('Policy')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/policy.html', context)

@admin_only
def offer(request):
    objects = Offer.objects.all()
    form = get_form_class(model=Offer)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = Offer.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = Offer.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('Offer')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = Offer.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('Offer')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/offer.html', context)

@admin_only
def banner(request):
    objects = Banner.objects.all()
    form = get_form_class(model=Banner)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = Banner.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = Banner.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('Banner')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = Banner.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('Banner')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/banner.html', context)

@admin_only
def contact(request):
    objects = Contact.objects.all()
    form = get_form_class(model=Contact)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = Contact.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = Contact.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('Contact')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = Contact.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('Contact')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/contact.html', context)

@admin_only
def pageSection(request):
    objects = PageSection.objects.all()
    form = get_form_class(model=PageSection)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = PageSection.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = PageSection.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('PageSection')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = PageSection.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('PageSection')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/page-section.html', context)

@admin_only
def about(request):
    objects = About.objects.all()
    form = get_form_class(model=About)
    id = None
    object = None

    if request.GET.get('func') == 'edit':
        id = request.GET.get('id')
        object = About.objects.get(id = id)
        form = form(instance=object)

    elif request.GET.get('func') == 'delete':
        object = About.objects.get(id = request.GET.get('id'))
        object.delete()

        return redirect('About')

    if request.method == 'POST':
        if request.GET.get('id') != 'None':
            object = About.objects.get(id = request.GET.get('id'))
            form = form(request.POST, instance= object)
        else:
            form = form(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('About')
        else:
            print(form.errors)

    context = {'objects': objects, 'form':form, 'id':id}
    return render(request, 'admin/about.html', context)

@admin_only
def lineitems(request):
    lineitems = LineItem.objects.all()
    context = {'lineitems': lineitems}
    return render(request, 'admin/lineitems.html', context)

@admin_only
def cartitems(request):
    cartitems = CartItem.objects.all()
    context = {'cartitems': cartitems}
    return render(request, 'admin/cartitems.html', context)

def accessdenied(request):
    return render(request, '403.html')