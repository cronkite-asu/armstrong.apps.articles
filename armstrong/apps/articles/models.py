from armstrong.apps.content.models import Content
from armstrong.core.arm_content.mixins.publication import PublishedManager
from django.db import models


class Article(Content):
    body = models.TextField()
    home_summary = models.TextField(blank=True, null=True)
    home_title = models.CharField(max_length=100, blank=True, null=True)

    objects = models.Manager()
    published = PublishedManager()
