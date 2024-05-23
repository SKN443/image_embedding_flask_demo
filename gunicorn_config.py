# gunicorn_config.py

# Bind to a specific IP address and port
bind = '0.0.0.0:5000'

# Number of worker processes
workers = 2

# The type of workers to use (sync, gevent, etc.)
worker_class = 'sync'

# Maximum number of pending connections
backlog = 2048

# Maximum number of requests a worker will process before restarting
max_requests = 1000

# Log level
loglevel = 'info'

# Paths to log files
accesslog = '-'
errorlog = '-'
