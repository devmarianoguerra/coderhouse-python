def listar_posts(blog):
    posts = blog.listar_posts()
    if not posts:
        print("No hay posts disponibles.")
        return
    for post in posts:
        print(f"{post.titulo} | {post.autor.nombre} | {post.estado}")


def buscar_por_titulo(blog, busqueda):
    posts = blog.buscar_por_titulo(busqueda)
    if not posts:
        print("No se encontraron posts.")
        return
    for post in posts:
        print(post.titulo)


def buscar_por_tag(blog, tag):
    posts = blog.filtrar_por_tag(tag)
    if not posts:
        print("No se encontraron posts con ese tag.")
        return
    for post in posts:
        print(post.titulo)