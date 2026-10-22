
# ACTIVIDAD: CADENAS Y ESTRUCTURAS DE DATOS


def mostrar_titulo(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)



# 1. OPERACIONES CON CADENAS


mostrar_titulo("1. OPERACIONES CON CADENAS")

texto = "Aprender Python es divertido"

print("Texto original:", texto)

# Obtener una subcadena.
subcadena = texto[9:15]
print("Subcadena:", subcadena)

# Buscar una palabra específica.
palabra = "Python"
posicion = texto.find(palabra)

if posicion != -1:
    print(
        f"La palabra '{palabra}' comienza "
        f"en la posición {posicion}."
    )
else:
    print(f"La palabra '{palabra}' no se encontró.")

# Reemplazar una palabra por otra.
texto_reemplazado = texto.replace("Python", "programación")
print("Texto con reemplazo:", texto_reemplazado)

# Separar el texto en palabras.
partes = texto.split()
print("Texto separado:", partes)



# 2. LISTAS PARALELAS: NOMBRES Y EDADES


mostrar_titulo("2. BÚSQUEDA EN LISTAS PARALELAS")

nombres = ["Ana", "Luis", "Marta", "Carlos"]
edades = [20, 22, 19, 25]


def buscar_edad(nombre_buscado):
    for indice, nombre in enumerate(nombres):
        if nombre.casefold() == nombre_buscado.strip().casefold():
            return edades[indice]

    return None


print("Nombres:", nombres)
print("Edades:", edades)

# Probar una persona que existe y otra que no existe.
for persona in ["Marta", "Pedro"]:
    edad = buscar_edad(persona)

    if edad is not None:
        print(f"{persona} tiene {edad} años.")
    else:
        print(f"No se encontró a {persona}.")



# 3. LISTA DE DICCIONARIOS


mostrar_titulo("3. LISTA DE USUARIOS")

usuarios = [
    {
        "nombre": "Marta",
        "email": "marta@example.com",
        "ciudad": "Lima"
    },
    {
        "nombre": "Carlos",
        "email": "carlos@example.com",
        "ciudad": "Bogotá"
    },
    {
        "nombre": "Ana",
        "email": "ana@example.com",
        "ciudad": "Lima"
    },
    {
        "nombre": "Luis",
        "email": "luis@example.com",
        "ciudad": "Quito"
    }
]

for usuario in usuarios:
    print(
        f"Nombre: {usuario['nombre']} | "
        f"Email: {usuario['email']} | "
        f"Ciudad: {usuario['ciudad']}"
    )



# 4. BÚSQUEDA TEXTUAL POR CIUDAD


mostrar_titulo("4. BÚSQUEDA POR CIUDAD")


def buscar_por_ciudad(ciudad_buscada):
    consulta = ciudad_buscada.strip().casefold()

    if not consulta:
        return []

    return [
        usuario
        for usuario in usuarios
        if consulta in usuario["ciudad"].casefold()
    ]


# Probar una ciudad con resultados y otra sin resultados.
for ciudad in ["Lima", "Madrid"]:
    print(f"\nBúsqueda por ciudad: {ciudad}")

    coincidencias = buscar_por_ciudad(ciudad)

    if coincidencias:
        for usuario in coincidencias:
            print(
                f"- {usuario['nombre']} | "
                f"{usuario['email']} | "
                f"{usuario['ciudad']}"
            )

        print("Total de coincidencias:", len(coincidencias))
    else:
        print("No se encontraron usuarios en esa ciudad.")



# 5. ORDENAMIENTO ALFABÉTICO


mostrar_titulo("5. NOMBRES ORDENADOS ALFABÉTICAMENTE")

usuarios_ordenados = sorted(
    usuarios,
    key=lambda usuario: usuario["nombre"].casefold()
)

for usuario in usuarios_ordenados:
    print(usuario["nombre"])



# 6. VALIDACIÓN DE RESULTADOS


mostrar_titulo("6. VALIDACIÓN DE RESULTADOS")

assert subcadena == "Python"
assert posicion == 9
assert texto_reemplazado == "Aprender programación es divertido"
assert partes == ["Aprender", "Python", "es", "divertido"]

assert len(nombres) == len(edades)
assert buscar_edad("Marta") == 19
assert buscar_edad("Pedro") is None

assert len(buscar_por_ciudad("Lima")) == 2
assert len(buscar_por_ciudad("Madrid")) == 0

assert [
    usuario["nombre"]
    for usuario in usuarios_ordenados
] == ["Ana", "Carlos", "Luis", "Marta"]

print("Todas las validaciones finalizaron correctamente.")