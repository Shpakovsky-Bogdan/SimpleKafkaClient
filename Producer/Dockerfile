FROM python:alpine
WORKDIR /app
COPY Producer.py .
RUN pip install kafka-python
CMD [ "python", "Producer.py" ]