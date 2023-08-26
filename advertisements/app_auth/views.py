from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


class WebView(object):
    """View class for auth pages"""

    def profile_view(request):
        """View function for profile page"""
        return render(request, 'app_auth/profile.html')

    def login_view(request):
        """View function for login page"""
        redirect_url = reverse('profile')

        if request.method == 'GET':

            if request.user.is_authenticated:
                return redirect(redirect_url)

            else:
                return render(request, 'app_auth/login.html')

        username = request.POST['username']
        contact = request.POST['contact']
        password = request.POST['password']

        user = authenticate(
            username=username, contact=contact, password=password
        )

        if user is not None:
            login(request, user)
            return redirect(redirect_url)

        context = {'error': 'Пользователь не найден!'}

        return render(request, 'app_auth/login.html', context=context)

    def logout_view(request):
        """View function for logout page"""
        logout(request)

        return redirect(reverse('login'))

    def register_view(request):
        """View function for registration page"""
        return render(request, 'app_auth/register.html')
