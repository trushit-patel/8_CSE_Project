from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

class CheckOutDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CheckOutDetails._meta.fields]

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'product']


class LineItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'date_added', 'order']

class LogoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Logo._meta.fields]

class LinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Link._meta.fields]

class NavbarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Navbar._meta.fields]

class WidgetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Widget._meta.fields]

class WidgetNewsLetterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WidgetNewsLetter._meta.fields]

class FooterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Footer._meta.fields]

class PaymentPartnersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PaymentPartners._meta.fields]

class PolicyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Policy._meta.fields]

class BannerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Banner._meta.fields]

class OfferAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Offer._meta.fields]

class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]

class PageSectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PageSection._meta.fields]

class AboutAdmin(admin.ModelAdmin):
    list_display = [field.name for field in About._meta.fields]


admin.site.register(Product, ProductAdmin)
admin.site.register(CheckOutDetails, CheckOutDetailsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CartItem, OrderItemAdmin)
admin.site.register(LineItem, LineItemAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Widget, WidgetAdmin)
admin.site.register(WidgetNewsLetter, WidgetNewsLetterAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(PaymentPartners, PaymentPartnersAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(PageSection, PageSectionAdmin)
admin.site.register(About, AboutAdmin)