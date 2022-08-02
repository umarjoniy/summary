# Generated by Django 4.0.6 on 2022-07-29 18:30

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Another',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awards', models.IntegerField()),
                ('projects', models.IntegerField()),
                ('customers', models.IntegerField()),
                ('coffee', models.IntegerField()),
                ('available', models.CharField(max_length=50)),
                ('sub_available', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('about', models.CharField(max_length=150)),
                ('text', models.TextField(max_length=200)),
                ('media', models.ImageField(upload_to='medias')),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=75)),
                ('title', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='awards')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='education')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=75)),
                ('title', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='experience')),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='partners')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('context', models.TextField()),
                ('ico', models.ImageField(upload_to='services')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('num', models.IntegerField()),
                ('is_main', models.BooleanField(default=False)),
                ('lwnum', models.IntegerField(blank=True, default=None, null=True)),
                ('lmnum', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects')),
                ('name', models.CharField(max_length=75)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.skills')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=150)),
                ('content', ckeditor.fields.RichTextField(null=True)),
                ('paragraph', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('tags', models.ManyToManyField(to='home.tags')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='me')),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('phone', models.CharField(max_length=25)),
                ('completed', models.IntegerField()),
                ('partners', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.partners')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.posts')),
            ],
        ),
    ]
