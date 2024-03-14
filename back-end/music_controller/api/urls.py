
from django.urls import path
from .views import main # from the same folder's views file import the function 'main'

urlpatterns = [
    path('home/', main),
]
