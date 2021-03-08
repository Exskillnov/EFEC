import imaplib, email
import os
import re #Expresiones Regulares

def inFolder (filename, fileList):
    for file in fileList:
        if file == filename:
            return True
    return False

savingPath = input('Ingrese la dirección a guardar los archivos: ')

comparisonPath = input('Ingrese la dirección a comprarar los archivos: ')
filesToCompare = os.listdir(comparisonPath)

username = input('Ingrese Usuario: ')
password = input('Ingrese Contraseña: ')

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)

folder = mail.select("[Gmail]/Enviados") #Ingresa a la carpeta de archivos enviados
print(folder)

result, data = mail.uid('search', None, 'ALL') #Recibe todos los mensajes

listOfItems = data[0].split() #Crea una lista con todas las IDs codificadas

print(listOfItems)

for item in listOfItems:
    result2, emailData = mail.uid('fetch', item, '(RFC822)')
    rawEmail = emailData[0][1].decode('utf-8')
    emailMessage = email.message_from_string(rawEmail)
    if emailMessage.get_content_maintype() == 'multipart': #mensaje con multipartes
        for part in emailMessage.walk():
            if part.get('Content-Disposition') is None: continue #Si el fragmento es None hace la siguiente iteración
            filename = part.get_filename() #Recupera el nombre del archivo
            if inFolder(filename, filesToCompare):
                print (emailMessage["Date"]) #Recupera la fecha del mensaje enviado
                savingFile = os.path.join(savingPath, filename)
                fileHandler = open(savingFile, 'wb') #Escribir en binario, si ya existe lo sobrescribe
                fileHandler.write(part.get_payload(decode=True)) #Decodifica el mensaje único y lo escribe en el archivo creado
                fileHandler.close() #Cierra el archivo
                print ('{0} Guardado o sobreescrito'.format(filename))
