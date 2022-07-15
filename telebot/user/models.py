from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(max_length=100, verbose_name='Email')
    password = models.CharField(max_length=50, verbose_name='Password')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    updated_dt = models.DateTimeField(auto_now=True, verbose_name='Updated Date')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'my_user'