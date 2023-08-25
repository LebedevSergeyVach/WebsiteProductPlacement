from django.urls import path

from .views import WebViews, advertisement_post


urlpatterns = [
    path("search", WebViews.index, name="search"),

    path('', WebViews.index, name="main-page"),
    path("top-sellers", WebViews.top_sellers, name="top-sellers"),

    path("advertisement", WebViews.advertisement, name="advertisement"),
    path("advertisement-post", advertisement_post, name="advertisement-post"),

    path("advertisement-AK-74", WebViews.advertisement_ak_74, name="advertisement-AK-74"),
    path("advertisement-laptop", WebViews.advertisement_laptop, name="advertisement-laptop"),
    path("advertisement-rtx", WebViews.advertisement_rtx, name="advertisement-rtx"),

    path("login", WebViews.login, name="login"),
    path("profile", WebViews.profile, name="profile"),
    path("register", WebViews.register, name="register"),

    path("fake", WebViews.fake, name="fake"),
]
