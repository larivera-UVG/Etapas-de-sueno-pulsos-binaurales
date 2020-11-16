# Obtención , Análisis y clasificación de señales  
## Offline
### Descripción 
Esta seccion contiene un grupo de archivos necesarios para la clasificacion de señales obtenidas desde la base de datos de PhysioNet devolviendo como resultado matrices de confusion y porcentajes de error obtenidos a traves de validación cruzada. 
### Requerimientos
Para poder ejecutar estos codigos de MATLAB no se requiere de librerias extras aparte de las que vienen por defecto en MATLAB.
## Tiempo Real
### Descripción
Al igual que en las pruebas offline se busca clasificar las diferentes etapas del sueño pero con la varienta de hacerlo a medida que estas van ocurriendo, realizando la lectura de datos atraves del Electro - Cap, el procesamiento de las señales obtenidas, la extraccion de las diferentes caracterisitcas para la clasificación y por ultimo implementar estas caracterisitcas para la clasificacion de las etapas.
### Requerimientos
Para esto solo se requiere instalar la libreria de "Lab Streaming Layer (LSL) with OpenBCI" la cual se puede encontrar en el siguiente enlace https://github.com/openbci-archive/OpenBCI_MATLAB junto con las instrucciones para su instalacion.
