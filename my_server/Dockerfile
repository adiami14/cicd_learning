FROM python:3.10-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
# Expose the service port
EXPOSE 5000