# Generated by Django 4.1.7 on 2023-02-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField(max_length=600)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]