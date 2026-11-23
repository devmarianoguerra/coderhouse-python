def validar_posts(posts):
    for index, post in enumerate(posts, start=1):
        # titulo = post.get("titulo")
        contenido = post.get("contenido")
        autor = post.get("autor")
        if type(post) != dict:
            print(f"Post {index} - Error: No tiene el formato correcto")
        elif "titulo" not in post or not str(post["titulo"]).strip():
            print(f"Post {index} - Error: falta la clave 'titulo'")
        elif "contenido" not in post or not str(post["contenido"]).strip():
            print(f"Post {index} - Error: falta la clave 'contenido'")
        elif "autor" not in post or not str(post["autor"]).strip():
            print(f"Post {index} - Error: falta la clave 'autor'")
        else:
            print(f"Post {index} - Valido")