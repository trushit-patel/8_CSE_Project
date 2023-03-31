from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class Filter(forms.Form):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    min_price = forms.DecimalField(max_digits=10, decimal_places=2)
    max_price = forms.DecimalField(max_digits=10, decimal_places=2)

class CartForm(forms.Form):
    quantity = forms.IntegerField(initial='1')
    product_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CartForm, self).__init__(*args, **kwargs)


class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckOutDetails
        fields = '__all__'
        exclude = ('user','id')

class PayMentForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('payment_method','order_note')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']