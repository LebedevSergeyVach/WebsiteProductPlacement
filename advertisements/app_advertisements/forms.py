from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    """Form for creating new advertisements"""
    class Meta:
        model = Advertisement
        fields = [
            'title', 'description', 'contact', 'image_1', 'image_2', 'image_3', 'price', 'auction',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image_1': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'image_2': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'image_3': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        """Validate that the title is not empty and does not start with a question mark"""
        title = self.cleaned_data.get('title')

        if title.startswith('?'):
            raise forms.ValidationError("Title cannot start with a question mark")

        return title
