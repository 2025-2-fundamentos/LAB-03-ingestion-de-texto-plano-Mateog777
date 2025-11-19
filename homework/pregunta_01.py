import pandas as pd
import re

def pregunta_01():
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    data_lines = lines[4:]
    registros = []
    actual = None

    patron = re.compile(
        r"^\s*(\d+)\s+(\d+)\s+([\d,]+)\s+%?\s+(.*)$"
    )

    for line in data_lines:
        if line.strip() == "":
            continue

        if line.lstrip()[0].isdigit():
            if actual is not None:
                registros.append(actual)

            m = patron.match(line)
            if not m:
                continue

            cluster = int(m.group(1))
            cantidad = int(m.group(2))
            porcentaje = float(m.group(3).replace(",", "."))
            palabras = m.group(4).strip()

            actual = {
                "cluster": cluster,
                "cantidad_de_palabras_clave": cantidad,
                "porcentaje_de_palabras_clave": porcentaje,
                "principales_palabras_clave": palabras,
            }
        else:
            texto = line.strip()
            actual["principales_palabras_clave"] += " " + texto

    if actual is not None:
        registros.append(actual)

    for r in registros:
        texto = " ".join(r["principales_palabras_clave"].split())
        texto = texto.replace(" ,", ",")
        texto = texto.rstrip(".")
        r["principales_palabras_clave"] = texto

    return pd.DataFrame(registros)
