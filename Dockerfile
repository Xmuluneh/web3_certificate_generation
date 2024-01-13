FROM python:3.10

COPY requirements.txt requirements.txt

RUN pip install -U pip

RUN pip install -r requirements.txt

RUN python manage.py server
# Copy app code and set working directory
COPY . .
WORKDIR /

# Run
CMD [ "python" ,'manage.py','server']