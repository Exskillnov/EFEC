# Proyecto E.F.E.C (Email File Extraction and Comparison)

## Razones del proyecto

Hace prácicamente poco tiempo perdí archivos en excel y pdf de mi computadora y estoy necesitando recuperarlos, gran parte de ellos fueron enviados y logré recuperar versiones anteriores con los nombres anteriores de esos archivos, el objetivo principal de este programa es comparar los nombres de los archivos que tengo en mi disco y encontrar la última versión (partiendo de que la última versión es el último archivo enviado a partir de la fecha de envio) enviada a un destinatario para así recuperarlo.

## Antes de Comenzar

Es necesario habilitar IMAP en las configuraciones de Gmail y al mismo tiempo habilitar el acceso al correo por medio de aplicaciones no seguras en el caso de que por algún motivo Google intente bloquear el acceso al programa detectándolo como dispositivo.

## Seguimiento

Para recuperar los archivos hasta ahora se manejará Python utilizando las librerias echo  `imaplib`, `email` y otros...
