 #from ast import While


from ast import While
from time import sleep

horas = 0

minutos = 0

segundos = 0

while horas < 24 :
    while minutos < 60 :
        while segundos < 60 :
            print (horas, ":", minutos, ":", segundos)
            segundos = segundos + 1
            sleep(1)
        segundos = 0
        minutos = minutos + 1
    horas = horas + 1
    minutos = 0

    
    

# while minutos < 60 :
#     while segundos < 60 :
#         print(minutos, ":", segundos)
#         segundos = segundos + 1
#     minutos = minutos + 1
#     segundos = 0