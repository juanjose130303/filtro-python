import json
from menus import menu_principal, menu_gestor_informes, menu_gestor_peliculas
from funciones import agregar_pelicula, editar_pelicula, eliminar_pelicula, eliminar_actor, buscar_pelicula, listar_todas_peliculas, listar_peliculas_por_genero, listar_peliculas_por_protagonista, buscar_pelicula_mostrar_info

def cargar_datos():
    try:
        with open("blockbuster_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"blockbuster": {"peliculas": {}, "generos": {}}}
    return data


def administrador_generos(data):
    while True:
        print("\nADMINISTRADOR DE GÉNEROS")
        print("1 Crear género")
        print("2 Listar géneros")
        print("3 Ir al Menú principal")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            crear_genero(data)
        elif opcion == "2":
            listar_generos(data)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

def crear_genero(data):
    genero_id = input("Ingrese el ID del género: ")
    genero_nombre = input("Ingrese el nombre del género: ")

    # Crear estructura de género
    genero = {"id": genero_id, "nombre": genero_nombre}

    # Agregar género a los datos
    data["blockbuster"]["generos"][genero_id] = genero

    print("Género creado con éxito.")

def listar_generos(data):
    print("\nLISTA DE GÉNEROS:")
    for genero_id, genero_info in data["blockbuster"]["generos"].items():
        print(f"ID: {genero_id}, Nombre: {genero_info['nombre']}")


def guardar_datos(data):
    with open("blockbuster_data.json", "w") as file:
        json.dump(data, file, indent=4)

def administrador_generos(data):
    while True:
        print("\nADMINISTRADOR DE GÉNEROS")
        print("1 Crear género")
        print("2 Listar géneros")
        print("3 Ir al Menú principal")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            crear_genero(data)
        elif opcion == "2":
            listar_generos(data)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

def crear_genero(data):
    genero_id = input("Ingrese el ID del género: ")
    genero_nombre = input("Ingrese el nombre del género: ")

    genero = {"id": genero_id, "nombre": genero_nombre}

    data["blockbuster"]["generos"][genero_id] = genero

    print("Género creado con éxito.")

def listar_generos(data):
    print("\nLISTA DE GÉNEROS:")
    for genero_id, genero_info in data["blockbuster"]["generos"].items():
        print(f"ID: {genero_id}, Nombre: {genero_info['nombre']}")

def gestor_informes(data):
    while True:
        menu_gestor_informes()
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            listar_peliculas_por_genero(data)
        elif opcion == "2":
            listar_peliculas_por_protagonista(data)
        elif opcion == "3":
            buscar_pelicula_mostrar_info(data)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

def gestor_peliculas(data):
    while True:
        menu_gestor_peliculas()
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            agregar_pelicula(data)
        elif opcion == "2":
            editar_pelicula(data)
        elif opcion == "3":
            eliminar_pelicula(data)
        elif opcion == "4":
            eliminar_actor(data)
        elif opcion == "5":
            buscar_pelicula(data)
        elif opcion == "6":
            listar_todas_peliculas(data)
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

def main():
    data = cargar_datos()

    while True:
        menu_principal()
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            administrador_generos(data)
        elif opcion == "2":
            print("a jugar ping pong?")
        elif opcion == "3":
            print("incompleto me faltó")
        elif opcion == "4":
            gestor_informes(data)
        elif opcion == "5":
            gestor_peliculas(data)
        elif opcion == "6":
            guardar_datos(data)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()