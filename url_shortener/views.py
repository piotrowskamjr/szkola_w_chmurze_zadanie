from django.http import HttpResponseRedirect
from rest_framework import generics

from url_shortener.models import Url
from url_shortener.serializers import UrlSerializer


class CreateUrlMap(generics.CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class RedirectToOriginalUrl(generics.RetrieveAPIView):
    queryset = Url.objects.all()
    lookup_field = 'short_url_alias'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return HttpResponseRedirect(instance.original_url)
