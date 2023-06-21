# Generated by Django 4.2.2 on 2023-06-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(to='posts.category'),
        ),
    ]