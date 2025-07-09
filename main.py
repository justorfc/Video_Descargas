import os
import subprocess

# === Paso 1: Solicita la URL ===
url = input("Ingresa la URL del video de YouTube: ").strip()

# === Paso 2: Crear carpeta de descarga ===
folder_name = "descargas_youtube"
os.makedirs(folder_name, exist_ok=True)

# === Paso 3: Elegir tipo de descarga ===
print("\n¿Qué deseas descargar?")
print("1. Video MP4")
print("2. Audio MP3")
choice = input("Elige 1 o 2: ").strip()

# === Paso 4: Preparar comando yt-dlp ===
if choice == "1":
    # Descargar video en formato MP4
    cmd = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "-o", os.path.join(folder_name, "%(title)s.%(ext)s"),
        url
    ]
elif choice == "2":
    # Descargar audio y convertir a MP3
    cmd = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "192K",
        "-o", os.path.join(folder_name, "%(title)s.%(ext)s"),
        url
    ]
else:
    print("Opción no válida.")
    exit()

# === Paso 5: Ejecutar el comando yt-dlp ===
try:
    subprocess.run(cmd, check=True)
    print("\n✅ Descarga completada.")
except subprocess.CalledProcessError as e:
    print("\n❌ Ocurrió un error durante la descarga.")
    print(str(e))
