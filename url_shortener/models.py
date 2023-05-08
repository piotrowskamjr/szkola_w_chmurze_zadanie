from django.db import models
from django.utils.crypto import get_random_string
from url_shortener.utils import TRIALS_NO, SHORT_URL_LENGTH


class Url(models.Model):
    original_url = models.URLField()
    short_url_alias = models.CharField(max_length=15, unique=True)

    @classmethod
    def create_short_url(cls):
        for _ in range(TRIALS_NO):
            random_url_alias = get_random_string(SHORT_URL_LENGTH)
            if cls.objects.filter(short_url_alias=random_url_alias).exists():
                continue
            return random_url_alias

    def save(self, *args, **kwargs):
        short_url_alias = self.__class__.create_short_url()
        if short_url_alias:
            self.short_url_alias = short_url_alias
            super().save(*args, **kwargs)
        else:
            raise KeyError('Cannot generate unique short url')
