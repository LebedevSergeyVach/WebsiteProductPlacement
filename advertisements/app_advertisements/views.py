from django.shortcuts import render, redirect, reverse

from .models import Advertisement
from .forms import AdvertisementForm

# Create your views here.


class WebViews(object):
    """Web views for the app."""

    def index(request):
        """Renders the index page."""
        advertisements = Advertisement.objects.all()
        context = {
            'advertisements': advertisements
        }

        return render(
            request, "app_advertisement/index.html", context=context
        )

    def top_sellers(request):
        """Renders the top sellers page."""
        return render(
            request, "app_advertisement/top-sellers.html"
        )

    def advertisement(request):
        """Renders the advertisement page."""
        return render(
            request, "app_advertisement/advertisement.html"
        )

    def advertisement_post(request):
        """Renders the advertisement post page."""
        if request.method == "POST":
            form = AdvertisementForm(request.POST, request.FILES)

            if form.is_valid():
                advertisement = form.save(commit=False)
                advertisement.user = request.user
                advertisement.save()
                url = reverse("main-page")

                return redirect(url)

        else:
            form = AdvertisementForm()

        context = {'form': form}

        return render(
            request, "app_advertisement/advertisement-post.html", context=context
        )

    def advertisement_ak_74(request):
        """Renders the advertisement AK-74 page."""
        return render(
            request, "app_dop/advertisement-AK-74.html"
        )

    def advertisement_laptop(request):
        """Renders the advertisement laptop page."""
        return render(
            request, "app_dop/advertisement-laptop.html"
        )

    def advertisement_rtx(request):
        """Renders the advertisement rtx page."""
        return render(
            request, "app_dop/advertisement-rtx.html"
        )

    def fake(request):
        """Renders the fake page."""
        return render(
            request, "app_dop/fake.html"
        )


# def advertisement_post(request):
#
#     if request.method == 'POST':
#         form = AdvertisementForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             advertisement = Advertisement(**form.cleaned_data)
#             advertisement.user = request.user
#             advertisement.save()
#             url = reverse('main-page')
#             return redirect(url)
#
#     else:
#         form = AdvertisementForm()
#
#     context = {'form': form}
#
#     return render(
#         request, "advertisement-post.html", context=context
#     )
