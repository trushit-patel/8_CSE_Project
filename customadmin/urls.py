from django.conf.urls import url
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/', dashboard, name='dashboard'),
    path('/403', accessdenied, name='403'),
    path('/Banner', banner, name='Banner'),
    path('/signin', login_page, name='signin'),
    path('/dashboard', dashboard, name='dashboard'),
    path('/Product', products, name='Product'),
    path('/users', users, name='users'),
    path('/Order', orders, name='Order'),
    path('/Link', links, name='Link'),
    path('/Logo', logo, name='Logo'),
    path('/Navbar', navbar, name='Navbar'),
    path('/Widget', widget, name='Widget'),
    path('/Offer', offer, name='Offer'),
    path('/PaymentPartners', paymentPartners, name='PaymentPartners'),
    path('/Policy', policy, name='Policy'),
    path('/WidgetNewsLetter', newsletterWidget, name='WidgetNewsLetter'),
    path('/CheckOutDetails', checkoutDetails, name='CheckOutDetails'),
    path('/Footer', footer, name='Footer'),
    path('/Category', category, name='Category'),
    path('/CartItem', cartitems, name='CartItem'),
    path('/LineItem', lineitems, name='LineItem'),
    path('/Contact', contact, name='Contact'),
    path('/PageSection', pageSection, name='PageSection'),
    path('/About', about, name='About'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)