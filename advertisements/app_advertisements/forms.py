from django import forms
from .models import Advertisement


class AdvertisementForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if title.startswith('?'):
            raise forms.ValidationError("Title cannot start with a question mark")

        return title
