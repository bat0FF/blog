# Generated by Django 4.2.3 on 2024-09-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options_post_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DF', 'Черновик'), ('PB', 'Опубликовать')], default='PB', max_length=2, verbose_name='Статус'),
        ),
    ]
