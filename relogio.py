 #from ast import While


from ast import While

from time import sleep


horas = 0
minutos = 0
segundos = 0

minutos = int(input("diga os minutos:"))
horas = int(input("diga nas horas:"))

horasAlarme = int(input("para que horas quere o alarm:"))
minutosAlarme = int(input("para que minuto quere o alarm:"))

while horas < 24 : 
    while minutos < 60 :
        if horasAlarme == horas :
            if minutosAlarme == minutos :
                print("acabou o tempo!!!")
                exit()
        while segundos < 60 :
            print (horas, ":", minutos, ":", segundos)
            segundos = segundos + 1
            sleep(1)
        segundos = 0
        minutos = minutos + 1
    horas = horas + 1
    minutos = 0    
