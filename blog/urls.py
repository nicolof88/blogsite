from django.urls import path
from . import views


# Define the namespace of app to avoid name clashes
app_name = 'blog'

# URL Patterns for blog app
urlpatterns = [
    # Entry point : /blog/
    path('', views.post_list, name="post_list"),
]
