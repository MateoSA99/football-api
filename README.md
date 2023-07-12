# football-api
Esta es una API de Fútbol creada por Mateo Soto Arango en compañía de la mano de Team International. La API usa tecnologías como Django, Django Rest FrameWork, Celery, Redis, PostgreSQL, Token de Autenticación y Render para el despliegue.

La idea de la API es crear tu equipo de fútbol y asociarle sus respectivos jugadores.

# Antes de comenzar a usar la API asegurese de ejecutar:
Luego de clonar el repositorio, compruebe que está en la carpeta:
```bash
cd football-api
```
Cree un entorno virtual con:
```python
python -m venv your_env_name
```
Active el entorno virtual y finalmente ejecute:

```python
pip install -r requirements.txt
```
Para tener todo lo necesario para iniciar.

# Primeros Pasos
`1.` En una primer terminal ejecute:

```python
python manage.py runserver
```
para iniciar la aplicación.

`2.` Ejecute para iniciar celery

```python
 celery -A api worker --loglevel=info
```

`3.` Vaya a: **http://127.0.0.1:8000/** y será redirigido a **http://127.0.0.1:8000/football/signup** y siga las instrucciones que allí aparecen.
Note que al iniciar sesión o registrarse en la api recibirá un email de confirmación.

`4.` Navegue libremente por la api









