import os, io
# AGREGAR TAREA
lista=[]
lista2=[]
a=0
def ingreso_datos(materia, contenido):
    bd = open("bd_materias.txt","a")
    co= open("bd_contenido.txt","a")
    bd.write(f"{materia}\n")
    co.write(f"{contenido}\n")
    bd.close()
    co.close()
    return materia
def print_lista():
    for m in range(len(lista)):
        print(f"{m+1}. la tarea es: {lista[m]} y el contenido es: {lista2[m]}\n")
#MENÚ
def agregar_tarea():
    print("para ya no escribir mas tareas escribe solo el simbolo '+'")
    while True: 
        a= input("que tarea quiers ingresar?: ")
        if a == "+":
            print_lista()
            break
        else:
            ingreso_datos(a,input("qeu va a llevar esa tarea: "))
def eliminar_tarea(index):
    
    lista.pop(index-1)
    lista2.pop(index-1)
    bd=open("bd_materias.txt","w")
    for mat in range(len(lista)):
        bd.writelines(f"{lista[mat]}\n")
    bd.close()
    co=open("bd_contenido.txt","w")
    for con in range(len(lista2)):
        co.writelines(f"{lista2[con]}\n")
    co.close()

# CONVERTIDOR A LISTA NORMAL
with open("bd_materias.txt") as archivo:
        for linea in archivo:
            a=list(linea)
            a.remove("\n")
            lista.append("".join(a))
with open("bd_contenido.txt") as archivo:
        for line in archivo:
            b=list(line)
            b.remove("\n")
            lista2.append("".join(b))
# INICIO
while True:
    print("1. Agregar nueva tarea\n2. Eliminar tarea\n3. Ver tareas\n4. Salir")
    inicio= int(input("num: "))
    if inicio==1:
        agregar_tarea()
    elif inicio==2:
         eliminar_tarea(int(input("Que tarea deseas eliminar: ")))
         #eliminar datos
    elif inicio==3:
         print_lista()
         # ver tareas
    else:
         break
