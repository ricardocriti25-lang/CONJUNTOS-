# Sistema de biblioteca escolar

libros = {
    1: {"titulo": "Matematicas", "autor": "Juan Perez"},
    2: {"titulo": "Programacion", "autor": "Ana Lopez"},
    3: {"titulo": "Historia", "autor": "Luis Garcia"},
    4: {"titulo": "Base de Datos", "autor": "Maria Ruiz"},
    5: {"titulo": "Ingles", "autor": "Pedro Torres"}
}

disponibles = {1, 2, 3}
prestados = {4, 5}

# Operaciones de conjuntos
print("Todos los libros:", disponibles.union(prestados))
print("Libros en ambos estados:", disponibles.intersection(prestados))
print("Libros disponibles:", disponibles.difference(prestados))

# Busqueda por identificador
try:
    buscar = int(input("Ingresa el ID del libro: "))
    if buscar in libros:
        print("Libro encontrado:", libros[buscar])
        if buscar in disponibles:
            print("Estado: Disponible")
        elif buscar in prestados:
            print("Estado: Prestado")
    else:
        print("El libro no existe")
except ValueError:
    print("Ingresa un numero de identificacion valido")
