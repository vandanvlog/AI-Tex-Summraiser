FROM python:3.8-slim-buster


WORKDIR /app

# Copy all files into the container
COPY . /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Reinstall transformers and accelerate cleanly
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

# Run the FastAPI app or main app
CMD ["python3", "app.py"]
