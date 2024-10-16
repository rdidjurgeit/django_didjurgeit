# Generated by Django 4.2.16 on 2024-10-16 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0003_task_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
