# Taller II — Estructuras de Datos
**Curso:** Análisis y Diseño de Algoritmos  
**Universidad del Valle**

---

## Integrantes

| Nombre | Código | Correo |
|--------|--------|--------|
| Juan Felipe Aristizabal | 2459364-3743 | juan.felipe.aristizabal@correounivalle.edu.co |
| [Nombre compañero] | [Código compañero] | [Correo compañero] |

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

Crear archivo de prueba:
```bash
cat > test1.txt << 'EOF'
7
ESCRIBIR hola
ESCRIBIR mundo
MOSTRAR
DESHACER
MOSTRAR
ESCRIBIR clase
MOSTRAR
EOF
python3 problema1_editor.py < test1.txt
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

Crear archivo de prueba:
```bash
cat > test2a.txt << 'EOF'
8
LLEGA Ana
LLEGA Luis
SIGUIENTE
ATIENDE
SIGUIENTE
LLEGA Marta
ATIENDE
ATIENDE
EOF
python3 problema2_urgencias.py < test2a.txt
```

Salida esperada:
```
Ana
Ana
Luis
Luis
Marta
```

---

### Problema 3 — Lista de canciones
**Estructura usada:** Lista enlazada simple (`SingleLinkedList`)  
**Archivo:** `problema3_canciones.py`

> ⚠️ **Pendiente** — asignado al compañero

Operaciones:
- `AGREGAR cancion` — agrega una canción al final
- `INSERTAR posicion cancion` — inserta en una posición específica (base 0)
- `ELIMINAR cancion` — elimina la primera aparición
- `MOSTRAR` — imprime la lista (o `LISTA VACIA`)

---

### Problema 4 — Conteo de productos vendidos
**Estructura usada:** Tabla hash (`HashTable`)  
**Archivo:** `problema4_productos.py`

> ⚠️ **Pendiente** — asignado al compañero

Operaciones:
- `VENDER producto cantidad` — registra unidades vendidas
- `CONSULTAR producto` — imprime unidades vendidas (o `0` si no existe)
- `TOTAL` — imprime el total de unidades vendidas entre todos los productos# Taller_2_ADA