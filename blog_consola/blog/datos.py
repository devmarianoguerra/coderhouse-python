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