import imaplib, email

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
            if part.get('Content-Disposition') is None: continue
            print (emailMessage["Date"]) #Recupera la fecha del mensaje enviado
            filename = part.get_filename()
            fp = open(filename, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()
            print ('{0} Guardado!'.format(filename))
