import socket
import hashlib


port = 50557
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",port))
s.listen(1)
client, addr = s.accept()

texto1 = open("hashcat/potfilearchivo1", "r")
texto2 = open("hashcat/potfilearchivo2", "r")
texto3 = open("hashcat/potfilearchivo3", "r")
texto4 = open("hashcat/potfilearchivo4", "r")
texto5 = open("hashcat/potfilearchivo5", "r")


textos = []
textos.append(texto1.readlines())
textos.append(texto2.readlines())
textos.append(texto3.readlines())
textos.append(texto4.readlines())
textos.append(texto5.readlines())

for i in range (0, len(textos)):
    hashlib.sha256(textos[i+1]).hexdigest()
    len(hashlib.sha256(textos[i+1]).digest()) 





