# Generated by Django 4.0.6 on 2022-07-15 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_dt', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'my_user',
            },
        ),
    ]
