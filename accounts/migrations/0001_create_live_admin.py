from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()

    # --- IMPORTANT: CHANGE YOUR ADMIN DETAILS HERE ---
    # Replace 'admin' with the username you want.
    # Replace the email with your email.
    # Replace the password with a strong password.
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin1',
            email='admin@gmail.com',
            password='admin1@123'
        )

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(create_superuser),
    ]