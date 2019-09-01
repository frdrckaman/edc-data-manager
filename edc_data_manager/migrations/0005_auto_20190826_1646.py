# Generated by Django 2.2.3 on 2019-08-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_data_manager", "0004_auto_20190806_1750")]

    operations = [
        migrations.AlterField(
            model_name="historicalqueryrule",
            name="rule_handler_name",
            field=models.CharField(
                choices=[("do_nothing", "Do Nothing"), ("default", "Default")],
                default="default",
                max_length=150,
            ),
        ),
        migrations.AlterField(
            model_name="queryrule",
            name="rule_handler_name",
            field=models.CharField(
                choices=[("do_nothing", "Do Nothing"), ("default", "Default")],
                default="default",
                max_length=150,
            ),
        ),
    ]