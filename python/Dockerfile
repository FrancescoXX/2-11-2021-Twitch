FROM python:3.6

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 80

CMD ["gunicorn", "--bind","0.0.0.0:80","wsgi:app"]