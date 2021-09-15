# Generated by Django 2.1.10 on 2021-09-15 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='Введите значение', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('description', models.TextField(max_length=1024, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('TEXT', 'TEXT'), ('CHOICE', 'CHOICE'), ('MULTICHOICE', 'MULTICHOICE')], default='TEXT', max_length=11, verbose_name='Тип вопроса')),
                ('text', models.CharField(max_length=256, verbose_name='Текст вопроса')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='polls.Vote'),
        ),
    ]
