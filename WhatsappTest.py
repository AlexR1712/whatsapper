from whatsapp import Whatsapp

test = Whatsapp()

#print(test.getContacts())
go = raw_input('Select Chat')
print(test.getContacts()) # retorna un arreglo con los nombres de contactos

test.exit()