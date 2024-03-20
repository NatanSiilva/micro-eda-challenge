FROM python:3.9.5-alpine3.13

WORKDIR /app/

ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE 1 

RUN apk update && \
    apk add --no-cache bash build-base curl mariadb-dev python3-dev
    

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt


CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "--port", "8000", "src.adapters.web.server:app"]
