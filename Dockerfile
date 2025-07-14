FROM python:3.9-slim
WORKDIR /app
COPY ..
RUN pip install requirements.txt
CMD ["python", "manage.py"]