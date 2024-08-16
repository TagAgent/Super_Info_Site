from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Hashtag(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Хэштэги'
        verbose_name = 'Хэштэг'


class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='publications', verbose_name='Категория', null=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='Hashtags', null=True)

    title = models.CharField(verbose_name='Название', max_length=50)
    short_description = models.CharField(verbose_name='Краткое содержание', max_length=200)
    description = models.TextField(verbose_name='Полное содержание')
    image = models.ImageField(verbose_name='Изображение')
    created_date = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_hidden = models.BooleanField(verbose_name='Скрыта', default=False)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'


class PublicationComment(models.Model):
    publication = models.ForeignKey(Publication, verbose_name='Публикация', on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(verbose_name='Имя автора', max_length=50, default='anonymous')
    text = models.TextField(verbose_name='Текст', default='I hacked this world')
    created_date = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'


class Feedback(models.Model):
    user_name = models.CharField(verbose_name='Имя автора', max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    text = models.TextField(verbose_name='Текст')
