FROM python:3.7
ADD . /tmp
WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

CMD python -u consumer.py 
