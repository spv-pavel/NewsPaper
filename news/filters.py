from django_filters import FilterSet  # импортируем filter set, чем-то напоминающий знакомые дженерики

from .models import Post


# создаём фильтр
class NewsFilter(FilterSet):
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться)
    # информация о товарах
    class Meta:
        model = Post
        # Поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
        fields = {
            'data_create': ['gt'],
            'title': ['icontains'],
            'author': ['exact'],
        }
