# Generated by Django 4.2.7 on 2023-12-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hair', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Gallery Image',
                'verbose_name_plural': 'Gallery Images',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='URL')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Pages',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['title'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='galleryphoto',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='photos', to='hair.tag'),
        ),
    ]
