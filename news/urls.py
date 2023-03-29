from django.urls import path
from .views import NewsList, NewDetail, SearchNewsList

urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewDetail.as_view()),
   path('search/', SearchNewsList.as_view()),
]
