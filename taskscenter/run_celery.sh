echo "sleep..."
sleep 30;
echo "begin celery"

celery -A celery_app worker -B -l INFO