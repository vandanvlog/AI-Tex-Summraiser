FROM python:3.8-slim-buster

# Install required system packages for building wheels
RUN apt update -y && apt install -y \
    gcc \
    g++ \
    build-essential \
    cmake \
    git \
    curl \
    awscli

WORKDIR /app

COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install Python packages
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]
