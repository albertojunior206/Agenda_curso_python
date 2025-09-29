from django import forms
from . import models
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category'
        )

    def clean(self):
        cleaned_data = self.cleaned_data

        return super().clean()