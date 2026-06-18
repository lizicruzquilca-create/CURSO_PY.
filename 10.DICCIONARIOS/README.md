#Diccionarios
los diccionarios son la forma mas comun de almacenar datos estructurados de objetos que nos rodea en el mundo, al igual que las listas que guardan informacion en 'elementos', de igual manera los diccionarios almacenan sus datos en 'elementos' separados por comas, la diferencia es que las listas almacenan los elementos por 'indice' y 'valor', y los diccionarios almacenan los elementos por 'clave:valor'.
**ejemplo**
```python
vocales:list[str]=['a','e','i','o','u'] #valores
#indices
#un elemnto en una lista esta conformado por dos cositas: el indice y su valor.
alumno:dict={'nombre':'eduardo','edad':40}
#Para acceder un valor en una lista
volaces[2] #1
#Para acceder un valor en un diccionario
alumno["nombre"] #eduardo

##Acceder a elementos 
- **Por clave(forma directa)**
```python
persona:dicc={
    "nombre":"celia",
    "edade":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com",
}
print(persona)["edad"] #16
print(persona)["email"] #celi@email.com
```

## acceder a elementos
    "email":"celi@email.com"
}
- **Por su metodo (forma mmas segura)**
```python
persona:dict={
    "nombre":"celia",
    "edade":16,
    "ciudad":"cabo verde",
    "email":"celi@email.com",
}
print(persona.get("nombre")) #celia
# la diferencia de este metodo es que no permite manejar errores
print(persona.get("telefono")) #none
print(persona.get("telefono","no disponible")) # si la clave telefono no existe no ostrar none si no el segundo parametro que le pasemos al metodo get.
```
## modificar elementos
** cambiar un valor existente**
```python
persona:dict={
    "nombre":"celia",
    "edade":16,
}
persona["edad"]=19
#agregar una nueva clave:valor
persona["carrera"]="agro"
#si la clave no existe se crea automaticamente, si existe se actualiza.
```
## agregar/actualizar multiples elementos
para esto tenemos que hacer uso de el metodo`.update` se puede agregar si los pares de  `clave:valor` no existe y actualizar si el `clave:valor` existe.
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":20465783674
}
#actualizar usando el metodo .UPDATE tengo dos maneras de usar este metodo
#1. diccionarios
tienda.update({"ruc":123654893222,"telefono":94629232})
#2. pares clave:valor
tienda.update(h_atencion="9-12",gerente="kevin")
```
##eliminar elementos
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":2456255653265
}
el_eliminado=tienda.pop("ruc")
tienda.popitem() #eliminar el ultimo elemento
#para limpiar todo el diccionario
tienda.clear()

##recorre un diccionario (tarea)
# Recorrer las claves
persona = {
    "nombre": "celi",
    "edad": 25,
    "ciudad": "puquio"
}

En este diccionario:

"nombre", "edad" y "ciudad" son las claves.
"celi", 25 y "puquio" son los valores.
# Recorrer los valores
for valor in mi_diccionario.values():
    print(valor)

Salida:
Celi
25
Puquio
# Recorrer claves y valores
for clave, valor in mi_diccionario.items():
    print(clave, ":", valor)
Salida:
nombre : celi
edad : 25
ciudad : Puquio
Dependiendo de lo que necesites, puedes recorrer:

# 1. Solo las claves
Cuando iteras directamente sobre un diccionario, Python devuelve sus claves.
for clave in persona:
    print(clave)

# 2. Solo los valores
Si únicamente te interesan los datos almacenados:
for valor in persona.values():
    print(valor)

El método .values() devuelve una vista con todos los valores del diccionario.

# 3. Claves y valores simultáneamente
Es la forma más utilizada porque permite acceder a toda la información de cada elemento.
for clave, valor in persona.items():
    print(clave, valor)
El método .items() devuelve pares (clave, valor).


# Métodos relacionados
# Método	Descripción
dict.keys()	Devuelve las claves
dict.values()	Devuelve los valores
dict.items()	Devuelve pares (clave, valor)

## recuerda:
* Usa for clave in diccionario: cuando solo necesites las claves.
* Usa diccionario.values() cuando solo necesites los valores.
*Usa diccionario.items() cuando necesites trabajar con claves y valores al mismo tiempo.