gunicorn -b 0.0.0.0:$PORT app:app&
sleep 20
python3 -m client
