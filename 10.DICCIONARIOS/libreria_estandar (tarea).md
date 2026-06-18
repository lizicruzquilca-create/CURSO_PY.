# libreria estadar de python
Es el conjunto de módulos y paquetes que vienen incluidos con Python.

Su objetivo es proporcionar herramientas para tareas comunes como manejo de archivos, fechas, matemáticas, redes, procesamiento de texto y estructuras de datos.
- cuales son
- cuales son los mas usados
- y las formas de incluirlas en nuestros archivos de python
    * math: Proporciona funciones matemáticas.
    EJEMPLO
    import math
        print(math.sqrt(25))
        print(math.pi)
    * random: Genera números aleatorios.
    import random
        print(random.randint(1, 10))
    * datetime: Permite trabajar con fechas y horas.
    from datetime import datetime
        ahora = datetime.now()
    print(ahora)
    * os: Interactúa con el sistema operativo.
    import os
    print(os.getcwd())  # Directorio actual
    * sys: Acceso a parámetros y configuración del intérprete.
    import sys
    print(sys.version)
    * json: Trabaja con datos en formato JSON.
    import json
    persona = {"nombre":"Ana",  
        "edad": 25}
    texto = json.dumps(persona)
    print(texto)
    * collections
    Incluye estructuras de datos especializadas.
    from collections import Counter
    texto = ["a", "b", "a", "c", "a"]
    print(Counter(texto))
    * re: Permite trabajar con expresiones regulares.
    import re
    texto = "Python 2025"
    resultado = re.findall(r"\d+", texto)
    print(resultado)
    * statistics: Funciones estadísticas básicas.
    import statistics
    datos = [10, 20, 30, 40]
    print(statistics.mean(datos))
    * itertools: Herramientas para iteradores y combinaciones.
    from itertools import permutations
    print(list(permutations([1, 2, 3], 2)))
# modulos en python7
    Un módulo es un archivo con extensión .py que contiene código Python (funciones, clases, variables, etc.) y que puede ser reutilizado en otros programas mediante la instrucción `import`.
    Su objetivo es organizar el código y facilitar su reutilización.
1. Módulos estándar: Vienen incluidos con Python.

Ejemplos:

- import math
- import random
- import datetime
- import os
- import json

2. Módulos de terceros: Se instalan con pip.
Ejemplos:

- import numpy
- import pandas
- import requests

3. Módulos propios: Son creados por el programador.

import operaciones