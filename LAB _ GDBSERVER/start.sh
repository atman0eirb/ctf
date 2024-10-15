#!/bin/bash

# Start gdbserver in the background as root
gdbserver :6048 /bin/sh &

# Run the Flask application as www-data
exec sudo -u www-data flask run --host=0.0.0.0
