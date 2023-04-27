from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MenuItem(MPTTModel):
    name: models.CharField = models.CharField(verbose_name='Имя', max_length=100)
    url: models.CharField = models.CharField(verbose_name='Ссылка', max_length=150)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
