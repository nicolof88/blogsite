from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create a custom manager to retrieve only published posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# Post Model for posts
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # Title of post
    title = models.CharField(max_length=250)
    # Slug for unique identifier on the URL
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # Author of the post is going to be a User from the auth system
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # Body of the post
    body = models.TextField()
    # Post dates
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # Define model managers
    objects = models.Manager()
    published = PublishedManager()

    # Additional info to organize the model
    class Meta:
        # By default, order model by desc publish date
        ordering = ('-publish',)

    def __str__(self):
        return self.title
