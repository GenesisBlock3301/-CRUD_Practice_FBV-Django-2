from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    name = forms.CharField()
    pages = forms.IntegerField()
    class Meta: #modification class
        model = Book
        fields = '__all__' #take all fields inside Book models
        # fields =['name', 'pages']
