from django.urls import include, path
from django.contrib import admin

from .views import WebViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path("search", WebViews.index, name="search"),

    path('', WebViews.index, name="main-page"),

    path("top-sellers", WebViews.top_sellers, name="top-sellers"),
    path("advertisement/<int:pk>", WebViews.advertisement_view, name="advertisement"),
    path("advertisement-post", WebViews.advertisement_post, name="advertisement-post"),

    path('handler404', WebViews.page_not_found_view, name='page-not-found'),
]
