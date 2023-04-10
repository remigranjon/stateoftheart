# Generated by Django 4.1.6 on 2023-03-28 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_author_article_header_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='domain',
            field=models.CharField(choices=[('Chemistry', 'Chemistry'), ('Environment and Ecology', 'Environment and Ecology'), ('Physics', 'Physics'), ('Biological Sciences', 'Biological Sciences'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Systems Engineering', 'Systems Engineering'), ('Mathematical Sciences', 'Mathematical Sciences'), ('Astronomy and Astrophysics', 'Astronomy and Astrophysics'), ('Earth Sciences', 'Earth Sciences'), ('Information Sciences', 'Information Sciences'), ('Nuclear and Particle Physics', 'Nuclear and Particle Physics'), ('Other', 'Other')], default='Other', max_length=250),
        ),
    ]
