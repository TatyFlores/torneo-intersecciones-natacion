import random

def abrir_archivo():
    f = open("Inscripción Competencia Intersecciones Natación(Sheet1).csv")
    data = f.readlines() 
    for i in range(len(data)):
        data[i] = data[i].strip("\n")
        data[i] = data[i].split(",")
        data[i] = [data[i][0]] + [data[i][4]] + data[i][6:]
    f.close()
    return data

def separar_secciones(data):
    natacion1 = []
    natacion2 = []
    for linea in data:
        if linea[3] == "DPT6300":
            linea.pop(-1)
            natacion1.append(linea)
        else:
            linea.pop(-2)
            natacion2.append(linea)
    return natacion1, natacion2

def separar_sexo(data):
    masc = []
    fem = []
    for linea in data:
        if linea[2] == "Femenino (Dama)":
            fem.append(linea)
        else:
            masc.append(linea)
    return fem, masc

def cantidad_series(data):
    d = len(data)
    if d%8 == 0:
        return d//8
    else:
        return d//8 + 1
    
def escribir_csv(archivo, listas):
    texto = "Serie,Pista,Nombre,Seccion\n"
    for serie in listas:
        for participante in serie:
            for dato in participante:
                texto += str(dato) + ","
            texto = texto[:-1] + "\n"
    texto = texto[:-1]
    f = open(archivo, "w")
    f.write(texto)
    f.close()
    return 

def mezclar(cant, data):
    total = []
    series = []
    for i in range(1, cant+1):
        serie = []
        sec = []
        j = 1
        while len(serie) < 8 or len(data) != len(total):
            a = random.choice(data)
            b = [i, j, a[1],a[4]]
            if b not in total:
                if a[3] == "DPT6302" or len(data)+1 == len(total):
                    total.append(b)
                    serie.append(b)
                    j+=1
                elif a[4] not in sec:
                    total.append(b)
                    serie.append(b)
                    sec.append(a[4])
                    j+=1
        series.append(serie)
    return series

