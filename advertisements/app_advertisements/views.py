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
                print(
                    f"# Пользователь выложил объявление:\n"
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
