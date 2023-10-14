FROM python:3.11
WORKDIR app
COPY . /app
RUN pip install -r requirements.txt 
EXPOSE 8001
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py runserver
