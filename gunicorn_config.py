import os

workers = int(os.environ.get('GUNICORN_PROCESS', '2'))
threads = int(os.environ.get('GUNICORN_THREADS', '4'))

forwarded_allow_ips = '*'

secure_scheme_headers = {'X-Forwarded-Proto': 'https'}
