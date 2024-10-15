#!/bin/sh

# Start SSH server
service ssh start

# Switch to www-user and run the application
exec su www-user -c "python /app/app.py"
