from blog.modelos import Autor, Post


def validar_posts(posts):
    resultados = []

    for index, post in enumerate(posts, start=1):
        if not isinstance(post, Post):
            resultado = "Error: No tiene el formato correcto"
        elif not str(post.titulo).strip():
            resultado = "Error: falta el título"
        elif not str(post.contenido).strip():
            resultado = "Error: falta el contenido"
        elif not isinstance(post.autor, Autor) or not str(post.autor.nombre).strip():
            resultado = "Error: el autor no es válido"
        else:
            resultado = "Válido"

        print(f"Post {index} - {resultado}")
        resultados.append(resultado)

    return resultados