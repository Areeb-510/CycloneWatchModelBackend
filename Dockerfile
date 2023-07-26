FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install tensorflow-intel
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*
COPY . .
EXPOSE 8000
CMD ["gunicorn", "cyclonewatch.wsgi:application", "--bind", "0.0.0.0:8000"]