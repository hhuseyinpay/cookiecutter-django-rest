FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application app to the image
COPY . app
WORKDIR app

EXPOSE 8000

# Migrates the database, uploads staticfiles, and runs the production server
# RUN python manage.py migrate  database bağlantıları .env'den okuduğum için sıkıntı oluyor burası
# RUN python manage.py collectstatic --no-input

CMD gunicorn --bind 0.0.0.0:8000 --chdir=/app {{cookiecutter.app_name}}.wsgi:application
