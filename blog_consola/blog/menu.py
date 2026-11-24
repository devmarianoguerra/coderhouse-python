from blog.datos import guardar_posts
from blog.modelos import Autor, ESTADOS_POST

def mostrar_posts(posts):
    if not posts:
        print("No hay posts disponibles.")
        return
    for post in posts:
        print(f"{post.id}. {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")


def mostrar_menu(blog):
    while True:
        print("\n--- MENU DEL BLOG ---")
        print("1. Ver todos los posts")
        print("2. Buscar por titulo")
        print("3. Filtrar por tag")
        print("4. Crear nuevo post")
        print("5. Validar posts")
        print("6. Guardar posts en JSON")
        print("7. Salir")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            mostrar_posts(blog.listar_posts())

        elif opcion == "2":
            texto = input("Introduce el titulo a buscar: ").strip()
            if not texto:
                print("Error: la búsqueda no puede estar vacía.")
            else:
                mostrar_posts(blog.buscar_por_titulo(texto))

        elif opcion == "3":
            tag = input("Introduce el tag a buscar: ").strip()
            if not tag:
                print("Error: el tag no puede estar vacío.")
            else:
                mostrar_posts(blog.filtrar_por_tag(tag))

        elif opcion == "4":
            try:
                titulo = input("Introduce un titulo: ").strip()
                contenido = input("Introduce el contenido: ").strip()
                nombre_autor = input("Introduce el nombre del autor: ").strip()
                if not titulo or not contenido or not nombre_autor:
                    raise ValueError("El título, el contenido y el autor son obligatorios")

                bio = input("Introduce la bio del autor (opcional): ").strip()
                especialidad = input("Introduce la especialidad (opcional): ").strip()
                redes = input("Introduce redes separadas por coma (opcional): ").strip()
                redes_sociales = [valor.strip() for valor in redes.split(",") if valor.strip()] if redes else []

                autor = Autor(nombre_autor, bio, especialidad, redes_sociales)

                print("Selecciona el estado del post:")
                for indice, estado in enumerate(ESTADOS_POST, start=1):
                    print(f"{indice}. {estado}")

                seleccion = input("Elige el número de tu opción: ").strip()
                if not seleccion.isdigit() or not 1 <= int(seleccion) <= len(ESTADOS_POST):
                    raise ValueError("Estado inválido")
                estado = ESTADOS_POST[int(seleccion) - 1]

                tags_texto = input("Ingresa los tags separados por una coma: ").strip()
                tags = [tag.strip() for tag in tags_texto.split(",") if tag.strip()] if tags_texto else []

                nuevo_post = blog.crear_post(titulo, contenido, autor, tags, estado)
                print(f"Post creado correctamente: {nuevo_post.titulo}")
            except ValueError as error:
                print(f"Error al crear el post: {error}")

        elif opcion == "5":
            resultados = blog.validar_posts()
            if not resultados:
                print("No hay posts para validar.")
            for numero, es_valido, mensaje in resultados:
                print(f"Post {numero} - {'Válido' if es_valido else 'Error: ' + mensaje}")

        elif opcion == "6":
            guardar_posts(blog.obtener_posts())

        elif opcion == "7":
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")
