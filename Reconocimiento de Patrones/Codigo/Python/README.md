# Envío de datos a MATLAB y Almacenamiento de Señales 

## Alamacenamiento en la base de datos
### Descripcion
Este archivo se encarga de realizar la conexion entre python y la base de datos en MYSQL haciendo la transferencia de archivos de manera local y alamacenando las rutas de los documentos en la base de datos para luego al realizar la descarga solo de accede a la ruta para obtenenr el archivo.
### Librerias utilizadas
Para este codigo se utilizan las liberias:
- mysql.connector
- shutil 

Para saber como instalarlas se puede utilizar el comando "pip install + nombre de la libreria" en la consola de comandos o referirirse a la siguiente paguina como referencia:https://docs.python.org/es/3/installing/index.html

### Utilizacion 
Para poder utilizar este programa solo es necesario abrirlo y variar los campos marcados dentro del codigo con los parametros para el usuario que lo desee utilizar y los archivos que desee almacenar.

## Envio de datos a MATLAB
### Descripcion
Este programa realiza la conexion entre Python y MATLAB para enviar los datos obtenidos por el Electro - Cap para luego ser procesados y analizados posteriormente. 
### Librerias utilizadas
Para este codigo se utilizan las liberias:
- pylsl
- argparse
- atexit

### Utilizacion
