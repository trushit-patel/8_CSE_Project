from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=191)
    postedBy = models.CharField(max_length=191)
    postedOn = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True)
    text = models.TextField()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name= 'products')
    description = models.TextField()
    shortdes = models.CharField(max_length=191)
    discount = models.IntegerField(default=0)
    sale_price = models.DecimalField(max_digits=7, decimal_places=2 ,default= 0.0)
    image = models.ImageField(upload_to='products_images/', blank=True)
    stock = models.IntegerField(default= 10)
    feature_product = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def set_user(self, user):
        self.user = user

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()

    def total_cost(self):
        return self.quantity * self.price

class CheckOutDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'checkout_details')
    first_name = models.CharField(max_length=191)
    last_name = models.CharField(max_length=191)
    email = models.EmailField()
    address = models.CharField(max_length=191)
    city = models.CharField(max_length=255)
    country = CountryField()
    zip_code = models.CharField(max_length=20)
    phn = models.CharField(max_length=20)

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_note = models.TextField(blank= True, null= True ,  default="")

    class PaymentMethod(models.TextChoices):
        COD = 'cd', 'Cash On Delivery'
        CREDIT_CARD = 'cc', 'Credit Card'
        DEBIT_CARD = 'dc', 'Debit Card'
        PAYPAL = 'pp', 'PayPal'
        STRIPE = 'st', 'Stripe'
        APPLE_PAY = 'ap', 'Apple Pay'
        GOOGLE_PAY = 'gp', 'Google Pay'
        UPI = 'up', 'UPI'

    payment_method = models.CharField(max_length=2, choices=PaymentMethod.choices)

    def set_user(self, user):
        self.user = user

    def __str__(self):
        return "{}:{}".format(self.id, self.user)

    def total_cost(self):
        return sum([li.cost() for li in self.lineitem_set.all()])


class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}:{}".format(self.product.name, self.id)

    def cost(self):
        return self.price * self.quantity


class Logo(models.Model):
    logo = models.ImageField(upload_to='logo/', blank=True)
    logo_url = models.CharField(max_length=255)

class Link(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name + ":" + self.url

class Navbar(models.Model):
    logo = models.OneToOneField(Logo, on_delete=models.PROTECT, related_name= 'nav_bar')
    links = models.ManyToManyField(Link)

class Widget(models.Model):
    heading = models.CharField(max_length=10)
    links = models.ManyToManyField(Link)

class WidgetNewsLetter(models.Model):
    heading = models.CharField(max_length=10)
    text = models.CharField(max_length=255, null=True, blank=True)

class Footer(models.Model):
    logo = models.OneToOneField(Logo, on_delete=models.PROTECT, related_name= 'footer')
    moto = models.CharField(max_length=255)
    widgets = models.ManyToManyField('Widget', related_name='footer')
    payment_partners = models.ManyToManyField('PaymentPartners', related_name='footer')
    news_letter = models.OneToOneField(WidgetNewsLetter, on_delete=models.PROTECT, related_name= 'footer')
    footer_text = models.TextField( default="Copyright © 2023 All rights reserved | This template is made with <3 by Colorlib")

class PaymentPartners(models.Model):
    url = models.CharField(max_length=255)
    partner = models.ImageField(upload_to='payment_partners/', blank=True, null=True)

class Policy(models.Model):
    title = models.CharField(max_length=100)
    policyName = models.CharField(unique=True, max_length = 100)
    text = models.TextField()

class Banner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='banners/', blank=True, null=True)

class Contact(models.Model):
    title = models.CharField(max_length=255)
    map = models.CharField(max_length=1000, null= True, blank= True)
    text = models.TextField()

class PageSection(models.Model):
    text = models.TextField()

class About(models.Model):
    title = models.CharField(max_length=255)
    sections = models.ManyToManyField(PageSection, related_name= 'About')

class Offer(models.Model):
    name = models.CharField(max_length=255)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name= 'offer')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()
    on_display = models.BooleanField(unique=True, default=False)

    def is_active(self):
        return timezone.now() < self.expiration

    def time_remaining(self):
        return (self.expiration - timezone.now()).total_seconds() * 1000

    def delete_if_expired(self):
        if not self.is_active():
            self.delete()