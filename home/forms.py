from . models import Book
from django import forms

class sellbookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name',
            'category',
            'price',
            'image',
            'pickuplocation',
            'college'
        ]
        widgets = {
            'book_name': forms.TextInput(attrs={'placeholder': 'Enter book name'}),
            'category': forms.TextInput(attrs={'placeholder': 'Enter category'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            'pickuplocation': forms.TextInput(attrs={'placeholder': 'Enter pick up location'}),
            'college': forms.TextInput(attrs={'placeholder': 'Enter college name'})  
        }


class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    comment= forms.CharField(label='',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your message here'}))
