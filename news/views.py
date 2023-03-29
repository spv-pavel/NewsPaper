from django.views.generic import ListView, DetailView

from .models import Post
from .filters import NewsFilter


class NewsList(ListView):
    # model = Post
    queryset = Post.objects.filter(types='NEWS')
    ordering = '-data_create'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class SearchNewsList(ListView):
    queryset = Post.objects.filter(types='NEWS')
    ordering = '-data_create'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
