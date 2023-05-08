from django.urls import path, include

urlpatterns = [
    path('', include('url_shortener.urls'))
]
