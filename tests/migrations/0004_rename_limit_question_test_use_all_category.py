# Generated by Django 5.1.2 on 2024-10-29 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tests", "0003_alter_test_description_alter_test_num_essay_question_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="test",
            old_name="limit_question",
            new_name="use_all_category",
        ),
    ]
