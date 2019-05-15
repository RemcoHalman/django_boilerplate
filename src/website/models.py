from django.db import models
from django.core.validators import URLValidator, FileExtensionValidator
from django.contrib.auth.models import User

from PIL import Image
from datetime import datetime

# Getting custom apps
from taggit.managers import TaggableManager
from colorfield.fields import ColorField
from tinymce.models import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = HTMLField(null=True, blank=True)
    background_image = models.ImageField(
        upload_to="page_bg_images/%Y/",
        max_length=255,
        null=True,
        blank=False,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg", "gif"])
        ],
    )
    date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.background_image.path)
        basewidth = 2048
        if img.height > basewidth or img.width > basewidth:
            wpercent = basewidth / float(img.size[0])
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img.save(self.background_image.path)


class Testimonial(models.Model):
    content = models.TextField()
    writer = models.CharField(max_length=100)
    verification_url = models.CharField(max_length=1000, validators=[URLValidator()])
    writer_profile_image = models.ImageField(
        upload_to="writer_testemonial_images/%Y/",
        max_length=255,
        default="default.jpg",
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg", "gif"])
        ],
    )
    backgroundColor = ColorField(default="#fff")

    def __str__(self):
        return self.writer

    def save(self):
        super().save()

        # img = self.writer_profile_image
        img = Image.open(self.writer_profile_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.writer_profile_image.path)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    background_image = models.ImageField(
        upload_to="blogpost_bg_images/%Y/",
        max_length=255,
        null=True,
        blank=False,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg", "gif"])
        ],
    )
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.background_image.path)
        basewidth = 720
        if img.height > basewidth or img.width > basewidth:
            wpercent = basewidth / float(img.size[0])
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img.save(self.background_image.path)


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    project_image = models.ImageField(
        upload_to="project_images/%Y/",
        max_length=255,
        null=True,
        blank=False,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg", "gif"])
        ],
    )
    content = models.TextField()
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.project_image.path)

        if img.height > 1280 or img.width > 1280:
            basewidth = 1280
            wpercent = basewidth / float(img.size[0])
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), Image.ANTIALIAS)
            img.save(self.project_image.path)


# video_background =  models.FileField(upload_to='bg_video/', max_length=255, null=True, blank=True,
#                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
