# Sistema de administración de blog

Sistema de consola para administrar publicaciones de un blog con Python. Permite listar, buscar por título, filtrar por tag, crear, validar y guardar posts.

## Ejecución

Desde la carpeta raíz del proyecto:

```bash
cd blog_consola
python3 main.py
```

## Estructura

```text
blog_consola/
├── main.py
├── README.md
├── posts.json
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

## Clases principales

- `Autor`: representa nombre, bio, especialidad y redes sociales.
- `Post`: representa una publicación y contiene una instancia de `Autor`, además de id, título, contenido, tags y estado.
- `Blog`: contiene la lista de objetos `Post` y centraliza listar, buscar, filtrar, crear y validar publicaciones.

Las clases tienen métodos `to_dict()` y `from_dict()` para convertir objetos hacia y desde diccionarios compatibles con JSON.

## Responsabilidades de los módulos

- `main.py`: carga los datos, crea la instancia `Blog` y protege la ejecución principal con `if __name__ == "__main__":`.
- `blog/modelos.py`: define las clases `Autor`, `Post` y `Blog`.
- `blog/datos.py`: carga y guarda los posts en `posts.json`; procesa archivos inexistentes, vacíos o con JSON inválido.
- `blog/menu.py`: muestra el menú e interactúa con la instancia de `Blog`.
- `blog/operaciones.py`: conserva funciones auxiliares compatibles con el nuevo modelo.
- `blog/validaciones.py`: valida los objetos cargados o creados.

## Persistencia JSON

Al iniciar, el programa lee `posts.json` y reconstruye objetos `Autor` y `Post`. La opción 6 del menú convierte los objetos a diccionarios y los guarda en el archivo. También se puede iniciar sin el archivo o con un archivo vacío sin que el programa se cierre inesperadamente.

## Cambios de este checkpoint

- Se incorporaron las clases `Autor`, `Post` y `Blog`.
- Los posts pasan a relacionarse con instancias de `Autor`.
- La colección y las operaciones principales están centralizadas en `Blog`.
- Se agregó conversión entre objetos y diccionarios.
- Se agregó carga y guardado de datos desde `posts.json`.
- El menú fue integrado con el objeto `Blog` y ahora maneja entradas vacías o inválidas.
