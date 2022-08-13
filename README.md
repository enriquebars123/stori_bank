# bank_backend

## Requerimientos

    python 3.10.1
    docker desktop 4.11.1


## Abrir el cmd, acceder al proyecto entrar a la carpeta bank

cd [nombre_proyecto]/bank


## instalar contenedores disponibles

Ejecutamos el siguiente codigo

code:
    docker-compose -f buid.yml up -d postgres

- esperamos que la consola marque done...

code:   
    docker-compose -f buid.yml up -d web

- esperamos que la consola marque done...


##obtener el [CONTAINER ID] , NAME "bankdj"

code: 
    docker ps -a



##acceder al modo interactivo de la consola identicar 

ejemplo : docker exec -i -t 4a414a7bcb70 /bin/bash 

code: 
    docker exec -i -t [CONTAINER ID] /bin/bash 


## una vez entrando a la consola interactiva ejecutar los siguientes comandos
code: 
    python manage.py makemigrations

    python manage.py migrate

    exit

## salir modo interactivo

Ctrl + c

## Finalmente accedermos a la aplicacion

http://127.0.0.1:8000/transaction/


ver resultados registrados en bd

http://127.0.0.1:8000/api/v1/transaction/


