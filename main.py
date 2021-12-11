import numpy as np
import calendar_heatmap as chm

# Generamos lista de valores aleatorios para los días que queremos
# representar en el calendario.
valores = np.random.randint(365, size=500)
year = 2021

# Función para generar imagen del calendario. Sólo los 2 primeros parámetros son obligatorios
# Los formatos de fichero soportados son:
# eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff

chm.calendar_heatmap(
    valores,                # Lista de valores a representar en el calendario
    year,                   # Año al que corresponde elprimer valor
    meses=15,               # Numero de meses que se quieren representar en el calendario
    mes_inicial=2,          # Mes al que corresponde el primer valor (no es obligatorio empezar en enero)
    columnas=4,             # Numero de meses a incluir en cada fila del calendario
    mostrar_valores=True,   # Además del código de color, se mostrará el valor numérico
    mostrar_dias=True,      # Se mostrará el día del mes en una esquina
    zoom=1,                 # Número de veces que se quiere ampliar el tamaño de la imgen resultante
    paleta='Purples',       # Paleta de colores a utilizar (cualquier identificador válido de matplotlib)
    fichero='hmap_cal.png'  # Nombre del fichero a crear. La extensión determinará el formato
)

