# Generated by Django 3.2 on 2021-07-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('singer', models.CharField(default='', max_length=100)),
                ('genre', models.CharField(default='', max_length=50)),
                ('composer', models.CharField(default='', max_length=30)),
                ('rel_date', models.CharField(default='', max_length=10)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='musicBlog/')),
            ],
        ),
    ]
