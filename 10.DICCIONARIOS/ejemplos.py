#Módulos y librería estandar
# Librería estandar typing, tipar datos a list y diccionarios para hacer mas optimo el código
# módulo es una porcion de codigo utilizable, para poder usarlo necesitamos importa la parte del código que deseamos utilizar.

# en este codigo estoy importando desde libreria typing la funcion union
# # union me permite tipas una coleccion de tipos, que si no sabes el tipo de dato con union le podemos pasar una lista de los  posibles tipos de datos que puede tener mi valor.
 
from typing import Union
# sin libreria
#alumno: dict[str:str|int]
alumno: dict[str:union[str,int,float,bool]]={
    "id_alumno":1,
    "DNI":53322363,
    "nombre":"mio",
    "edad":20,
    "matricula":true,
}
# Para acceder: tenemos dos maneras la manera clasica y
##clasica
print(alumno["DNI"])

# metodos
print(alumno.get("edad","valor no encontrado"))
# crear/modificar
print(alumno)
alumno["nombre"]="otro" #si existe la clave se actualiza el valor
alumno["ruc"]= 8916411211115421 # si no existe la clave se crea
print(alumno)
#crear/modificar varios
alumno.update({"nombre":"otro2","edad":21})
alumno.update({"carrera":"agro","semestre":"iii"})
print(alumno)
#eliminar
eliminado=alumno.pop("carrera") #elimina la clave y su valor
print(f"el elemento eliminado es:{eliminado}")
print(f"mi nuevo diccionario es:{alumno}")   