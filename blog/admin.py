from django.contrib import admin
from .models import Post


# Register and customize your models here so that they show up on the Admin site
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Display posts as a list with certain fields only
    list_display = ('title', 'slug', 'author', 'publish', 'status',)
    # Filters available for the list
    list_filter = ('status', 'created', 'publish', 'author',)
    # Search fields available
    search_fields = ('title', 'body')
    # Fields that are going to be auto populated
    prepopulated_fields = {'slug': ('title',)}
    # Raw ID Fields
    raw_id_fields = ('author',)
    # Date hierarchy for display
    date_hierarchy = 'publish'
    # Order
    ordering = ('status', 'publish',)
