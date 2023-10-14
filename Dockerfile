FROM python:3.11
COPY . .
RUN pip install -r requirements
EXPOSE 8001
CMD ["python","manage.py","runserver","0.0.0.0:8001"]
