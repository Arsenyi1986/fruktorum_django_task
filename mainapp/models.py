import opengrapher
from django.contrib.auth.models import User

from django.db import models
import requests
from bs4 import BeautifulSoup


class Collection(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Link(models.Model):
    url = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.parse_and_save()

    def parse_and_save(self):
        opengraph_data = opengrapher.parse(self.url)
        metadata = self.get_metadata()

        ParsedData.objects.create(
            link=self,
            title=opengraph_data.get("title", metadata.get("title", "")),
            description=opengraph_data.get("description", metadata.get("description", "")),
            link_type=opengraph_data.get("type", metadata.get("type", "")),
            image=opengraph_data.get("image", metadata.get("image", ""))
        )

    def get_metadata(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('meta', property='og:title')
        description = soup.find('meta', property='og:description')
        image = soup.find('meta', property='og:image')
        site_type = soup.find('meta', property='og:type')

        return {
            "title": title.get('content') if title else "",
            "description": description.get('content') if description else "",
            "type": site_type.get('content') if site_type else "",
            "image": image.get('content') if image else ""
        }


class ParsedData(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link_type_choices = [
        ('website', 'Website'),
        ('book', 'Book'),
        ('article', 'Article'),
        ('music', 'Music'),
        ('video', 'Video'),
    ]
    link_type = models.CharField(max_length=10, choices=link_type_choices, default='website', blank=True, null=True)
    image = models.ImageField(max_length=255, blank=True, null=True)
    collections = models.ManyToManyField(Collection, blank=True)

    def __str__(self):
        return f"{self.link.url} - {self.title}"




