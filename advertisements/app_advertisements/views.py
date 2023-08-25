from django.shortcuts import render, redirect, reverse

from .models import Advertisement
from .forms import AdvertisementForm

# Create your views here.


class WebViews(object):
    """Web views for the app."""

    def index(request):

        advertisements = Advertisement.objects.all()
        context = {
            'advertisements': advertisements
        }

        return render(
            request, "index.html", context=context
        )

    def top_sellers(request):
        return render(
            request, "top-sellers.html"
        )

    def advertisement(request):
        return render(
            request, "advertisement.html"
        )

    def login(request):
        return render(
            request, "login.html"
        )

    def profile(request):
        return render(
            request, "profile.html"
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

    def register(request):
        return render(
            request, "register.html"
        )

    def advertisement_ak_74(request):
        return render(
            request, "advertisement-AK-74.html"
        )

    def advertisement_laptop(request):
        return render(
            request, "advertisement-laptop.html"
        )

    def advertisement_rtx(request):
        return render(
            request, "advertisement-rtx.html"
        )

    def fake(request):
        return render(
            request, "fake.html"
        )


def advertisement_post(request):

    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)

        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)

    else:
        form = AdvertisementForm()

    context = {'form': form}

    return render(
        request, "advertisement-post.html", context=context
    )