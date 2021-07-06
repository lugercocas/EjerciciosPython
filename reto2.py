#Reto 2.: Cálculo del Índice de Calidad del Aire (ICA) generado por la Concentración de un Contaminante
#Por: Luis Gerardo Collazos Castro
#collazosl@uninorte.edu.co
#C.C.: 1083876534
#Cel.: 3213545648
#print("Programa que calcula el valor del ICA y entrega una alarma según el valor de")
#print("concentración de CO2 1h en ppm.")
#Leo el valor de la concentración y lo almaceno en C.
alerta = ""
conteo_total = 0
conteo_verde=0
conteo_amarillo=0
conteo_naranja=0
conteo_rojo=0
conteo_morado=0
conteo_marron=0
ICA = 0
ICApro = 0
while alerta != "verde":
    C = float(input("Ingrese la concentración de CO2 1h en ppm:"))
    bandera = 0
    conteo_total+=1       
    if C >= 0 and C < 0.054:
        Ii = 0
        Ih = 50
        BPi = 0
        BPh = 0.053
    elif C >= 0.054 and C < 0.101:
        Ii = 51
        Ih = 100
        BPi = 0.054
        BPh = 0.100
    elif C >= 0.101 and C < 0.361:
        Ii = 101
        Ih = 150
        BPi = 0.101
        BPh = 0.360
    elif C >= 0.361 and C < 0.650:
        Ii = 151
        Ih = 200
        BPi = 0.361
        BPh = 0.649
    elif C >= 0.650 and C < 1.250:
        Ii = 201
        Ih = 300
        BPi = 0.650
        BPh = 1.249
    elif C >= 1.250 and C < 1.650:
        Ii = 301
        Ih = 400
        BPi = 1.250
        BPh = 1.649
    elif C >= 1.650 and C < 2.050:
        Ii = 401
        Ih = 500
        BPi = 1.650
        BPh = 2.049
    else:
        bandera = 1
    if bandera == 0:
        ICA = ((Ih - Ii)/(BPh-BPi)) * (C - BPi) + Ii 
        if ICA >= 0 and ICA <= 50:
            alerta = "verde"
            conteo_verde+=1
        elif ICA > 50 and ICA <= 100:
            alerta = "amarillo"
            conteo_amarillo+=1
        elif ICA > 100 and ICA <= 150:
            alerta = "naranja"
            conteo_naranja+=1
        elif ICA > 150 and ICA <= 200:
            alerta = "rojo"
            conteo_rojo+=1
        elif ICA > 200 and ICA <= 300:
            alerta = "morado"
            conteo_morado+=1
        elif ICA > 300:
            alerta = "marron"
            conteo_marron+=1
        #print("{:.2f}".format(ICA),alerta)
        ICApro = ICA + ICApro
    #else:
        #print("-1 error en los datos")
ICApro = ICApro/conteo_total
if ICApro >= 0 and ICApro <= 50:
    alerta = "verde"
elif ICApro > 50 and ICApro <= 100:
    alerta = "amarillo"
elif ICApro > 100 and ICApro <= 150:
    alerta = "naranja"
elif ICApro > 150 and ICApro <= 200:
    alerta = "rojo"
elif ICApro > 200 and ICApro <= 300:
    alerta = "morado"
elif ICApro > 300:
    alerta = "marron"
print(conteo_total)
print("{:.2f}".format(ICApro),alerta)
print("verde","{:.2f}%".format(conteo_verde*100/conteo_total))
print("amarillo","{:.2f}%".format(conteo_amarillo*100/conteo_total))
print("naranja","{:.2f}%".format(conteo_naranja*100/conteo_total))
print("rojo","{:.2f}%".format(conteo_rojo*100/conteo_total))
print("morado","{:.2f}%".format(conteo_morado*100/conteo_total))
print("marron","{:.2f}%".format(conteo_marron*100/conteo_total))