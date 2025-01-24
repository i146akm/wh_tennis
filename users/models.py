from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IsActive(models.Model):
    class Meta:
        verbose_name_plural = 'Активные пользователи'
        verbose_name = 'Активные пользователи'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    user_agent = models.CharField(max_length=200, verbose_name='User-Agent пользователя')
    is_active = models.BooleanField(verbose_name='Статус')

    def __str__(self):
        return f'{self.user} | {'Активный' if self.is_active == True else 'Неактивный'}'
    
