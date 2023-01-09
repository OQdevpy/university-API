# Generated by Django 4.1.1 on 2022-11-03 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_blog_author'),
        ('course', '0003_alter_course_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='blog.tag'),
        ),
    ]