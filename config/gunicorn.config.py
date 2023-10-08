# Change directory to specified directory before loading apps.
chdir = "app"
# Define the host and port for your application.
bind = ["0.0.0.0:8000"]
# Number of worker processes.
workers = 2
# Number of threads per worker (only applicable to certain worker classes).
threads = 2
# Set the worker class. You can use "sync", "eventlet", "gevent", or other options.
worker_class = "gevent"
# Timeout for handling a request.
timeout = 30

# Log settings (customize log file and log level as needed).
# accesslog = "/path/to/access.log"
# errorlog = "/path/to/error.log"

# How verbose the Gunicorn error logs should be
loglevel = "debug"

# default is the send error log to stdout
# errorlog = '-'
# accesslog = '-'
# Whether to send flask output to the error log
capture_output = True
# hot reload
reload = True

# Path to the virtual environment, if applicable.
# Uncomment the line below and replace "/path/to/venv" with your actual virtual environment path.
# pythonpath = "/path/to/venv"

# Additional environment variables (optional).
# env = {
#     "VAR_NAME": "value",
#     "ANOTHER_VAR": "another_value",
# }

# SSL settings (uncomment if using HTTPS).
# keyfile = "/path/to/ssl_key.pem"
# certfile = "/path/to/ssl_cert.pem"

# Enable graceful restarts.
# graceful_timeout = 10
