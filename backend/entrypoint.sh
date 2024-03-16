#!/bin/bash

# Wait until the database service is ready
while !</dev/tcp/db/5432; do sleep 1; done

# Apply Django migrations
python manage.py migrate

# Create default superuser (replace values as needed)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Run Django tests
python manage.py test

# Start Django server
python manage.py runserver 0.0.0.0:8000
