from django.urls import path

from .views import NewsListView, NewDetailView, SearchNewsListView, NewAddCreateView, NewUpdateView, NewDeleteView

urlpatterns = [
   path('', NewsListView.as_view()),
   path('<int:pk>', NewDetailView.as_view(), name='new'),
   path('search/', SearchNewsListView.as_view()),
   path('add/', NewAddCreateView.as_view(), name='new_add'),
   path('edit/<int:pk>', NewUpdateView.as_view(), name='new_edit'),
   path('delete/<int:pk>', NewDeleteView.as_view(), name='new_delete'),
]
