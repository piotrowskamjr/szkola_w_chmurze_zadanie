from rest_framework import serializers
from url_shortener.models import Url
from url_shortener.utils import get_server


class UrlSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    @staticmethod
    def get_short_url(obj):
        server = get_server()
        return f'{server}{obj.short_url_alias}'

    class Meta:
        model = Url
        fields = ['original_url', 'short_url']
        read_only_fields = ['short_url']
        extra_kwargs = {'original_url': {'write_only': True}}
