from django import forms
from .models import PickupRequest

class PickupRequestForm(forms.ModelForm):
    class Meta:
        model = PickupRequest
        fields = ['item_name','quantity','pickup_address','description']