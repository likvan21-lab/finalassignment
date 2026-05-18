from django import forms
from .models import Product
from .models import Category
from .models import Supplier


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

class SupplierForm(forms.ModelForm):

    class Meta:
        model = Supplier
        fields = '__all__'
class StockForm(forms.Form):

    product = forms.ModelChoiceField(queryset=Product.objects.all())

    quantity = forms.IntegerField()

    action = forms.ChoiceField(
        choices=[
            ('IN', 'Stock In'),
            ('OUT', 'Stock Out')
        ]
    )