web: gunicorn manage:app --worker-class=gevent --workers 4
worker: worker: celery -A tasks worker --loglevel=info -E -P gevent -c 15 --without-gossip --without-mingle --without-heartbeat
