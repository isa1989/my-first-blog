# Generated by Django 2.0.4 on 2018-10-25 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_word_word_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='letter',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='connect', to='polls.Letter'),
        ),
    ]