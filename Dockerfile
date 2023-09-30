# Una imagen mínima de Docker basada en Alpine Linux 
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la ruta en /app
COPY . /app

# Instala las dependecias 
RUN pip install -r requirements.txt

# Expone el puerto 5000 (puerto predeterminado de flask)\
EXPOSE 5000

# Define el comando predeterminado que se ejecutará cuando se inicie el contenedor
CMD ["python", "services/controller.py"]


# Comando para crear imagen
# docker build -t flask/api .

# Comando para levantar el docker
# docker run -p 8000:5000 flask/api

