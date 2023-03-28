from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


# TYPE_POST = [
#     ('article', 'статья'),
#     ('news', 'новость'),
# ]


class Author(models.Model):
    # связь «один к одному» с встроенной моделью пользователей User
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # type: User
    author_rating = models.IntegerField(default=0)  # рейтинг пользователя

    def update_rating(self):
        # суммарный рейтинг каждой статьи автора умножается на 3
        # суммарные рейтинги всех комментариев автора;
        # суммарный рейтинг всех комментариев к статьям автора
        rating_posts_author = Post.objects.filter(author_id=self.pk).aggregate(post_rating=Sum('post_rating'))['post_rating']  # noqa: E501
        rating_comments_author = Comment.objects.filter(user_id=self.user).aggregate(comment_rating=Sum('comment_rating'))['comment_rating']  # noqa: E501
        rating_comments_posts = Comment.objects.filter(post__author__user=self.user).aggregate(comment_rating=Sum('comment_rating'))['comment_rating']  # noqa: E501

        self.author_rating = rating_posts_author * 3 + rating_comments_author + rating_comments_posts  # noqa: E501
        self.save()
        return self.author_rating


class Category(models.Model):
    # sport = 'SP'
    # politics = 'PO'
    # education = 'ED'
    # weather = 'WE'

    # CATEGORY_TYPES = [
    #     (sport, 'Спорт'),
    #     (politics, 'Политика'),
    #     (education, 'Образование'),
    #     (weather, 'Погода'),
    # ]

    category_name = models.CharField(max_length=25,
                                     # choices=CATEGORY_TYPES,
                                     # default=sport,
                                     # unique=True
                                     )

    def __str__(self):
        return self.category_name.title()


class Post(models.Model):
    article = 'ARTI'
    news = 'NEWS'

    POST_TYPE = [
        (article, 'Статья'),
        (news, 'Новость')
    ]
    # связь один ко многим с Author
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    types = models.CharField(max_length=4, choices=POST_TYPE, default=news)
    data_create = models.DateField(auto_now_add=True)
    # Связь «многие ко многим» с моделью Category(с доп. моделью PostCategory)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255, blank=False)
    text = models.TextField(blank=False)
    post_rating = models.IntegerField(default=0)  # рейтинг статьи/новости

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        # который возвращает начало статьи (предварительный просмотр) длиной
        # 124 символа и добавляет многоточие в конце.
        return self.text[:124] + '...'

    def __str__(self):
        return f'{self.title}: {self.text[:20]}...'


class PostCategory(models.Model):
    # связь «один ко многим» с моделью Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # связь «один ко многим» с моделью Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    # связь «один ко многим» с моделью Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # связь «один ко многим» со встроенной моделью User (комментарии может
    #  оставить любой пользователь, необязательно автор)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=False)
    date_create = models.DateField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)  # рейтинг комментария

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
