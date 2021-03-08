# E.F.E.C (Email File Extraction and Comparison)

## Razones del proyecto

Hace prácicamente poco tiempo perdí archivos en excel y pdf de mi computadora y estoy necesitando recuperarlos, gran parte de ellos fueron enviados y logré recuperar versiones anteriores con los nombres anteriores de esos archivos, el objetivo principal de este programa es comparar los nombres de los archivos que tengo en mi disco y encontrar la última versión (partiendo de que la última versión es el último archivo enviado a partir de la fecha de envio) enviada a un destinatario para así recuperarlo.

## Antes de Comenzar

Primero que nada es necesario habilitar IMAP en las configuraciones y [habilitar el acceso a aplicaciones poco seguras](https://myaccount.google.com/lesssecureapps).

En el caso de que existan problemas al momento de generar conexiones al correo y este haya sido creado por un proovedor de hosting u otros, contactarlos para solucionar problemas.

## Seguimiento

* Para recuperar los archivos hasta ahora se manejará Python utilizando las librerias `imaplib` para generar la conexión y extracción de datos, `email` para decodificar información y `os` para el manejo de archivos dentro del sistema.

* Hasta ahora el código es funcional y gran parte está explicado en comentarios, gran parte del código está escrito en ingles sin embargo y esto es más que nada por costumbre.

### Actualizaciones necesarias

1. Hacer que el programa no descargue un mismo archivo `n` veces sino que se quede con el archivo de la última fecha.

2. Modularizar el código pasando ciertas instrucciones a funciones.

3. Crear una clase con las siguientes funcionalidades.

4. Mostrar o solucionar posibles errores de tipeo, conexión o depuración de datos.

### Revisar

1. Comprobar extracción exitosa de otros tipos de archivos que no sean excel.
