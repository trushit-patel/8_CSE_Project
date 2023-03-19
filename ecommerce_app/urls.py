from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-page', views.admin_dashboard, name='admin'),
    path('product/<int:product_id>/<slug:product_slug>',views.show_product, name='product_detail'),
    path('cart', views.show_cart, name='show_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('shop', views.shop, name='shop'),
    path('orders', views.orders, name='orders'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('register', views.register, name='register'),
    path('base', views.loadStatic, name='base'),
    path('order/<int:order_id>',views.show_order, name='order_detail'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog/<int:blog_id>', views.blog_details, name='blog_details'),
    path('contact', views.contact, name='contact'),
    path('privacy-policy', views.privacy, name='privacy-policy'),
    path('refund-policy', views.refund, name='refund-policy'),
    path('shipping-policy', views.shipping, name='shipping-policy'),
    path('terms-of-service', views.serviceTerms, name='terms-of-service'),
    path('403', views.accessdenied, name='403'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)