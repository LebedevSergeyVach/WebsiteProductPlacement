from datetime import datetime

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.db.models import Count

from .models import Advertisement
from .forms import AdvertisementForm


User = get_user_model()
# Create your views here.


class WebViews(object):
    """Web views for the app."""

    def index(request):
        """Renders the index page."""
        title = request.GET.get("query")

        if title:
            advertisements = Advertisement.objects.filter(
                title__icontains=title.strip()
            )
        else:
            advertisements = Advertisement.objects.all()

        context = {"advertisements": advertisements, "title": title}

        return render(
            request, "app_advertisement/index.html", context=context
        )

    def top_sellers(request):
        """Renders the top sellers page."""
        users = User.objects.annotate(
            adv_count=Count("advertisement")
        ).order_by("-adv_count")

        context = {"users": users}

        return render(
            request, "app_advertisement/top-sellers.html", context=context
        )

    def advertisement_view(request, pk):
        """Renders the advertisement page."""
        advertisement = Advertisement.objects.get(pk=pk)

        context = {
            "advertisement": advertisement
        }

        return render(
            request, "app_advertisement/advertisement.html", context=context
        )

    @login_required(login_url=reverse_lazy("login"))
    def advertisement_post(request):
        """Renders the advertisement post page."""
        if request.method == "POST":
            form = AdvertisementForm(request.POST, request.FILES)

            if form.is_valid():
                advertisement = form.save(commit=False)
                advertisement.user = request.user
                advertisement.save()
                url = reverse("main-page")

                # DEBUG
                now = datetime.now()
                print(
                    f'# Пользователь выложил объявление: [{now.strftime("%Y-%m-%d %H:%M:%S")}]\n'
                    f"{advertisement.user} Title: {advertisement.title} "
                    f"Description: {advertisement.description} Price: {advertisement.price} "
                    f"Image: {advertisement.image_1} Auction: {advertisement.auction}"
                )

                return redirect(reverse("main-page"))

        else:
            form = AdvertisementForm()

        context = {'form': form}

        return render(
            request, "app_advertisement/advertisement-post.html", context=context
        )

    def handler404(request, exception):
        """Returns 404 error page."""
        return render(
            request, 'app_advertisement/404.html', status=404
        )

    @login_required(login_url=reverse_lazy("login"))
    def products(request):
        """Returns products list."""
        if request.method == 'GET':
            if request.user.is_superuser:
                return render(
                    request, 'app_advertisement/WindowsProducts.html',
                )
            else:
                return render(
                    request, 'app_advertisement/main.html'
                )

    def maps(request):
        """Returns map"""
        redirect_url = reverse("main-page")

        if request.method == "GET":
            if request.user.is_superuser:
                return render(
                    request, 'maps/maps.html'
                )
            else:
                return redirect(redirect_url)

    def map_sib_sety(request):
        """Returns map sib sety"""
        redirect_url = reverse("main-page")

        if request.method == "GET":
            if request.user.is_superuser:
                return render(
                    request, 'maps/map_sib_sety.html'
                )
            else:
                return redirect(redirect_url)

    def map_rostelecom(request):
        """Returns map rostelecom"""
        redirect_url = reverse("main-page")

        if request.method == "GET":
            if request.user.is_superuser:
                return render(
                    request, 'maps/maps_rostelecom.html'
                )
            else:
                return redirect(redirect_url)
