# Generated by Django 3.1.4 on 2021-01-06 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210106_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='category',
            field=models.ForeignKey(default='General', on_delete=django.db.models.deletion.SET_DEFAULT, to='app.category'),
        ),
    ]