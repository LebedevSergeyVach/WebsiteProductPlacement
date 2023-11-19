from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    """Custom user creation form."""

    def __init__(self, *args, **kwargs):
        """Create a new"""
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = \
            "form-control form-control-lg bg-dark text-light btn-outline-primary"
        self.fields["first_name"].widget.attrs["class"] = \
            "form-control form-control-lg bg-dark text-light btn-outline-primary"
        self.fields["last_name"].widget.attrs["class"] = \
            "form-control form-control-lg bg-dark text-light btn-outline-primary"
        self.fields["password1"].widget.attrs["class"] = \
            "form-control form-control-lg bg-dark text-light btn-outline-primary"
        self.fields["password2"].widget.attrs["class"] = \
            "form-control form-control-lg bg-dark text-light btn-outline-primary"
        self.fields["email"].widget.attrs["class"] = \
            "form-control form-control-lg bg-dark text-light btn-outline-primary"

    class Meta:
        """ Meta class for the UserCreationForm. """
        model = User

        fields = [
            "username", "email", "first_name", "last_name", "password1", "password2",
        ]
