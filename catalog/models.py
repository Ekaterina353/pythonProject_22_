from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


class Product(models.Model):

    name = models.CharField(max_length=250, verbose_name='название', help_text='Введите название')
    description = models.TextField(max_length=250, verbose_name='описание', help_text='Введите описание')
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='фото',
                              help_text='Загрузите фотографию')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='категория',
                                 help_text='Введите категорию', blank=True, null=True)
    price = models.CharField(max_length=100, verbose_name='Цена', help_text='Введите цену', blank=True, null=True)
    created_at = models.DateField(verbose_name='дата создания', help_text='Введите дату создания', blank=True,
                                  null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')  # Добавлено поле Владелец
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')  # Добавлено поле Статус публикации


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),  # Право на отмену публикации
        ]


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='название', help_text='Введите название', blank=True,
                            null=True)
    description = models.TextField(max_length=250, verbose_name='описание', help_text='Введите описание', blank=True,
                                   null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
