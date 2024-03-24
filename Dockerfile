FROM python:3.9

WORKDIR /framework

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python","test.py"]