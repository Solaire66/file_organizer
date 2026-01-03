import os
import shutil
import pytest
# Asumiendo que tu script se llama organizador.py y está en src/
# O puedes extraer la lógica a una función para importarla

def organizar_archivos(directorio_base):
    # (Aquí deberías poner la lógica de tu script metida en una función)
    # Por ahora, simularemos la lógica mínima para el test
    carpetas = ["Imagenes", "Documentos", "Videos"]
    for c in carpetas:
        os.makedirs(os.path.join(directorio_base, c), exist_ok=True)
    
    for archivo in os.listdir(directorio_base):
        ruta = os.path.join(directorio_base, archivo)
        if os.path.isfile(ruta):
            ext = os.path.splitext(archivo)[1].lower()
            if ext in [".jpg", ".png"]:
                shutil.move(ruta, os.path.join(directorio_base, "Imagenes", archivo))
            elif ext in [".pdf", ".txt"]:
                shutil.move(ruta, os.path.join(directorio_base, "Documentos", archivo))

# TEST CON PYTEST
def test_organizacion_basica(tmp_path):
    # 1. Crear un directorio temporal de prueba
    d = tmp_path / "descargas"
    d.mkdir()
    
    # 2. Crear archivos de prueba
    foto = d / "vacaciones.jpg"
    foto.write_text("contenido falso")
    doc = d / "tarea.pdf"
    doc.write_text("contenido falso")
    
    # 3. Ejecutar la lógica de organización
    # Nota: Aquí llamamos a la función con la ruta temporal
    organizar_archivos(str(d))
    
    # 4. Verificaciones (Assertions)
    assert os.path.exists(str(d / "Imagenes" / "vacaciones.jpg"))
    assert os.path.exists(str(d / "Documentos" / "tarea.pdf"))
    assert not os.path.exists(str(d / "vacaciones.jpg")) # Ya no debe estar en la raíz
