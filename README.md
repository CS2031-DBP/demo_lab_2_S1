# Semana 1

Este proyecto consiste en una API con FastAPI y un frontend simple. Para desarrollar, necesitarás instalar y configurar algunas herramientas como Visual Studio Code y Postman. Sigue los pasos a continuación para configurar tu entorno de trabajo y ejecutar el proyecto.

## Requisitos

- **Postman**: para probar las solicitudes API.
- **Visual Studio Code**: como entorno de desarrollo.
- **Extensiones de VS Code**:
  - [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Configuración

### 1. Clonar el Repositorio

1. Selecciona una carpeta existente en tu sistema, por ejemplo: `Desktop`.
2. Abre una terminal y navega a la carpeta seleccionada:

   ```bash
   cd Desktop
   ```

3. Asegúrate de configurar tu cuenta de Git antes de clonar el repositorio:

   ```bash
   git config --global user.name "ejemplo"
   git config --global user.email "ejemplo@mail.com"
   ```

4. Clona el repositorio:

   ```bash
   git clone https://github.com/CS2031-DBP/demo_lab_2_S1.git
   ```

### 2. Abrir el Proyecto en Visual Studio Code

1. Abre Visual Studio Code.
2. Desde VS Code, selecciona "Abrir Carpeta" y navega hasta el directorio `demo_lab_2_S1` que clonaste en el paso anterior.

### 3. Instalar Dependencias del Backend

1. Dentro de VS Code, abre una terminal integrada.
2. Navega al directorio del backend:

   ```bash
   cd backend
   ```

3. Instala las dependencias necesarias para FastAPI:

   ```bash
   pip install "fastapi[standard]"
   ```

   Si encuentras problemas con `pip`, prueba los siguientes comandos:

   - `pip3 install "fastapi[standard]"`
   - `python3 -m pip install "fastapi[standard]"`
   - `py -m pip install "fastapi[standard]"`
   - `python -m pip install "fastapi[standard]"`

   **Nota**: Si nada de esto funciona, reinstala Python desde la [Microsoft Store](https://apps.microsoft.com/store/detail/python-39/9P7QFQMJRFP7) (si estás en Windows). En otros sistemas operativos, Python debería estar preinstalado.

### 4. Ejecutar la API

Para iniciar el servidor de la API, ejecuta el siguiente comando desde el directorio `backend`:

```bash
uvicorn main:app --reload
```

La API debería estar disponible en `http://127.0.0.1:8000`.

## Ejecutar el Frontend

1. Navega al directorio `frontend` usando el explorador de archivos en Visual Studio Code.
2. Haz clic derecho en `index.html` y selecciona la opción **"Open with Live Server"**.

Esto abrirá el frontend en tu navegador web predeterminado.

## Uso de Postman para Probar Endpoints

### ¿Qué es Postman?
Postman es una herramienta utilizada para probar y desarrollar APIs. Permite enviar solicitudes HTTP y visualizar las respuestas, lo que es útil para asegurarte de que tu API funcione correctamente.

### Cómo Probar Endpoints en Postman

1. **Descargar e instalar Postman**: Si aún no lo has hecho, puedes descargar Postman desde [aquí](https://www.postman.com/downloads/).

2. **Abrir Postman**: Una vez que Postman esté instalado, ábrelo para empezar a probar los endpoints de tu API.

### Probando el Endpoint `GET /animes`

1. **Crear una nueva solicitud**:
   - En la interfaz de Postman, haz clic en el botón **"New"** y selecciona **"Request"**.
   - Nombra la solicitud como desees (ej. `Get Animes`) y selecciona o crea una colección donde guardarla.

2. **Configurar la solicitud**:
   - Selecciona el método `GET` en el menú desplegable.
   - En el campo de URL, ingresa: `http://localhost:8000/animes`.
   - No necesitas agregar un cuerpo a la solicitud `GET`.

3. **Enviar la solicitud**:
   - Haz clic en el botón **"Send"**.
   - Deberías recibir una respuesta JSON con la lista de animes si el endpoint está funcionando correctamente.

### Probando el Endpoint `POST /animes`

1. **Crear una nueva solicitud**:
   - Igual que antes, haz clic en **"New"** y selecciona **"Request"**.
   - Nombra la solicitud como desees (ej. `Create Anime`) y selecciona o crea una colección donde guardarla.

2. **Configurar la solicitud**:
   - Selecciona el método `POST`.
   - En el campo de URL, ingresa: `http://localhost:8000/animes`.

3. **Agregar el cuerpo de la solicitud**:
   - Haz clic en la pestaña **"Body"**.
   - Selecciona **"raw"** y luego **"JSON"** en el menú desplegable.
   - Ingresa el siguiente JSON en el área de texto:

   ```json
   {
       "coverImageUrl": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx114129-RLgSuh6YbeYx.jpg",
       "title": "Gintama: THE FINAL",
       "genres": [
           "action",
           "comedy",
           "drama",
           "sci-fi"
       ],
       "rating": 91,
       "kind": "Movie",
       "reviews": 38620,
       "season": "Winter 2021"
   }
   ```

4. **Enviar la solicitud**:
   - Haz clic en el botón **"Send"**.
   - Si la solicitud es exitosa, deberías recibir una respuesta que confirme que el anime ha sido creado.

### Verificando la Operación
- Después de realizar el `POST`, puedes usar el `GET` para verificar que el nuevo anime se ha agregado correctamente a la lista.

### Consejos Adicionales
- **Revisa las respuestas de error**: Si algo sale mal, Postman te mostrará el mensaje de error. Esto puede ayudarte a depurar problemas con tu API.
- **Guarda tus solicitudes**: Puedes guardar cada solicitud en una colección para que puedas reutilizarlas en el futuro.

  
## Notas

- Asegúrate de que Python esté correctamente instalado y configurado en tu sistema.
- Si encuentras problemas, verifica que las extensiones de VS Code estén instaladas correctamente y que las dependencias del proyecto se hayan instalado sin errores.
  
¡Y eso es todo! Con estos pasos, deberías poder probar tus endpoints utilizando Postman y asegurarte de que tu API funcione correctamente.
