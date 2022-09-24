FROM python:3.9-alpine3.15

WORKDIR /code

RUN apk update && apk add postgresql-dev tzdata && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
      apk add --no-cache \
      --virtual=.build-dependencies \
      gcc \
      g++ \
      musl-dev \
      git \
      python3-dev \
      jpeg-dev \
      # Pillow
      zlib-dev \
      freetype-dev \
      lcms2-dev \
      openjpeg-dev \
      tiff-dev \
      tk-dev \
      tcl-dev \
      harfbuzz-dev \
      fribidi-dev && \
    apk del --purge .build-dependencies

ADD Pipfile Pipfile.lock ./

RUN pip install pipenv

RUN pipenv install --system --skip-lock

ADD . .

EXPOSE 8000

ENTRYPOINT ["aerich", "upgrade"]
ENTRYPOINT ["python", "run.py"]
