# Generated by Django 5.0 on 2023-12-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_image',
            field=models.ImageField(blank=True, null=True, upload_to='curriculum/media/curriculum'),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_position',
            field=models.CharField(choices=[('DevOps', 'DevOps'), ('Software Engineer', 'Software Engineer'), ('Project Manager', 'Project Manager'), ('ServiceNow Monitoring Integration', 'ServiceNow Monitoring Integration')], max_length=50),
        ),
    ]
