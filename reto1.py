#Reto 1.: Cálculo del Índice de Calidad del Aire (ICA) generado por la Concentración de un Contaminante
#Por: Luis Gerardo Collazos Castro
#collazosl@uninorte.edu.co
#C.C.: 1083876534
#Cel.: 3213545648
print("Programa que calcula el valor del ICA y entrega una alarma según el valor de")
print("concentración de CO2 1h en ppm.")
#Leo el valor de la concentración y lo almaceno en C.
C = float(input("Por favor ingrese el valor de la concentración C de CO2 1h en ppm:"))
bandera = 0
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
    alerta = ""
    if ICA >= 0 and ICA <= 50:
        alerta = "verde"
    elif ICA > 50 and ICA <= 100:
        alerta = "amarillo"
    elif ICA > 100 and ICA <= 150:
        alerta = "naranja"
    elif ICA > 150 and ICA <= 200:
        alerta = "rojo"
    elif ICA > 200 and ICA <= 300:
        alerta = "morado"
    elif ICA > 300:
        alerta = "marron"
    print("{:.2f}".format(ICA),alerta)
else:
    print("-1 error en los datos")
