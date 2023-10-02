# API

## Descripción:
Este proyecto permite demostrar el uso de una API implementada en Python a través del framework de Flask

## Instalación:
El primer paso es instalar las dependencias que estan dentro del archivo requirements.txt

Para esto debemos pararnos en la direccion de la carpeta API y ejecutar el comando ***python -m pip install -r requirements.txt***

## Cómo ejecutar:
Una vez tengamos instaladas las dependencias ejecutamos el programa python **controller.py**
O en su defecto ejecutar el comando *'python controller.py'* dentro de la carpeta services en laterminal

## Verificar api:
Despues de levantar el servidor de Flask procedemos a abrir el index que se encuentra dentro de la carpeta client
O de igual manera ingresar la dirección de ***http://localhost:8000/api/message*** en el navegador para ver el mensaje json

## Despliegue en servidor:
Después de desarrollar tu aplicación, querrás hacerla disponible públicamente para otros usuarios. Cuando estás desarrollando localmente, probablemente estés usando el servidor de desarrollo, el depurador y el recargador incorporados. Estos no deben ser utilizados en producción. En su lugar, deberías utilizar un servidor WSGI dedicado o una plataforma de alojamiento, algunos de los cuales se describirán aquí.

El objetivo principal de estos documentos es familiarizarte con los conceptos involucrados en la ejecución de una aplicación WSGI utilizando un servidor WSGI de producción y un servidor HTTP. Hay muchos servidores WSGI y servidores HTTP, con muchas posibilidades de configuración. Las páginas siguientes discuten los servidores más comunes, y muestran los fundamentos de la ejecución de cada uno. La siguiente sección discute las plataformas que pueden gestionar esto por ti.

** Gunicorn
** Waitress
** mod_wsgi
** uWSGI
** gevent
** eventlet
** ASGI

# UTILIZAR DOCKER

## Build
- ** docker build -t name_docker . **

## Run
- ** docker run -p 5000:5000 name_docker **
