
#---------------------------------------
#@Autor: Luis Gerardo Collazos Castro
#@Date: 17/06/2021
#@Title: Reto 5
#---------------------------------------

#1) calcula_ica(): es una función que calcula el ICA
def calcula_ica(concentracion):
    C = concentracion
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
    else:
        ICA = -1
    return ICA

#2) calcula_alerta(): función que calcula la alerta de acuerdo al ICA ingresado.
def calcula_alerta(ICAin):
    alerta_out = ""
    if ICAin >= 0 and ICAin <= 50:
        alerta_out = "verde"
    elif ICAin > 50 and ICAin <= 100:
        alerta_out = "amarillo"
    elif ICAin > 100 and ICAin <= 150:
        alerta_out = "naranja"
    elif ICAin > 150 and ICAin <= 200:
        alerta_out = "rojo"
    elif ICAin > 200 and ICAin <= 300:
        alerta_out = "morado"
    elif ICAin > 300:
        alerta_out = "marron"
    return alerta_out

#leo los datos de entrada
file = open("data.csv")
dataInput = file.read().split("\n")
file.close()
temp_in = input().split(" ")
#ordeno los datos de entrada:
entrada = []
for d in temp_in:
    try:
        entrada.append(int(d))
    except:
        pass
entrada.sort() # ordeno la lista
#print(sorted(entrada))

        
#proceso los datos
data = []
for datos in dataInput:
    temp = datos.split(",")
    try:
        temp[0] = int(temp[0])
        temp[3] = float(temp[3])
        data.append(temp)
    except:
        pass


#realizo los calculos
for id in entrada:
    temp = []
    for  dato in data:
        if dato[0] == id:
            ica = calcula_ica(dato[3])
            aler = calcula_alerta(ica)
            temp.append({
                'id_city': dato[0],
                'city_name': dato[1],
                'department_name': dato[2],
                'measurement': dato[3],
                'ICA': ica,
                'alerta': aler})
    p_out = temp[0]
    #imprimo la salida 1
    print(p_out['id_city'],p_out['city_name'],p_out['department_name'])
    #imprimo la salida 2
    c_datos = len(temp)
    print("count",c_datos)
    #imprimo la salida 3
    print('c measurement')
    # calculo el promedio de las concentraciones
    c = 0
    for z in temp:
        c = c + z['measurement']
    mean = 0
    if c_datos != 0:
        mean = c / c_datos
    #imprimo la salida 4
    print('mean','{:.2f}'.format(mean))
    #calculo la desviación estandar de la muestra
    std = 0
    for d_std in temp:
        std = std + (d_std['measurement'] - mean)**2
    std = std / c_datos
    std = std ** (1/2)
    # imprimo la salida 5
    print('std',"{:.2f}".format(std))
    #calculo el mínimo.
    C = []
    for dt in temp:
        C.append(dt['measurement'])
    C.sort()
    #imprimo la salida 6
    min = C[0]
    print('min',"{:.2f}".format(min))
    #imprimo la salida 7
    max = C[len(C)-1]
    print('max', "{:.2f}".format(max))
    #imprimo la salida 8
    print("ica")
    # calculo la salida 9


    # calculo el promedio de las concentraciones
    c = 0
    for z in temp:
        c = c + z['ICA']
    mean = 0
    if c_datos != 0:
        mean = c / c_datos
    #imprimo la salida 10
    print('mean','{:.2f}'.format(mean))
    #calculo la desviación estandar de la muestra
    std = 0
    for d_std in temp:
        std = std + (d_std['ICA'] - mean)**2
    std = std / (c_datos - 1)
    std = std ** (1/2)
    # imprimo la salida 11
    print('std',"{:.2f}".format(std))
    #calculo el mínimo.
    C = []
    for dt in temp:
        C.append(dt['ICA'])
    C.sort()
    #imprimo la salida 12
    min = C[0]
    print('min',"{:.2f}".format(min))
    #imprimo la salida 13
    max = C[len(C)-1]
    print('max', "{:.2f}".format(max))

    #imprimo la salida 14
    print("alerts")
    #calculo la cantidad de alertas por color en la ciudad
    verde = 0 
    amari = 0
    naran = 0
    rojo  = 0
    morad = 0
    marro = 0
    for col in temp:
        color = col['alerta']
        if color == "verde":
            verde += 1
        elif color == "amarillo":
            amari += 1
        elif color == "naranja":
            naran += 1
        elif color == "rojo":
            rojo += 1
        elif color == "morado":
            morad += 1
        elif color == "marron":
            marro += 1
    #imprimo la salida 15
    print("verde",verde)
    #imprimo la salida 16
    print("amarillo",amari)
    #imprimo la salida 17
    print("naranja",naran)
    #imprimo la salida 18
    print("rojo",rojo)
    #imprimo la salida 19
    print("morado",morad)
    #imprimo la salida 20
    print("marron",marro)