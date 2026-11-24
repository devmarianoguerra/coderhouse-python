import json
from pathlib import Path

from blog.modelos import Post


BASE_DIR = Path(__file__).resolve().parent.parent
POSTS_PATH = BASE_DIR / "posts.json"
LEGACY_POSTS_PATH = BASE_DIR / "blog" / "posts.json"


def cargar_posts() -> list:
    ruta = POSTS_PATH if POSTS_PATH.exists() else LEGACY_POSTS_PATH

    if not ruta.exists():
        print("No existe posts.json. Se inicia un blog sin publicaciones.")
        return []

    try:
        if ruta.stat().st_size == 0:
            print("posts.json está vacío. Se inicia un blog sin publicaciones.")
            return []

        with ruta.open("r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            print("Error: posts.json debe contener una lista de publicaciones.")
            return []

        posts = []
        for indice, dato in enumerate(datos, start=1):
            try:
                posts.append(Post.from_dict(dato))
            except (ValueError, KeyError, TypeError) as error:
                print(f"Post {indice} inválido y no pudo cargarse: {error}")
        return posts

    except json.JSONDecodeError:
        print("Error: posts.json contiene JSON inválido. Se inicia un blog sin publicaciones.")
        return []
    except OSError as error:
        print(f"No se pudo leer posts.json: {error}")
        return []


def guardar_posts(posts) -> bool:
    try:
        lista_diccionarios = []
        for post in posts:
            if not hasattr(post, "to_dict") or not callable(post.to_dict):
                raise ValueError("Se encontró un objeto que no puede convertirse a diccionario")
            dato = post.to_dict()
            if not isinstance(dato, dict):
                raise ValueError("to_dict() debe devolver un diccionario")
            lista_diccionarios.append(dato)

        POSTS_PATH.parent.mkdir(parents=True, exist_ok=True)
        with POSTS_PATH.open("w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
        print("Posts guardados correctamente en posts.json")
        return True

    except (OSError, ValueError, TypeError) as error:
        print(f"Error al guardar posts.json: {error}")
        return False


# Este es un diccionario 
perfil_autor = {
    "nombre": "Mariano",
    "bio": "Lorem Ipsum",
    "especialidad": "JavaScript",
    "redes_sociales": ["@mariano_frontend", "@mariano_developer"]
}


#Esta es una tupla
estados_post = ("borrador", "publicado", "archivado")

#Este es un set
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

#Esta es una lista
posts = [
    {
        "id":1,
        "titulo": "Primeros pasos con Python",
        "autor": perfil_autor,
        "contenido": "Blog de Python",
        "tags": ["programacion", "python"],
        "estado": "publicado"
    },
    {
        "id":2,
        "titulo": "Aprendiendo Javascript",
        "autor": perfil_autor,
        "contenido": "Blog de Javascript",
        "tags": ["programacion", "javascript"],
        "estado": "borrador"
    },
    {
        "id":3,
        "titulo": "Creando una API con Java y SpringBoot",
        "autor": perfil_autor,
        "tags": ["programacion", "java"],
        "estado": "archivado"
    }
]