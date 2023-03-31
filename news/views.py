from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .filters import NewsFilter
from .forms import NewForm


class NewsListView(ListView):
    queryset = Post.objects.filter(types='NEWS')
    template_name = 'news/news.html'
    context_object_name = 'news'
    ordering = '-data_create'
    paginate_by = 10


class SearchNewsListView(ListView):
    queryset = Post.objects.filter(types='NEWS')
    ordering = '-data_create'
    template_name = 'news/search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewDetailView(DetailView):
    model = Post
    template_name = 'news/new.html'
    form_class = NewForm
    context_object_name = 'new'


class NewAddCreateView(CreateView):
    template_name = 'news/new_add.html'
    form_class = NewForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_types = 'NEWS'
        # post.author = ???
        return super().form_valid(form)


class NewUpdateView(UpdateView):
    template_name = 'news/new_edit.html'
    form_class = NewForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте,
    # который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewDeleteView(DeleteView):
    template_name = 'news/new_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    context_object_name = 'new'
