# ToDo API — Demo 001

API RESTful para la gestión de tareas (ToDo) construida con Django y Django REST Framework.

Este proyecto es el resultado del aprendizaje práctico obtenido en el certificado **"Automatización de TI con Python" de Google**, impartido en **Coursera**. Representa la **Demo 001**, un primer acercamiento al desarrollo de APIs Web utilizando el ecosistema Django.

## Stack tecnológico

| Tecnología | Versión |
|---|---|
| Python | 3.x |
| Django | 6.0.6 |
| Django REST Framework | Última |
| SQLite | 3.x |

## Modelo de datos

La API gestiona un único recurso llamado `Project`, que representa una tarea:

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Integer (PK) | Identificador único (autogenerado) |
| `title` | CharField(200) | Título de la tarea |
| `description` | TextField | Descripción detallada |
| `status` | BooleanField | `False` = pendiente, `True` = completada |
| `created_at` | DateTimeField | Fecha de creación (solo lectura) |
| `updated_at` | DateTimeField | Última modificación (solo lectura) |

## Endpoints de la API

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/api/projects/` | Listar todas las tareas |
| `POST` | `/api/projects/` | Crear una nueva tarea |
| `GET` | `/api/projects/{id}/` | Obtener detalle de una tarea |
| `PUT` | `/api/projects/{id}/` | Actualizar una tarea completa |
| `PATCH` | `/api/projects/{id}/` | Actualización parcial de una tarea |
| `DELETE` | `/api/projects/{id}/` | Eliminar una tarea |

## Cómo ejecutar

1. Clonar el repositorio y acceder al directorio:
   ```bash
   cd ToDo
   ```

2. Activar el entorno virtual:
   ```bash
   .\venv\Scripts\activate
   ```

3. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

4. La API estará disponible en `http://localhost:8000/api/projects/`

## Ejemplo de uso

### Crear una tarea
```bash
curl -X POST http://localhost:8000/api/projects/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Aprender Django", "description": "Completar el tutorial oficial", "status": false}'
```

### Listar tareas
```bash
curl http://localhost:8000/api/projects/
```

## Estructura del proyecto

```
ToDo/
├── ToDoProject/       # Configuración del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── projects/          # Aplicación de la API
│   ├── api.py         # ViewSet con la lógica CRUD
│   ├── models.py      # Definición del modelo Project
│   ├── serializers.py # Serializador para JSON
│   └── urls.py        # Rutas registradas con DRF Router
├── manage.py
├── db.sqlite3         # Base de datos SQLite
└── README.md
```

## Licencia

Demo 001 — Proyecto resultado del aprendizaje en el certificado **"Google IT Automation with Python"**, impartido en Coursera.
