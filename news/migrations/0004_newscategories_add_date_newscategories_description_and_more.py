# Generated by Django 4.0.2 on 2022-03-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_category_newscategories_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='newscategories',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='newscategories',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='newscategories',
            name='image',
            field=models.ImageField(default='', upload_to='Categories/'),
        ),
    ]
