from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    """Form for creating new advertisements"""
    class Meta:
        model = Advertisement
        fields = [
            'title', 'description', 'image', 'price', 'auction',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_title(self):
        """Validate that the title is not empty and does not start with a question mark"""
        title = self.cleaned_data.get('title')

        if title.startswith('?'):
            raise forms.ValidationError("Title cannot start with a question mark")

        return title
