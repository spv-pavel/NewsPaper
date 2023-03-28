from django.views.generic import ListView, DetailView

from .models import Post


class NewsList(ListView):
    # model = Post
    queryset = Post.objects.filter(types='NEWS')
    ordering = '-data_create'
    template_name = 'news.html'
    context_object_name = 'news'


class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
