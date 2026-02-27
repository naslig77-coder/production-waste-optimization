import pandas as pd
from pathlib import Path

# Paths
RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")
PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

files = [
    "desperdicios.csv",
    "pesos_se.csv",
    "instalaciones.csv",
    "nombre_maquina.csv"
]

for file in files:
    print(f"Procesando {file}...")

    df = pd.read_csv(
        RAW_PATH / file,
        sep=";",
        encoding="utf-8",
        low_memory=False
    )

    # Limpieza básica
    df.columns = df.columns.str.strip()
    df = df.drop_duplicates()

    output_file = PROCESSED_PATH / f"clean_{file}"
    df.to_csv(output_file, index=False)

    print(f"Guardado en {output_file}")

print("Transformación completada")