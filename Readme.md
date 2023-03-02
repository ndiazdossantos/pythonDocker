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

Para subirlo a [DockerHub](https://hub.docker.com/) primeramente debemos ir a nuestro perfil y presionar en "Create repository":

![Imagen](https://i.imgur.com/dWgMmFr.png)

Una vez accedemos seleccionamos el nombre de nuestro repositorio y presionamos en create.

![Imagen2](https://i.imgur.com/XDNq9GP.png)

Una vez tenemos todo creado accedemos a nuestro terminal y ejecutamos la sucesión de estos comandos:

`$ docker-login`

`$ docker tag youtubeimagen:latest ndiazdossantos2023:youtubeimagen`

`$ docker push ndiazdossantos2023/youtubeimagen:latest`

Donde nos autenticamos con nuestra cuenta de docker hub, posteriormente creamos el tag de nuestra imagen y lo vinculamos al repositorio de nuestra cuenta y finalmente realizamos el push del tag creado a nuestra cuenta y con la imagen seleccionada.