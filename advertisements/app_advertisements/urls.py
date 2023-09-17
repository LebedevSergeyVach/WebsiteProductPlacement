from django.urls import path

from .views import WebViews


urlpatterns = [
    path("search", WebViews.index, name="search"),

    path('', WebViews.index, name="main-page"),

    path("top-sellers", WebViews.top_sellers, name="top-sellers"),
    path("advertisement/<int:pk>", WebViews.advertisement_view, name="advertisement"),
    path("advertisement-post", WebViews.advertisement_post, name="advertisement-post"),
]
