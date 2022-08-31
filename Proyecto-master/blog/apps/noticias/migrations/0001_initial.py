# Generated by Django 3.2.14 on 2022-08-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('creado', models.DateField(auto_now_add=True)),
                ('cuerpo', models.TextField()),
                ('autor', models.CharField(max_length=50, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='noticias')),
            ],
        ),
    ]
