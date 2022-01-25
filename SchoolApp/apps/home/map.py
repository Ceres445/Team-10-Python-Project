from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.public_api.models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "http"

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return f"/posts/{obj.id}"


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return ["homePage", "register"]

    def location(self, item):
        return reverse(item)
