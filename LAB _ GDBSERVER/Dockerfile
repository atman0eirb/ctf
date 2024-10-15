# Dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update > /dev/null && \
    apt-get install -y \
        python3-pip \
        gdb \
        gdbserver \
        sudo \
    > /dev/null 2>&1 && \
    pip install Flask > /dev/null 2>&1

# Create www-data user and group if they don't exist
RUN getent group www-data || groupadd -r www-data && \
    getent passwd www-data || useradd -r -g www-data www-data

# Copy application files and set ownership
COPY app/ /app
RUN chown -R www-data:www-data /app

# Copy and set permissions for the start script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Run the start script
CMD ["/start.sh"]
