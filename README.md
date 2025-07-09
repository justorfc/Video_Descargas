A continuación se presenta el archivo `README.md` del proyecto **Video\_Descargas**, incluyendo:

* Descripción del propósito
* Instrucciones de uso
* Requisitos
* Captura de línea de comandos (simulada)
* Créditos

---

## ✅ Contenido para `README.md`

Guarda este contenido en un archivo llamado `README.md` dentro de tu carpeta del proyecto:

````markdown
# 🎬 Video_Descargas

Aplicación de consola desarrollada en Python para descargar videos o audios desde YouTube utilizando `yt-dlp` y `ffmpeg`.

## 📌 Funcionalidad

- ✅ Descarga videos en formato MP4 con audio incluido.
- ✅ Descarga audios en formato MP3 de alta calidad.
- ✅ Crea una carpeta automática `descargas_youtube/` donde guarda los archivos.
- ✅ Totalmente operativa desde consola.

---

## 🛠 Requisitos

- Python 3.8 o superior  
- `yt-dlp`: para manejar descargas de YouTube  
- `ffmpeg`: para combinar video/audio o convertir a MP3  

### ▶ Instalación de dependencias

```bash
pip install yt-dlp
````

### ▶ Instalación de ffmpeg (Windows)

1. Descargar desde: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Extraer en `C:\ffmpeg`
3. Agregar `C:\ffmpeg\bin` al **PATH** del sistema
4. Verificar:

```bash
ffmpeg -version
```

---

## 🚀 Cómo usar

Desde terminal:

```bash
python main.py
```

El programa solicitará la URL del video y el tipo de descarga (video o audio).

Ejemplo de ejecución:

```
Ingresa la URL del video de YouTube: https://www.youtube.com/watch?v=abc123xyz
¿Qué deseas descargar?
1. Video MP4
2. Audio MP3
Elige 1 o 2: 1
Descargando video...
✅ Descarga completada.
```

---

## 📁 Estructura del proyecto

```
Video_Descargas/
├── main.py
├── .gitignore
├── requirements.txt
├── README.md
└── descargas_youtube/     <-- Carpeta donde se almacenan los archivos descargados (ignorada en Git)
```

---

## 🧾 Autor

Desarrollado por Justo Fuentes
Docente de Programación con Python y Estadística Aplicada – Universidad de Sucre

---

## ⚖️ Licencia

Este proyecto puede ser utilizado con fines educativos y personales. Se agradece dar crédito al autor.