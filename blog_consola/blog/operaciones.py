def listar_posts(posts):
     print("Posts disponbles: ")
     for post in posts:
      print(f"{post["titulo"]} | {post["autor"]["nombre"]}")

def buscar_por_titulo(posts, busqueda):
    print("Posts encontrados: ")
    for post in posts:
        if busqueda in post["titulo"].lower().strip():
            print(f"{post["titulo"]}")

def buscar_por_tag(posts, tag_buscado):
     print("Tags encontrados: ")
     for post in posts:
        for tag in post["tags"]:
            if tag_buscado == tag: 
                print(f"Posts con el tag {tag_buscado}")
                print(f"{post["titulo"]}")