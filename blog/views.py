from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    # Django will automatically use 'object' as the context variable.

class BlogCreateView(CreateView):
    model = BlogPost
    template_name = 'blog_create.html'
    fields = ['title', 'author', 'content','published_date']
    # After successfully creating a post, redirect to the blog list.
    success_url = reverse_lazy('blog-list')
