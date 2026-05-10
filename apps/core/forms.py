from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone Number (Optional)'}),
            'subject': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'How can we help you?', 'rows': 5}),
        }
