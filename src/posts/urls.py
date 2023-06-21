from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogListCategory, BlogPostDetailView

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('<str:category>/<str:slug>', BlogPostDetailView.as_view(), name='post'),
    path('category', BlogListCategory.as_view(), name='blog_category'),
    path('create', BlogPostCreate.as_view(), name='create'),
]