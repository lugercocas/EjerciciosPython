from os import system
#Funciones:
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

#Función que crea un vector con tamaño de la cantidad de ciudades
def crear_vector(n):
    i = 0
    lista = []
    while i < n:
        lista.append(0)
        i += 1
    return lista

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

def calcular_salida(lista,nc):
    """
    nc = total de ciudades
    """
    contar = crear_vector(nc)
    icas_c = crear_vector(nc)
    sal = []
    for fila in lista:
        i=0
        while i < nc:
            if fila[0] ==  i+1:                
                icas_c[i]=(icas_c[i]+fila[1])
                contar[i]+=1
                break
            i+=1
    m=0  
    #print("cuentas")
    #print(contar)  
    while m < nc:
        aler = ""
        ica_temp=0
        if contar[m] != 0:
            ica_temp = icas_c[m]/contar[m]
        aler = calcula_alerta(ica_temp)
        sal.append([m+1,ica_temp,aler])
        m+=1
    return sal

def hallar_max(lista):
    o = lista[0]
    r = 1
    for s in lista:
        if s[1] > o[1]:
            o = [s[0],s[1],s[2]]
    return o

def hallar_min(lista):
    o = lista[0]
    r = 1
    for s in lista:
        if s[1] < o[1]:
            o = [s[0],s[1],s[2]]
    return o

def hallar_porsentaje(lista):
    sal = [
        [0,'verde'],
        [0,'amarillo'],
        [0,'naranja'],
        [0,'rojo'],
        [0,'morado'],
        [0,'marron']]
    
    for a in lista:
        j = 0
        for al in sal:
            if a[2] == al[1]:
                sal[j][0] += 1
                break
            j+=1      
    i = 0
    for p in sal:
        sal[i][0] = (sal[i][0] * 100)/ len(lista)
        i += 1
    return sal

#valida primera entrada: n m
def valida_primera_entrada(entrada):
    if int(entrada[0]) < 0 or len(entrada) != 2:
        return False
    else:
        return True

#valida las entradas de ciudad y concentración.
def valida_entrada(ciudad_C,entrada):
    #cuantas ciudades se ingresarán datos
    city = int(ciudad_C[0])  
    #número de ciudad que se ingresa datos
    ncity = int(entrada[0]) 
    #Podría haver una entrada tipo [n1,m1,n2,m2...]
    mul = len(ciudad_C)%2
    #Faltaría validar los valores de n2,n3,...
    #si se cumplen todas las condiciones
    if (city <= ncity) and (city >= 1) and (len(ciudad_C) ==2) and mul ==0:
        return True
    else:
        return False

def primera_entrada():
    entrada = input()
    while not valida_primera_entrada(entrada.split(" ")):
        entrada = input()
    return entrada

def inputs(in_d):
    i = 0
    data = []
    length = int((in_d.split(" "))[1])
    while i < length:
        inp = input()        
        if valida_entrada(inp.split(" "),in_d.split(" ")):
            data.append(inp)
            i +=1
    #print(data)    
    return data

def main(lista, entrada):
    dato = entrada.split(" ")
    nciudades = int(dato[0])
    nentradas = int(dato[1])
    salida = []
    alertas = []
    for inputd in lista:
        #print(inputd)
        ciudad = int(inputd.split(" ")[0])
        C = float(inputd.split(" ")[1])
        ICA = calcula_ica(C)
        alerta = calcula_alerta(ICA)
        salida.append([ciudad,ICA,alerta])
    promedio = calcular_salida(salida, nciudades)    
    return [promedio,salida]

def imprime_salida(vector):
    """El vector contiene todas los datos a continuación pero en una sola fila.
    su tamaño o length es de 13.

    ciudad

    mejor_ica promedio_ica peor_ica

    ica_verde ica_amarillo ica_naranja ica_rojo ica_morado ica_morron

    icas_menores_al_promedio icas_iguales_al_promedio icas_mayores_al_promedio
    """
    for i in vector:
        print(i)
    pass

def calcula_salida_final(entrada,lista):
    #por cada ciudad
    for i in range(1,entrada[0]+1):
        #imprimo primera salida
        print(i)
        contarCiudad = []
        for j in range(entrada[1]):
            icasCiudad = lista[1][j]
            if icasCiudad[0] == i:
                #cuento cuantos de cada ciudad hay
                contarCiudad.append(icasCiudad)
        mejorStr = "0.00"
        promeStr = "0.00"
        peorStr = "0.00"
        if len(contarCiudad) != 0:
            mejor = (hallar_min(contarCiudad))[1]
            prom = (lista[0][i-1])[1]
            peor = (hallar_max(contarCiudad))[1]
            mejorStr = "{:.2f}".format(mejor)
            promeStr = "{:.2f}".format(prom)
            peorStr  = "{:.2f}".format(peor)
        #imprimo segunda linea
        print(mejorStr,promeStr,peorStr)
        #--------------------------
        colores = [0,0,0,0,0,0]
        contar = [0,0,0] #[#mejor,#prome,#peor]
        for color in contarCiudad:
            if color[2] == 'verde':
                colores[0]+=1
            elif color[2] == 'amarillo':
                colores[1]+=1 
            elif color[2] == 'naranja':
                colores[2]+=1 
            elif color[2] == 'rojo':
                colores[3]+=1 
            elif color[2] == 'morado':
                colores[4]+=1 
            elif color[2] == 'marron':
                colores[5]+=1 
            icaStr = "{:.2f}".format(color[1])
            if icaStr == promeStr:
                contar[1]+=1
            elif float(icaStr) < float(promeStr):
                contar[0]+=1
            elif float(icaStr) > float(promeStr):
                contar[2]+=1
        c = colores
        #imprimo la cantidad de colores de alarmas según el ICA
        print(c[0],c[1],c[2],c[3],c[4],c[5])
        #---------------------------------------------------
        """
        Falta lo siguiente que es l aúltima salida.
        La cantidad de ICAs menores al promedio, iguales al promedio y mayores al promedio, separados por espacios. Si una ciudad no presenta lecturas, todos los valores previamente mencionados deben ser 0.
        """
        print(contar[0],contar[1],contar[2])
        #----------------------------------------------------
    return [lista,entrada]
system("clear")
salida = []#[0,0.0,0.0,0.0,0,0,0,0,0,0,0,0,0]
#primera_in = "5 8"#"3 5"#primera_entrada()
primera_in = primera_entrada()
#data1 = ['3 1.048', '2 0.932', '3 0.808', '1 1.831', '3 0.482']#inputs(primera_in)
#data = ['5 0.905','2 0.138','5 0.957','1 0.743','2 1.951','2 1.925','5 1.912','3 0.464']
data = inputs(primera_in)
promedio_sal = main(data,primera_in)
 
mejor = hallar_min(promedio_sal[0])
peor = hallar_max(promedio_sal[0])
porsen = hallar_porsentaje(promedio_sal[0])
entrada = [int(primera_in.split(" ")[0]),int(primera_in.split(" ")[1])]
salida = calcula_salida_final(entrada,promedio_sal)