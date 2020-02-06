# Create user.
cd /home/serveruser/project/api

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Make migrations
echo "Make database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.filter(username="admin").exists() or \
    User.objects.create_superuser("admin", "admin@example.com", "admin")
EOF

#Start Server
python manage.py runserver 