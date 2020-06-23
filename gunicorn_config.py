import os
# you can set ENV VARS when you run the image...
backend_host=os.environ.get('BACKEND_HOST', "0.0.0.0")
backend_port=os.environ.get('BACKEND_PORT', "8888")

command = 'gunicorn'
pythonpath = '/code/'
bind = f"{backend_host}:{backend_port}"
workers = 1
#user = 'nobody'
