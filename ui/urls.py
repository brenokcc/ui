from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('', include('sloth.api.urls')),
    path('', include('sloth.app.urls')),
]
