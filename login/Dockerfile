FROM python:3.7
ADD . /tmp
WORKDIR /app

COPY  . .
RUN pip install -r requirements.txt

CMD python3 add.py
