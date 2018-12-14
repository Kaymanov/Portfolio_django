from django.db import models

# Create your models here.

class Work (models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование организации')
    post = models.CharField(max_length=50, verbose_name='Должность')
    date_work = models.CharField(max_length=50, verbose_name='Период работы')
    responsibility = models.TextField(verbose_name='Обязанности')

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"
        ordering = ['name']

    def __str__(self):
        return self.name


