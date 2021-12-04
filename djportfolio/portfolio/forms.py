from django import forms

class ContactForm(forms.Form):
    contact_email = forms.EmailField(label='Your email', max_length=254, required=True)
    contact_message = forms.CharField(label='Your name', required=True)
