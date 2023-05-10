# Generated by Django 4.2 on 2023-05-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('text', models.TextField(verbose_name='disc')),
            ],
            options={
                'ordering': ['email'],
            },
        ),
    ]
