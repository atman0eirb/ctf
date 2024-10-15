# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install necessary packages including OpenSSH server
RUN apt-get update && \
    apt-get install -y openssh-server sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create the user and set the password
RUN useradd -m user && \
    echo "user:My@2763JHVGH##~" | chpasswd && \
    mkdir /home/user/.ssh && \
    chmod 700 /home/user/.ssh

# Set up the .reminder file with permissions 777
RUN touch /home/user/.reminder && \
    echo "My@2763JHVGH##~" > /home/user/.reminder && \
    chown user:user /home/user/.reminder && \
    chmod 777 /home/user/.reminder 

# Configure SSH to allow password authentication
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Set the same password for root
RUN echo "root:My@2763JHVGH##~" | chpasswd

RUN echo "Bien joué Mr root !" >> /root/final  | chpasswd



# Create the www-user user and group
RUN groupadd -r www-user && useradd -r -g www-user www-user


# Set up the working directory
WORKDIR /app

# Copy the application files
COPY app/ /app/

RUN chown -R www-user:www-user /app

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the entrypoint script and set permissions
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
