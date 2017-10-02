from whatsapp import Whatsapp
"""
ws = Whatsapp()
go = input('Go Ahead!') 
contacts = ws.getContacts() # Get contact list
for name in contacts:
    ws.getChatBySearch(name)
    ws.setTextMessage('Hola! {name}'.format(name=name))
    # ws.send()
input('Exit?')
ws.exit()
"""

ws = Whatsapp()
go = input('Go Ahead!')
name = 'Ambar' 
ws.getChatBySearch(name)
ws.setTextMessage('Hola! {name}'.format(name=name))
ws.send()
input('Exit?')
