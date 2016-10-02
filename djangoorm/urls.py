from django.conf.urls import url, include

urlpatterns = [
    url(r'^game/', include('game.urls')),
]
