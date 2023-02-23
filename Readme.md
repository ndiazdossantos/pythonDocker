# Imagen Docker personalizada


---
Primero debemos especificar que librerías queremos instalar en nuestra imagen personalizada, para ello debemos crear el fichero [```Dockerfile```](https://github.com/ndiazdossantos/proyectoYoutube/blob/master/Dockerfile).

```yml
FROM python:3

RUN pip install pytube

```
Para crear nuestra propia imagen personalizada de un contenedor de docker debemos ejecutar el comando:


`$ docker build -t youtubeimagen:latest .`

Posteriormente configuramos nuestro [```docker-compose.yml```](https://github.com/ndiazdossantos/proyectoYoutube/blob/master/docker-compose.yml)

```yml
services:
  python:
    image: youtubeimagen:latest
    volumes:
      - .:/usr/src/app
    stdin_open: true
    tty: true
    working_dir: /usr/src/app
    command: python main.py 
```
Finalmente para levantar el servicio con nuestra propia imagen:

`$ docker-compose up`


Y ya tendremos nuestro contenedor con el script que hayamos especificado en ejecución en "command: ", en nuestro caso un script de python.