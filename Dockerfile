FROM python:3.8-slim-buster

# ✅ Step 1: Install required build tools
RUN apt update -y && apt install -y gcc g++ build-essential cmake

# ✅ Step 2: Set working directory
WORKDIR /app

# ✅ Step 3: Copy all project files
COPY . /app

# ✅ Step 4: Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ✅ Step 5: Ensure correct transformers versions
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

# ✅ Step 6: Run your FastAPI or Python app
CMD ["python3", "app.py"]
