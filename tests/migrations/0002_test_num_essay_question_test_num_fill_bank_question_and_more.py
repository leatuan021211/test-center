# Generated by Django 5.1.2 on 2024-10-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="test",
            name="num_essay_question",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="test",
            name="num_fill_bank_question",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="test",
            name="num_multiple_answer_question",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="test",
            name="num_multiple_choice_question",
            field=models.IntegerField(default=0),
        ),
    ]
