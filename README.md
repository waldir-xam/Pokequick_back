# **Flask Boilerplate**

## **1. Crear entorno** 
---

```py
python -m venv venv
```

## **2. Crear archivo .env con los siguientes valores de las variables de entorno** 
---

```py
FLASK_APP='main.py'
FLASK_DEBUG=True
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
ENVIRONMENT= 'development'

DATABASE_URL='postgresql://postgres:ratatrampa@localhost:5432/collection'

JWT_SECRET='Pokemon'
```
> **Nota:** En la variable DATABASE_URL se debe cambiar el usuario y contraseña de postgres, el nombre de la base de datos y el puerto de la base de datos.

## **2. Activar entorno** 
---
```py
venv/Scripts/activate         |Windows
source venv/Scripts/activate  |Bash
source venv/bin/activate      |MacOS
```

## **3. Instalar las dependencias usadas** 
---
```py
pip install -r requirements.txt
```

## **4. Instalar dotenv** 
---

```py
 pip install python-dotenv
```

## **5. Guardar dependencias, ejecutar cada que se instalen complementos** 
---

```py
pip freeze > requirements.txt
```

## **6. Iniciar Flask** 
---

```py
Flask run
```

# **Migraciones**

### **1. Iniciar migraciones(se ejecuta una sola vez)**

```sh
flask db init
```
> **Nota:** si hay un error al ejecutar este comando, se debe eliminar la carpeta migrations y volver a ejecutar el comando. 

### **2. Crear una migracion(cuando se crea o modifica un modelo)**

```sh
flask db migrate -m "comentario"
```


### **3. Subir los cambios a nuestra bd**

```sh
flask db upgrade
```
