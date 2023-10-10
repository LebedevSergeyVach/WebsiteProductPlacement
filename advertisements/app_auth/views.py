from datetime import datetime

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import MyUserCreationForm


# Create your views here.


class WebView(object):
    """View class for auth pages"""

    @login_required(login_url=reverse_lazy('login'))
    def profile_view(request):
        """View function for profile page"""
        return render(
            request, 'app_auth/profile.html'
        )

    def login_view(request):
        """View function for login page"""
        redirect_url = reverse("profile")

        if request.method == "GET":
            if request.user.is_authenticated:
                return redirect(redirect_url)
            else:
                return render(
                    request, "app_auth/login.html"
                )

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request, username=username, password=password,
        )

        # DEBUG
        now = datetime.now()
        print(
            f'# Пользователь вошел в аккаунт: [{now.strftime("%Y-%m-%d %H:%M:%S")}]\n'
            f'Username: {username} Password: {password}'
        )

        if user is not None:
            login(request, user)
            return redirect(redirect_url)

        context = {"error": "Вы не зарегистрировались или неверно вели данные 🥲🥲🥲"}

        return render(
            request, "app_auth/login.html", context=context
        )

    def logout_view(request):
        """View function for logout page"""
        logout(request)

        # DEBUG
        now = datetime.now()
        print(f'# Пользователь вышел из аккаунта: [{now.strftime("%Y-%m-%d %H:%M:%S")}] ')

        return redirect(reverse('login'))

    def register_view(request):
        """View function for register page"""
        if request.method == "POST":
            form = MyUserCreationForm(request.POST)

            if form.is_valid():
                user = form.save()
                user = authenticate(
                    username=user.username, password=request.POST["password1"]
                )
                login(request, user=user)

                # DEBUG
                now = datetime.now()
                print(
                    f'# Пользователь зарегистрировался: [{now.strftime("%Y-%m-%d %H:%M:%S")}]\n'
                    f'Username: {user} Password: {request.POST["password1"]}'
                )

                return redirect(reverse("profile"))

        else:
            form = MyUserCreationForm()

        context = {"form": form}

        return render(
            request, "app_auth/register.html", context=context
        )

