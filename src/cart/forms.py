from django import forms

BOOK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 100)]


class CartAddBookForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=BOOK_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)