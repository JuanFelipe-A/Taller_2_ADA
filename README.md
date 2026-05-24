# Taller II — Estructuras de Datos
**Curso:** Análisis y Diseño de Algoritmos  
**Universidad del Valle**

---

## Integrantes

| Nombre | Código | Correo |
|--------|--------|--------|
| Juan Felipe Aristizabal | 2459364-3743 | juan.felipe.aristizabal@correounivalle.edu.co |
| Victor Manuel Murillo Goyes | 2459569-3743 | victor.goyes@correounivalle.edu.co |

---

## Estructura del proyecto

```
Taller_2_ADA/
├── problema1_editor.py       # Problema 1 — Editor de texto con deshacer
├── problema2_urgencias.py    # Problema 2 — Atención de pacientes en urgencias
├── problema3_canciones.py    # Problema 3 — Lista de canciones
├── problema4_productos.py    # Problema 4 — Conteo de productos vendidos
├── test1.txt                 # Caso de prueba Problema 1
├── test2a.txt                # Caso de prueba A Problema 2
├── test2b.txt                # Caso de prueba B Problema 2
├── test3a.txt                # Caso de prueba A Problema 3
├── test3b.txt                # Caso de prueba B Problema 3
├── test4a.txt                # Caso de prueba A Problema 4
├── test4b.txt                # Caso de prueba B Problema 4
└── README.md
```

---

## Cómo ejecutar

Cada problema lee desde la entrada estándar (`stdin`). El formato de entrada es:

```
N
OPERACION_1
OPERACION_2
...
OPERACION_N
```

Donde `N` es el número de operaciones.

**Opción 1 — Archivo de prueba:**
```bash
python3 problemaN.py < testN.txt
```

**Opción 2 — Entrada manual:**
```bash
python3 problemaN.py
```
Luego escribe las operaciones línea por línea.

---

## Problemas resueltos

### Problema 1 — Editor de texto con deshacer

**Estructura usada:** Pila (`Stack`)  
**Archivo:** `problema1_editor.py`

Operaciones:
- `ESCRIBIR palabra` — agrega la palabra al texto
- `DESHACER` — elimina la última palabra escrita
- `MOSTRAR` — imprime el texto actual (o `VACIO` si está vacío)

Archivo de prueba (`test1.txt`):
```
7
ESCRIBIR hola
ESCRIBIR mundo
MOSTRAR
DESHACER
MOSTRAR
ESCRIBIR clase
MOSTRAR
```

Salida esperada:
```
hola mundo
hola
hola clase
```

---

### Problema 2 — Atención de pacientes en urgencias

**Estructura usada:** Cola (`Queue`)  
**Archivo:** `problema2_urgencias.py`

Operaciones:
- `LLEGA nombre` — agrega un paciente al final de la cola
- `ATIENDE` — atiende al primer paciente (o imprime `SIN PACIENTES`)
- `SIGUIENTE` — muestra el próximo paciente (o imprime `COLA VACIA`)

Archivo de prueba A (`test2a.txt`):
```
8
LLEGA Ana
LLEGA Luis
SIGUIENTE
ATIENDE
SIGUIENTE
LLEGA Marta
ATIENDE
ATIENDE
```

Salida esperada:
```
Ana
Ana
Luis
Luis
Marta
```

Archivo de prueba B (`test2b.txt`):
```
5
ATIENDE
LLEGA Pedro
ATIENDE
SIGUIENTE
ATIENDE
```

Salida esperada:
```
SIN PACIENTES
Pedro
COLA VACIA
SIN PACIENTES
```

---

### Problema 3 — Lista de canciones

**Estructura usada:** Lista enlazada simple (`SingleLinkedList`)  
**Archivo:** `problema3_canciones.py`

Operaciones:
- `AGREGAR cancion` — agrega una canción al final
- `INSERTAR posicion cancion` — inserta en una posición específica (base 0); si la posición supera el tamaño, se agrega al final
- `ELIMINAR cancion` — elimina la primera aparición
- `MOSTRAR` — imprime la lista separada por espacios (o `LISTA VACIA`)

Archivo de prueba A (`test3a.txt`):
```
7
AGREGAR rock
AGREGAR pop
INSERTAR 1 jazz
MOSTRAR
ELIMINAR rock
MOSTRAR
AGREGAR salsa
```

Salida esperada:
```
rock jazz pop
jazz pop
```

Archivo de prueba B (`test3b.txt`):
```
6
MOSTRAR
AGREGAR reggaeton
INSERTAR 5 vallenato
MOSTRAR
ELIMINAR pop
MOSTRAR
```

Salida esperada:
```
LISTA VACIA
reggaeton vallenato
reggaeton vallenato
```

---

### Problema 4 — Conteo de productos vendidos

**Estructura usada:** Tabla hash (`HashTable`)  
**Archivo:** `problema4_productos.py`

Operaciones:
- `VENDER producto cantidad` — registra unidades vendidas (acumula si el producto ya existe)
- `CONSULTAR producto` — imprime unidades vendidas (o `0` si no existe)
- `TOTAL` — imprime el total de unidades vendidas entre todos los productos

Archivo de prueba A (`test4a.txt`):
```
7
VENDER arroz 3
VENDER leche 2
CONSULTAR arroz
VENDER arroz 4
CONSULTAR arroz
CONSULTAR pan
TOTAL
```

Salida esperada:
```
3
7
0
9
```

Archivo de prueba B (`test4b.txt`):
```
6
TOTAL
VENDER cafe 5
VENDER cafe 2
VENDER azucar 1
CONSULTAR cafe
TOTAL
```

Salida esperada:
```
0
7
8
```
