from django.db import models


class Course(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', max_length=1000)
    image = models.ImageField('Изображение', upload_to='main_app/courses')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'Курс {self.title}'
