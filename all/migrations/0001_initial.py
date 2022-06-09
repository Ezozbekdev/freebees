# Generated by Django 4.0.5 on 2022-06-08 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=199)),
                ('short', models.TextField()),
                ('imgs', models.ImageField(upload_to='about_img')),
                ('text', models.TextField()),
                ('happy_clents', models.IntegerField(default=0)),
                ('awords', models.IntegerField(default=0)),
                ('complated_project', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=169)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Img_profile')),
                ('title', models.CharField(max_length=150)),
                ('dic', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=240)),
                ('img', models.ImageField(upload_to='user-img')),
                ('age', models.DateField(default=14)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img-blog')),
                ('title', models.CharField(max_length=550)),
                ('started', models.CharField(max_length=5550)),
                ('body', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='all.user')),
            ],
        ),
    ]
