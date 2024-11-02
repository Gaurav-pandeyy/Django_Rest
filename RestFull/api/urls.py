from tkinter.font import names

from django.urls import path
from tutorial.urls import urlpatterns

from .views import get_users,create_user

urlpatterns = [
    path('users/',get_users,name="get_users"),
    path('users/create/',create_user,name="create_user")
]