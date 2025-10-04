from django import forms
from .models import ContactInquiry, Service

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'phone', 'service_interested',
                  'property_type', 'timeline', 'budget_range', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(555) 123-4567'}),
            'service_interested': forms.Select(attrs={'class': 'form-control'}),
            'property_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Home, Office, Retail'}),
            'timeline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Within 2 weeks'}),
            'budget_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., $1,000 - $5,000'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your project...'}),
        }
