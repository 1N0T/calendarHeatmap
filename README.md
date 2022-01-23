![logo](https://raw.github.com/1N0T/images/master/global/1N0T.png)

# Calendar HeatMap.

Se trata de una función a la que le pasaremos una lista con una serie de valores. Se presupone que cada valor representa el de un día determinado y, es requisito que incluya un valor para día consecutivo desde el día inicial.

El primer valor de la lista, se corresponderá con el del primer día del mes, pero no es necesario que sea el dl primer mes del año. Se puede comenzar desde cualquier mes (pero simepre desde el día 1 del mismo). En el caso de que no se pudiera cumplir esta condición, por no disponer de valores desde el principio de mes, se deberían insertar **numpy.nan** en la lista, para todos aquellos días desde el inicio para los que no se disponga de un valor.

Por otra parte, si no se disponen de valores hasta el final de un mes, no es necesario completarlos (esta circunstancia ya está controlada en la función). 

Puedes leer [aquí](https://dev.to/1n0t/matplotlib-heatmap-calendar-3kbo) una explicación, paso a paso, del enfoque adoptado.

### Dependencias.
La aplicación requiere la instalación de:
 * matplotlib.
 * numpy.
 
### Ejemplos de resultado.
Podemos mostrar calendario representando valores sólo con el mapa de colores. Pero adicionalmente, podemos añadir una etiqueta con el valor númerio representado y/o el día del mes al que se corresponde.


![img01](https://raw.github.com/1N0T/images/master/calendarHeatmap/opciones_visualizacion_datos_mes.png)

También es posible personalizar la paeta de colores, así como la cantidad de meses mostrados y, el numero de columnas en las que se representan.

![img01](https://raw.github.com/1N0T/images/master/calendarHeatmap/calendar_heatmap_purpura.png)

### Ejemplo de utilización
```python
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
    valores,                       # Lista de valores a representar en el calendario
    year,                          # Año al que corresponde elprimer valor
    meses=15,                      # Numero de meses que se quieren representar en el calendario
    mes_inicial=2,                 # Mes al que corresponde el primer valor (no es obligatorio empezar en enero)
    columnas=4,                    # Numero de meses a incluir en cada fila del calendario
    minimo = 0,                    # Valor inicial que representa el inicio de la escala de colores
    maximo = 400,                  # Valor final que representa el final de la escala de colores
    mostrar_valores=True,          # Además del código de color, se mostrará el valor numérico
    mostrar_dias=True,             # Se mostrará el día del mes en una esquina
    mostrar_escala_colores = True, # Mostramos la escala de colores
    zoom=1,                        # Número de veces que se quiere ampliar el tamaño de la imgen resultante
    paleta='Purples',              # Paleta de colores a utilizar (cualquier identificador válido de matplotlib)
    fichero='calendario.png'       # Nombre del fichero a crear. La extensión determinará el formato
)

```
### Historial de versiones.
| Versión | Descripción |
|---------|-------------|
| v1.0.1 | Añadida visualización de escala de colores y personalización rango de valores. |
| v1.0 | Versión inicial |