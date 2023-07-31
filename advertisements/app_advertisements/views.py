from django.shortcuts import render


# Create your views here.

class WebViews(object):
    """Web views for the app."""

    def index(request):
        return render(request, "index.html")

    def top_sellers(request):
        return render(request, "top-sellers.html")

    def advertisement(request):
        return render(request, "advertisement.html")

    def login(request):
        return render(request, "login.html")

    def profile(request):
        return render(request, "profile.html")

    def advertisement_post(request):
        return render(request, "advertisement-post.html")

    def register(request):
        return render(request, "register.html")

    def advertisement_ak_74(request):
        return render(request, "advertisement-AK-74.html")

    def fake(request):
        return render(request, "fake.html")
