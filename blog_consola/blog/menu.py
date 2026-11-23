import blog.datos as datos
from blog.operaciones import listar_posts, buscar_por_titulo, buscar_por_tag
from blog.validaciones import validar_posts

def mostrar_menu():

    try:
        showMenu= True
        while(showMenu):
            print("--- MENU DEL BLOG ---")
            print("1. Ver todos los posts")
            print("2. Buscar por titulo")
            print("3. Filtrar por tag")
            print("4. Validar posts")
            print("5. Salir")
            opcion = input("elige una opcion: ")

            if(opcion == "1"):
                listar_posts(datos.posts)
            elif(opcion == "2"):
                busqueda = input('Introduce la palabra a buscar: ').lower().strip()
                buscar_por_titulo(datos.posts, busqueda)
            elif(opcion == "3"):
                busqueda = input("Intoduce el tag a buscar: ").lower().strip()
                buscar_por_tag(datos.posts, busqueda)
            elif(opcion == "4"):
                validar_posts(datos.posts)
            elif(opcion == "5"):
                print("Gracias por usar el sistema del blog. ¡Hasta luego!")
                break
            else:
                print("Opcion invalida. Intenta de nuevo")
    except ValueError:
        print('Debes ingresar un número')
