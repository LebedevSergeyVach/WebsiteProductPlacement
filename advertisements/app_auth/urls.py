from django.urls import path

from .views import profile_view, logout_view, login_view, register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),
]
