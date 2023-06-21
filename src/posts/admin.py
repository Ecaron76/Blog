from django.contrib import admin

from posts.models import BlogPost


# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "published",
        "author",
        "created_on",
        "last_updated",
        "published"
    )

    empty_value_display = "Inconnu"

    list_editable = ("published", "slug",)
    search_fields = ("title",)
    list_filter = ("published", "author",)
    autocomplete_fields = ("author",)
    filter_horizontal = ("category",)
    list_per_page = 10