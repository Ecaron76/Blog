from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, CreateView, DetailView
from posts.models import BlogPost, Category
from django.http import JsonResponse



# Create your views here.
def latest_posts_context(request):
    return {
        'latest_posts': BlogPost.get_latest_posts(),
    }

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset



class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__slug=self.kwargs['category'], slug=self.kwargs['slug'])
        return queryset

class BlogListCategory(ListView):
    model = Category
    template_name = "category_list"
    context_object_name = "categories"

class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title','description', 'content', 'category', 'created_on' ]