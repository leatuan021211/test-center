# Generated by Django 5.1.2 on 2024-10-30 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0005_rename_num_fill_bank_question_test_num_fill_blank_question"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="test",
            name="random_question",
        ),
    ]
