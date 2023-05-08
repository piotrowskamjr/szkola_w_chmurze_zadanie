from django.urls import path
from url_shortener.views import CreateUrlMap, RedirectToOriginalUrl

appname = "url_shortener"

urlpatterns = [
    path('<str:short_url_alias>', RedirectToOriginalUrl.as_view()),
    path('', CreateUrlMap.as_view()),
]
