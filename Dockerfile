FROM python:3.9

WORKDIR /framework

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["test.py"]