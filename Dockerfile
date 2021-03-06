FROM python:2.7

RUN apt-get update -yqq && apt-get install openssl -yqq

# Set PYTHONUNBUFFERED so output is displayed in the Docker log
ENV PYTHONUNBUFFERED=1
ENV STATIC_ROOT=/usr/src/app/static/

EXPOSE 8000
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application's code
COPY . /usr/src/app

# Run the app
CMD ["./cli/run.sh"]