import os
import gzip
import shutil
import requests

# Carpeta donde se guardarán los archivos
folder = "2014_september/"
os.makedirs(folder, exist_ok=True)

# URL base de Jicamarca, diciembre 2023
base = "https://lisn.igp.gob.pe/database/base/gps/LISN/laya/2014/09/scint/"

# Recorremos los días del 1 al 31
for day in range(1, 32):
    fname = f"laya_1409{day:02d}.s4.gz"       # Nombre del archivo comprimido
    url = base + fname
    gz_path = os.path.join(folder, fname)
    s4_path = gz_path.replace(".gz", "")      # nombre del archivo descomprimido

    # Descarga del archivo
    r = requests.get(url)
    if r.status_code == 200:
        with open(gz_path, "wb") as f:
            f.write(r.content)
        print("✅ Descargado:", fname)

        # Descompresión automática
        with gzip.open(gz_path, "rb") as f_in:
            with open(s4_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        print("📂 Descomprimido:", s4_path)

        # Opcional: eliminar el .gz
        os.remove(gz_path)
    else:
        print("❌ No encontrado:", fname)
