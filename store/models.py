from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Student(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='имя')
    second_name = models.CharField(max_length=200, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)  # РАСПАКОВЫВАЕМ СЛОВАРЬ

    is_active = models.BooleanField(default=True, verbose_name='учится')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('second_name',)


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.URLField(max_length=100, verbose_name='адрес')
    massage = models.CharField(max_length=100, verbose_name='краткое описание')

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('name',)


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name="название")
    description = models.TextField(verbose_name='описание')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='студент')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
