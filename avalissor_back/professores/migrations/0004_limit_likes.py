# Generated by Django 5.0.6 on 2024-06-24 01:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0003_created_comment_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='likescomentarios',
            constraint=models.UniqueConstraint(fields=('comentario', 'autor'), name='Apenas um like por comentario'),
        ),
    ]
