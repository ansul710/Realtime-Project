from django.urls import path

from .consumers import WSConsumer
# from .consumers import WSNewConsumer

ws_urlpatterns = [
    path('ws/xyz_url/', WSConsumer.as_asgi()),
    # path('ws/abc_url/', WSNewConsumer.as_asgi()),
]
