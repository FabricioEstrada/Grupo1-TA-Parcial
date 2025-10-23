import re
import pandas as pd

def read_sao(filepath):
    """
    Lee un archivo .SAO (ionosonda de Jicamarca o similar)
    y extrae variables principales: fecha, hora, foF2, hmF2, foEs, etc.
    Devuelve un DataFrame con los resultados.
    """
    pattern_time = re.compile(r"TIME\s*=\s*(\d{6})")
    pattern_date = re.compile(r"DATE\s*=\s*(\d{6})")
    pattern_foF2 = re.compile(r"foF2\s*=\s*([0-9.]+)")
    pattern_hmF2 = re.compile(r"hmF2\s*=\s*([0-9.]+)")
    pattern_foEs = re.compile(r"foEs\s*=\s*([0-9.]+)")
    pattern_hmE = re.compile(r"hmE\s*=\s*([0-9.]+)")

    records = []
    with open(filepath, "r", errors="ignore") as f:
        content = f.read()

    entries = content.split("IONOGRAM")
    for entry in entries:
        date = pattern_date.search(entry)
        time = pattern_time.search(entry)
        foF2 = pattern_foF2.search(entry)
        hmF2 = pattern_hmF2.search(entry)
        foEs = pattern_foEs.search(entry)
        hmE = pattern_hmE.search(entry)

        if date and time:
            records.append({
                "DATE": date.group(1),
                "TIME": time.group(1),
                "foF2": float(foF2.group(1)) if foF2 else None,
                "hmF2": float(hmF2.group(1)) if hmF2 else None,
                "foEs": float(foEs.group(1)) if foEs else None,
                "hmE": float(hmE.group(1)) if hmE else None,
            })

    df = pd.DataFrame(records)
    if not df.empty:
        df["DATETIME"] = pd.to_datetime(df["DATE"] + df["TIME"], format="%y%m%d%H%M%S", errors="coerce")
        df = df.dropna(subset=["DATETIME"])
        df = df.sort_values("DATETIME").reset_index(drop=True)

    return df

