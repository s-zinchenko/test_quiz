# Generated by Django 2.2.10 on 2021-11-11 05:57

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
                ('text', models.CharField(max_length=512, verbose_name='Текст ответа')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=512, verbose_name='Текст вопроса')),
                ('answer_type', models.CharField(choices=[('TEXT', 'Text answer'), ('ONE', 'One answer'), ('MULTIPLE', 'Multiple answers')], max_length=64, verbose_name='Тип ответа')),
                ('answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='core.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswersRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название опроса')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Время начала')),
                ('end_date', models.DateTimeField(verbose_name='Время окончания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_questions', to='core.Question')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='responded_users',
            field=models.ManyToManyField(related_name='answers', through='core.UserAnswersRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]