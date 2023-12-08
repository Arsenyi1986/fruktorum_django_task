from django.db import models
import opengrapher
from datetime import datetime
from django.utils import timezone

# Create your models here.


class Collection(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    CrDate = models.DateTimeField()
    MdFate = models.DateTimeField()

    def __str__(self):
        return self.Title


class BookMark(models.Model):
    Title = models.CharField(max_length=50, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    Link = models.CharField(max_length=200)
    link_type_choices = [
        ('website', 'Website'),
        ('book', 'Book'),
        ('article', 'Article'),
        ('music', 'Music'),
        ('video', 'Video'),
    ]
    LinkType = models.CharField(max_length=10, choices=link_type_choices, default='website', blank=True, null=True)
    Preview = models.ImageField(max_length=255, blank=True, null=True)
    Collection = models.ManyToManyField(Collection)
    CrDate = models.DateTimeField(auto_now_add=True)
    MdDate = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.Title

    def save(self, *args, **kwargs):
        if self.MdDate is not None:
            self.MdDate = timezone.make_aware(self.MdDate)
        super().save(*args, **kwargs)
        if self.Link:
            parse_and_save(self.Link)

    def clean(self):
        self.MdDate = timezone.make_aware(self.MdDate)


def parse_and_save(url):
    data = opengrapher.parse(url)
    title = data.get("title", "")
    desc = data.get("description", "")
    wurl = data.get("url", "")
    wtype = data.get("type", "")
    preview = data.get("image", "")
    update_at = datetime.now()

    bookMark = BookMark(Title=title, Description=desc,
                        Link=wurl, LinkType=wtype, Preview=preview,
                        MdDate=update_at)
    bookMark.save()
    print("Successssssssssssssssssss")




