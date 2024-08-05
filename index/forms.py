from django import forms
from .models import ContactForm, BilingForm

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = ContactForm
        fields = ['name','email','message']


class ShippingForm(forms.ModelForm):
    
    class Meta:
        model = BilingForm
        fields = ['name','email','phone','address','city','state','code']