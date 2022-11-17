<div align="center"> <h1> Correr el proyecto en local </h1> </div>

- Clonar repositorio y cambiar a la rama "dev" con

```
  git checkout dev
```

- Para el entorno virtual utilicé

```
py -m venv venv
```

- Correr el entorno virtual

```
.\venv\Scripts\activate
```

- Instalar dependencias del requirements.txt en el entorno virtual

```
pip install -r requirements.txt
```

- Crear las migraciones

```
py manage.py makemigrations
```

- Correr las migraciones en la Base de Datos

```
py manage.py migrate
```

- Crear un superusuario para poder acceder al sitio

```
py manage.py createsuperuser
```


<div align="center"> <h1> Credenciales de admin para el sitio live </h1> </div>

- username: admin
- password: adminpass