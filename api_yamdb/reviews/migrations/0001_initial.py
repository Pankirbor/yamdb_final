# Generated by Django 3.2 on 2023-03-27 17:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import reviews.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=256, verbose_name='название категории'
                    ),
                ),
                (
                    'slug',
                    models.SlugField(
                        unique=True, verbose_name='слаг категории'
                    ),
                ),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        max_length=256, verbose_name='название жанра'
                    ),
                ),
                (
                    'slug',
                    models.SlugField(unique=True, verbose_name='слаг жанра'),
                ),
            ],
            options={
                'verbose_name': 'жанр',
                'verbose_name_plural': 'жанры',
            },
        ),
        migrations.CreateModel(
            name='GenreTitle',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'genre',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='reviews.genre',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        db_index=True,
                        max_length=256,
                        verbose_name='название тайтла',
                    ),
                ),
                (
                    'year',
                    models.IntegerField(
                        validators=[reviews.validators.year_validator],
                        verbose_name='год выпуска',
                    ),
                ),
                ('description', models.TextField(verbose_name='описание')),
                (
                    'category',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='titles',
                        to='reviews.category',
                    ),
                ),
                (
                    'genre',
                    models.ManyToManyField(
                        related_name='titles',
                        through='reviews.GenreTitle',
                        to='reviews.Genre',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'pub_date',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Дата добавления'
                    ),
                ),
                ('text', models.TextField(verbose_name='текст отзыва')),
                (
                    'score',
                    models.IntegerField(
                        default=1,
                        help_text='Поставьте оценку от 1 до 10',
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name='оценка',
                    ),
                ),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reviews',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'title',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='reviews',
                        to='reviews.title',
                    ),
                ),
            ],
            options={
                'verbose_name': 'отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
        migrations.AddField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='reviews.title'
            ),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'pub_date',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Дата добавления'
                    ),
                ),
                ('text', models.TextField(verbose_name='текст отзыва')),
                (
                    'author',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'review',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='comments',
                        to='reviews.review',
                    ),
                ),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(
                fields=('author', 'title'), name='unique_review'
            ),
        ),
        migrations.AddConstraint(
            model_name='genretitle',
            constraint=models.UniqueConstraint(
                fields=('title', 'genre'), name='unique_title_genre'
            ),
        ),
    ]