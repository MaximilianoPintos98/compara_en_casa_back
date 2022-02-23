FROM python:3.8
ENV PYTHONUNBUFFERED 1 
RUN mkdir /code_compara

WORKDIR /code_compara

COPY requirements.txt /code_compara/

RUN python -m pip install -r requirements.txt

COPY . /code_compara/

EXPOSE 8000