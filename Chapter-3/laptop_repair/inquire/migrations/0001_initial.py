# Generated by Django 3.1.6 on 2021-05-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessorieslist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessories_list', models.CharField(max_length=30)),
            ],
        ),
    ]
