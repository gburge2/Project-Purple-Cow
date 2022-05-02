FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

run pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver" , "0.0.0.0:3000"] 
