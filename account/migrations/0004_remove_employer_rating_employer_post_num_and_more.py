# Generated by Django 4.2.2 on 2023-07-04 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('util', '0001_initial'),
        ('account', '0003_alter_userable_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='rating',
        ),
        migrations.AddField(
            model_name='employer',
            name='post_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employer',
            name='rating_sum',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userable',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userable',
            name='interest',
            field=models.ManyToManyField(blank=True, related_name='interests', to='util.interest'),
        ),
    ]