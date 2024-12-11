from django.db import models
from django.contrib.auth.models import AbstractUser

class categories(models.Model):
    name = models.CharField('Категория', max_length=100, unique=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
class ychebniki(models.Model):
    author = models.CharField('Автор', max_length=150)
    description = models.TextField('Описание', blank=True, null=True)
    img = models.ImageField('Изображение', upload_to='images', blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdf', blank=True, null=True)
    category = models.ForeignKey(to=categories, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.author
    
    class Meta:
        db_table = 'ychebniki'
        verbose_name = 'Учебник'
        verbose_name_plural = 'Учебники'

        
class User(AbstractUser):
    text = models.TextField('Заметки', blank=True, null=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


class Favorite(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=ychebniki, on_delete=models.CASCADE)

class Help(models.Model):
    name = models.TextField('Имя', max_length=150, blank=True, null=True)
    email = models.TextField('Почта', max_length=150, blank=True, null=True)
    topik = models.TextField('Тема', max_length=150, blank=True, null=True)
    HelpText = models.TextField('Текст сообщения', blank=True, null=True)

    class Meta:
        db_table = 'Help'
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    