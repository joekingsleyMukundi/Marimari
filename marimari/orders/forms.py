# from django import forms
# # https://blog.kwetuhub.com/creating-shopping-cart-views-shop-products-django-2-0-python-3-6/

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)