from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['product'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['price_achat'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['price_vente'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['remise'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = Stock
        fields = ['name', 'quantity', 'product','price_achat', 'price_vente', 'remise']