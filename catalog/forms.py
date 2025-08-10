from django import forms
from .models import Product, Category


class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ['title', 'content', 'image', 'created_at', 'publication_sign', 'count_of_views']


class CategorytForm(forms.Form):
    class Meta:
        model = Category
        fields = ['name', 'description']
