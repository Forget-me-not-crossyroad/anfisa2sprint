from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Название категории, не более 256 символов',
    )
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Слаг',
        help_text='Уникальное название категории',
    )
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения',
        help_text='Число порядка отображения, дефолтное значение 100',
    )

    class Meta:
        verbose_name = 'объект «Категория»'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Название топпинга, не более 256 символов',
    )
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Слаг',
        help_text='Уникальное название топпинга',
    )

    class Meta:
        verbose_name = 'объект «Топпинг»'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Название обёртки, не более 256 символов',
    )

    class Meta:
        verbose_name = 'объект «Упаковка»'
        verbose_name_plural = 'Упаковки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Название мороженого, не более 256 символов',
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Описание мороженого',
    )
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Упаковка',
        help_text='Название обёртки',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория',
        help_text='Название категории',
    )
    toppings = models.ManyToManyField(
        Topping, verbose_name='Топпинг', help_text='Название топпингов'
    )
    is_on_main = models.BooleanField(
        default=False,
        verbose_name='На главную',
        help_text='Чек-бокс: включить / выключить отображение на главной странице',
    )

    class Meta:
        verbose_name = 'объект «Мороженое»'
        verbose_name_plural = 'Мороженое'

    def __str__(self):
        return self.title
