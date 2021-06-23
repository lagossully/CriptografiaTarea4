import subprocess
import string
import base64

bashCommand = []

bashCommand.append("hashcat -a 0 -m 0 -w 4 Ofuscado/archivo_1 Diccionarios/diccionario_2.dict")

bashCommand.append("hashcat -a 0 -m 10 -w 4 Ofuscado/archivo_2 Diccionarios/diccionario_2.dict")

bashCommand.append("hashcat -a 0 -m 10 -w 4 Ofuscado/archivo_3 Diccionarios/diccionario_2.dict")

bashCommand.append("hashcat -a 0 -m 1000 -w 4 Ofuscado/archivo_4 Diccionarios/diccionario_2.dict")

bashCommand.append("hashcat -a 0 -m 1800 -w 4 Ofuscado/archivo_5 Diccionarios/diccionario_2.dict")


for i in range(0,len(bashCommand)):

    pot = open("hashcat/potfilearchivo"+str(i+1), "w")

    open = subprocess.Popen(bashCommand[i].split(), stdout=subprocess.PIPE)

    output, error = open.communicate()

    print(output.decode('utf-8'))

    pot.writelines(output.decode('utf-8'))

    pot.close()