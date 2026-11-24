from __future__ import annotations


ESTADOS_POST = ("borrador", "publicado", "archivado")


class Autor:
    def __init__(self, nombre: str, bio: str = "", especialidad: str = "", redes_sociales=None):
        nombre = str(nombre).strip()
        if not nombre:
            raise ValueError("El nombre del autor no puede estar vacío")

        self.nombre = nombre
        self.bio = str(bio).strip()
        self.especialidad = str(especialidad).strip()
        self.redes_sociales = list(redes_sociales or [])

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Autor":
        if not isinstance(datos, dict):
            raise ValueError("Los datos del autor deben ser un diccionario")
        if not str(datos.get("nombre", "")).strip():
            raise ValueError("El autor no contiene un nombre válido")
        return cls(
            nombre=datos["nombre"],
            bio=datos.get("bio", ""),
            especialidad=datos.get("especialidad", ""),
            redes_sociales=datos.get("redes_sociales", []),
        )

    def __str__(self) -> str:
        return self.nombre


class Post:
    def __init__(self, id: int, titulo: str, contenido: str, autor: Autor,
                 tags=None, estado: str = "borrador"):
        titulo = str(titulo).strip()
        contenido = str(contenido).strip()

        if not titulo:
            raise ValueError("El título del post no puede estar vacío")
        if not contenido:
            raise ValueError("El contenido del post no puede estar vacío")
        if not isinstance(autor, Autor):
            raise ValueError("El autor del post debe ser una instancia de Autor")

        estado = str(estado).strip().lower()
        if estado not in ESTADOS_POST:
            raise ValueError("El estado debe ser borrador, publicado o archivado")

        self.id = int(id)
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = [str(tag).strip() for tag in (tags or []) if str(tag).strip()]
        self.estado = estado

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Post":
        if not isinstance(datos, dict):
            raise ValueError("Los datos del post deben ser un diccionario")

        claves = ("id", "titulo", "contenido", "autor", "tags", "estado")
        faltantes = [clave for clave in claves if clave not in datos]
        if faltantes:
            raise ValueError("Faltan claves en el post: " + ", ".join(faltantes))

        autor = Autor.from_dict(datos["autor"])
        return cls(
            id=datos["id"],
            titulo=datos["titulo"],
            contenido=datos["contenido"],
            autor=autor,
            tags=datos["tags"],
            estado=datos["estado"],
        )


class Blog:
    def __init__(self, posts=None):
        self.posts = list(posts or [])

    def listar_posts(self) -> list:
        return self.posts

    def buscar_por_titulo(self, titulo: str) -> list:
        texto = str(titulo).strip().lower()
        if not texto:
            return []
        return [post for post in self.posts if texto in post.titulo.lower()]

    def filtrar_por_tag(self, tag: str) -> list:
        texto = str(tag).strip().lower()
        if not texto:
            return []
        return [
            post for post in self.posts
            if any(texto == str(post_tag).strip().lower() for post_tag in post.tags)
        ]

    def agregar_post(self, post: Post) -> None:
        if not isinstance(post, Post):
            raise ValueError("Solo se pueden agregar instancias de Post")
        self.posts.append(post)

    def crear_post(self, titulo: str, contenido: str, autor: Autor,
            tags=None, estado: str = "borrador") -> Post:
        nuevo_id = max((post.id for post in self.posts), default=0) + 1
        nuevo_post = Post(nuevo_id, titulo, contenido, autor, tags, estado)
        self.agregar_post(nuevo_post)
        return nuevo_post

    def validar_posts(self) -> list:
        resultados = []
        for numero, post in enumerate(self.posts, start=1):
            try:
                if not isinstance(post, Post):
                    raise ValueError("No es una instancia de Post")
                if not post.titulo.strip():
                    raise ValueError("falta el título")
                if not post.contenido.strip():
                    raise ValueError("falta el contenido")
                if not isinstance(post.autor, Autor):
                    raise ValueError("el autor no es una instancia de Autor")
                resultados.append((numero, True, "Válido"))
            except (ValueError, AttributeError) as error:
                resultados.append((numero, False, str(error)))
        return resultados

    def obtener_posts(self) -> list:
        return self.posts



