def agregar_pelicula(data):
    codigo = input("Ingrese el código de la película: ")
    nombre = input("Ingrese el nombre de la película: ")
    duracion = input("Ingrese la duración de la película: ")
    sinopsis = input("Ingrese la sinopsis de la película: ")

    # Obtener género
    genero_id = input("Ingrese el ID del género de la película: ")
    genero_nombre = input("Ingrese el nombre del género de la película: ")
    genero = {"id": genero_id, "nombre": genero_nombre}

    # Obtener actor
    actor_id = input("Ingrese el ID del actor: ")
    actor_nombre = input("Ingrese el nombre del actor: ")
    actor_rol = input("Ingrese el rol del actor (protagonista, antagonista, reparto): ")
    actor = {"id": actor_id, "nombre": actor_nombre, "rol": actor_rol}

    # Obtener formato
    formato_id = input("Ingrese el ID del formato: ")
    formato_nombre = input("Ingrese el nombre del formato: ")
    formato_nro_copias = int(input("Ingrese el número de copias del formato: "))
    formato_valor_prestamo = float(input("Ingrese el valor de prestamo del formato: "))
    formato = {"id": formato_id, "nombre": formato_nombre, "NroCopias": formato_nro_copias, "ValorPrestamo": formato_valor_prestamo}

    # Crear estructura de película
    pelicula = {
        "id": codigo,
        "nombre": nombre,
        "duracion": duracion,
        "sinopsis": sinopsis,
        "generos": {genero_id: genero},
        "actores": {actor_id: actor},
        "formato": {formato_id: formato}
    }

    # Agregar película a los datos
    data["blockbuster"]["peliculas"][codigo] = pelicula

    print("Película agregada con éxito.")

def editar_pelicula(data):
    codigo = input("Ingrese el código de la película que desea editar: ")

    if codigo in data["blockbuster"]["peliculas"]:
        # Código para editar una película existente
        pass
    else:
        print("Película no encontrada.")

def eliminar_pelicula(data):
    codigo = input("Ingrese el código de la película que desea eliminar: ")

    if codigo in data["blockbuster"]["peliculas"]:
        del data["blockbuster"]["peliculas"][codigo]
        print("Película eliminada con éxito.")
    else:
        print("Película no encontrada.")

def eliminar_actor(data):
    codigo_pelicula = input("Ingrese el código de la película de la cual desea eliminar un actor: ")

    if codigo_pelicula in data["blockbuster"]["peliculas"]:
        actor_id = input("Ingrese el ID del actor que desea eliminar: ")

        if actor_id in data["blockbuster"]["peliculas"][codigo_pelicula]["actores"]:
            del data["blockbuster"]["peliculas"][codigo_pelicula]["actores"][actor_id]
            print("Actor eliminado con éxito.")
        else:
            print("Actor no encontrado en la película.")
    else:
        print("Película no encontrada.")

def buscar_pelicula(data):
    codigo = input("Ingrese el código de la película que desea buscar: ")

    if codigo in data["blockbuster"]["peliculas"]:        
        pass
    else:
        print("Película no encontrada.")

def listar_todas_peliculas(data):
    print("\nLISTA DE PELÍCULAS:")
    for pelicula_id, pelicula_info in data["blockbuster"]["peliculas"].items():
        print(f"Código: {pelicula_id}, Nombre: {pelicula_info['nombre']}, Duración: {pelicula_info['duracion']} minutos")

def listar_peliculas_por_genero(data):
    genero_id = input("Ingrese el ID del género: ")

    if genero_id in data["blockbuster"]["generos"]:
        print("\nLISTA DE PELÍCULAS POR GÉNERO:")
        for pelicula_id, pelicula_info in data["blockbuster"]["peliculas"].items():
            if genero_id in pelicula_info["generos"]:
                print(f"Código: {pelicula_id}, Nombre: {pelicula_info['nombre']}")
    else:
        print("Género no encontrado.")

def listar_peliculas_por_protagonista(data):
    actor_nombre = input("Ingrese el nombre del protagonista: ")

    peliculas_protagonista = []
    for pelicula_id, pelicula_info in data["blockbuster"]["peliculas"].items():
        for actor_id, actor_info in pelicula_info["actores"].items():
            if actor_info["nombre"] == actor_nombre and actor_info["rol"] == "protagonista":
                peliculas_protagonista.append({"Código": pelicula_id, "Nombre": pelicula_info["nombre"]})

    if peliculas_protagonista:
        print("\nLISTA DE PELÍCULAS CON EL PROTAGONISTA:")
        for pelicula in peliculas_protagonista:
            print(f"Código: {pelicula['Código']}, Nombre: {pelicula['Nombre']}")
    else:
        print("No se encontraron películas con el protagonista especificado.")

def buscar_pelicula_mostrar_info(data):
    codigo = input("Ingrese el código de la película que desea buscar: ")

    if codigo in data["blockbuster"]["peliculas"]:
        pelicula_info = data["blockbuster"]["peliculas"][codigo]
        print(f"\nINFORMACIÓN DE LA PELÍCULA {codigo}:")
        print(f"Nombre: {pelicula_info['nombre']}")
        print(f"Duración: {pelicula_info['duracion']} minutos")
        print(f"Sinopsis: {pelicula_info['sinopsis']}")

        print("\nACTORES:")
        for actor_id, actor_info in pelicula_info["actores"].items():
            print(f"ID: {actor_id}, Nombre: {actor_info['nombre']}, Rol: {actor_info['rol']}")

    else:
        print("Película no encontrada.")
