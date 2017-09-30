from whatsapp import Whatsapp

test = Whatsapp()

#print(test.getContacts())
go = raw_input('Select Chat')
#print(test.getContacts()) # retorna un arreglo con los nombres de contactos

test.getChatBySearch('Maria Estefania')

test.setTextMessage('Prueba exitosa!')

raw_input('Exit?')
test.exit()
