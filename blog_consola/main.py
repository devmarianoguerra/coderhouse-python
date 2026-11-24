from blog.datos import cargar_posts
from blog.menu import mostrar_menu
from blog.modelos import Blog


def main():
    posts = cargar_posts()
    blog = Blog(posts)
    mostrar_menu(blog)


if __name__ == "__main__":
    main()
