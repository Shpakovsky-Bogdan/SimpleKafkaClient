FROM python:alpine
WORKDIR /app
COPY Consumer.py .
RUN pip install kafka-python
CMD [ "python", "Consumer.py" ]