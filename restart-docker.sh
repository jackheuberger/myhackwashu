echo "checking updates..."
pip install -r requirements.txt
echo "checking updates...done"
echo "migrating db..."
python manage.py makemigrations
python manage.py migrate sessions
python manage.py migrate
python manage.py migrate applications
echo "migrating db...done"
echo "collecting static..."
#python manage.py collectstatic --no-input
echo "collecting static...done"
echo "removing all pyc..."
find . -name \*.pyc -delete
echo "removing all pyc...done"
echo "Deploy completed. The game is on!"

echo "creating superuser..."

#if [ "$DJANGO_SUPERUSER_USERNAME" ]
#then
#    python manage.py createsuperuser \
#        --noinput \
#        --email "organizer@hackwashu.com" \
#        --name "organizer@hackwashu.com" || true
#fi
