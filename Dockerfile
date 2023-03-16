FROM python:3

WORKDIR /usr/src/app

COPY requisitos.txt ./
RUN pip install --no-cache-dir -r requisitos.txt

COPY ./ /usr/src/app

CMD [ "python", "main.py"]