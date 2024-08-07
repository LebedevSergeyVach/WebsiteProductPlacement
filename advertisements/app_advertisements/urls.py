from django.urls import path
from .views import WebViews


urlpatterns = [
    path("search", WebViews.index, name="search"),

    path('', WebViews.index, name="main-page"),

    path("top-sellers", WebViews.top_sellers, name="top-sellers"),
    path("advertisement/<int:pk>", WebViews.advertisement_view, name="advertisement"),
    path("advertisement-post", WebViews.advertisement_post, name="advertisement-post"),

    path('handler404', WebViews.handler404, name='handler404'),


    path('maps', WebViews.maps, name="maps"),
    path('map-sib-sety', WebViews.map_sib_sety, name='map-sib-sety'),
    path('map-rostelecom', WebViews.map_sib_sety, name='map-rostelecom'),

    path('WindowsProducts', WebViews.handler404, name="WindowsProducts"),

    path('Kirill-go-fuck-yourself', WebViews.handler404, name="Kirill-go-fuck-yourself"),
]
