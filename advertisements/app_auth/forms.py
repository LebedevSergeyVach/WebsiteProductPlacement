from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    """Custom user creation form."""

    def __init__(self, *args, **kwargs):
        """Create a new"""
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["first_name"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["last_name"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["password1"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["password2"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["email"].widget.attrs["class"] = "form-control form-control-lg"

    class Meta:
        """Meta class for user creation form."""
        model = User
        fields = [
            "username", "email", "first_name", "last_name", "password1", "password2"
        ]