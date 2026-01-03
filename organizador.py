import os
import shutil

# Definir la carpeta de descargas
carpeta_descargas = os.getcwd()

# Definir las carpteas destino para cada tipo de archivo
carpeta_imagenes = os.path.join(carpeta_descargas, "Imagenes")
carpeta_documentos = os.path.join(carpeta_descargas, "Documentos")
carpeta_videos = os.path.join(carpeta_descargas, "Videos")

# Lista de extensiones de archivos para cada categoria
extensiones_imagenes = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
extensiones_documentos = [".pdf", ".doc", ".doctx", ".txt", ".docx", ".pptx"]
extensiones_videos = [".mp4", ".avi", ".mov", ".mkv"]

# 1. Crear las carpetas destino si no existen
if not os.path.exists(carpeta_imagenes):
	os.makedirs(carpeta_imagenes)
	
if not os.path.exists(carpeta_documentos):
	os.makedirs(carpeta_documentos)
	
if not os.path.exists(carpeta_videos):
	os.makedirs(carpeta_videos)
	
# 2. Recorrer todos los archivos en la carpeta de descargas
for nombre_archivos in os.listdir(carpeta_descargas):
	ruta_archivo = os.path.join(carpeta_descargas, nombre_archivos)
	
	#3. Verificar si es un archivo (no es una carpeta)
	if os.path.isfile(ruta_archivo):
		#4. Obtener la extension del archivo
		nombre_base, extension = os.path.splitext(nombre_archivos)
		extension = extension.lower() # Convertir a minusculas para comparar
		
		
		
		#5. Mover el archivo a la carpeta correspondiente segun su extension
		if extension in extensiones_imagenes:
			ruta_destino = os.path.join(carpeta_imagenes, nombre_archivos)
			shutil.move(ruta_archivo, ruta_destino)
			print(f"Movido: {nombre_archivos} a {carpeta_imagenes}")
			
		elif extension in extensiones_documentos:
			ruta_destino = os.path.join(carpeta_documentos, nombre_archivos)
			shutil.move(ruta_archivo, ruta_destino)
			print(f"Movido: {nombre_archivos} a {carpeta_documentos}")
			
		elif extension in extensiones_videos:
			ruta_destino = os.path.join(carpeta_videos, nombre_archivos)
			shutil.move(ruta_archivo, ruta_destino)
			print(f"Movido: {nombre_archivos} a {carpeta_videos}")
			# Se puede agregar un else para archivos no clasificados
			

print("Proceso de organizacion completo")
