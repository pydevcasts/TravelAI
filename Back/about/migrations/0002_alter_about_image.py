from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="about/%Y/%m/%d"),
        ),
    ]
