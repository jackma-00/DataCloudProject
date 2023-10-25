FROM python:3.10-slim-bullseye

WORKDIR /code

COPY ./setup.py /code/setup.py
 
RUN pip install --no-cache-dir --upgrade .

COPY ./src /code/src

CMD ["python", "./src/main.py"]
