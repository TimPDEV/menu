from django.db import models


class Menu(models.Model):
    name = models.CharField('Название', max_length=150)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='items',
        verbose_name='Меню'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        verbose_name='Родитель', blank=True, null=True
    )
    name = models.CharField('Название', max_length=150)
    slug = models.SlugField('URL', unique=True)

    @property
    def level(self):
        if self.parent:
            return self.parent.level + 1
        return 1

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
