import calendar
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.transforms import BlendedGenericTransform

def calendar_heatmap (
        valores,
        year,
        dias_semana = ['Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa', 'Do'],
        nombres_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        minimo = None,
        maximo = None,
        mostrar_dias = True,
        mostrar_valores = True,
        mostrar_escala_colores = True,
        meses = 12,
        mes_inicial = 1,
        columnas = 4,
        zoom = 2,
        paleta = 'YlGn',
        fichero = "calendar_hearmap.pdf"
    ):

    escala = 3.5
    maximo_semanas_mes = 6

    # Calculamos el número de filas necesarias, para representar todos los meses indicados
    # en función del número de columnas deseado (meses por fila)
    if columnas > meses:
        columnas = meses 
    filas = int(math.ceil(meses / columnas))

    # Creamos los subplots necesarios para ocupar todas las filas/columnas del gráfico
    fig, ax = plt.subplots(filas, columnas, figsize=(escala*columnas*zoom, escala*filas*zoom))
    
    # Para facilitar la iteración, convertimos la matriz bidimensional de subplots, en una 
    # una matriz unidimensional
    axs = np.array(ax).reshape(-1)
    
    numero_valores = len(valores)
    if not minimo:
        minimo = 0
    if not maximo:  
        maximo = max(valores)

    puntero_dia_actual = 0
    hoja_calendario = 0

    # Comprobamos el rango de años que incluye a todos los meses a representar
    if mes_inicial + meses > 12 + 1:
        year_delta = (mes_inicial + meses) // 12
        years = str(year) + '-' + str(year + year_delta)
    else:
        years = year

    # Iteramos por cada uno de los meses. Permitimos la posibilidad de que el primer mes
    # no sea necesariamente enero. Podemos empezar en marzo p.ej.
    for mes in range(mes_inicial, mes_inicial + meses):

        # Controlamos a que año (desde el inicial) pertenece el mes en curso
        year_delta = mes // 12 
        mes = mes % 12 
        if mes == 0:
            mes = 12

        # Averiguamos cuantos días tien el mes actual y, el día de la semana en el que empieza
        dia_semana, dias_mes = calendar.monthrange(year + year_delta, mes)
        
        # Creamos una cuadrícula de valores vacíos para el mes en tratamiento
        plantilla_mes = np.empty((maximo_semanas_mes, len(dias_semana)))
        plantilla_mes[:] = np.nan

        # Colocamoos el nombre del més como título del subplot
        axs[hoja_calendario].set_title(nombres_meses[mes - 1]+'\n', fontsize=12*zoom)

        # Establecemos etiquetas de eje x (dias de la semana)
        axs[hoja_calendario].set_xticks(np.arange(len(dias_semana)))
        axs[hoja_calendario].set_xticklabels(dias_semana, fontsize=10*zoom, fontweight='bold', color='#555555')
        
        # Eliminamos etiquetas eje y
        axs[hoja_calendario].set_yticklabels([])

        # Mostraremos días de la semana en la parte superior
        axs[hoja_calendario].tick_params(axis=u'both', which=u'both', length=0)
        axs[hoja_calendario].xaxis.tick_top()

        # Dibujamos una cuadrícula para dar sensación de separación entre los días
        axs[hoja_calendario].set_xticks(np.arange(-.5, len(dias_semana), 1), minor=True)
        axs[hoja_calendario].set_yticks(np.arange(-.5, maximo_semanas_mes, 1), minor=True)
        axs[hoja_calendario].grid(which='minor', color='w', linestyle='-', linewidth=int(2*zoom))

        # Ocultamos las líneas que enmarcan el gráfico del mes
        for lado in ['left', 'right', 'bottom', 'top']:
            axs[hoja_calendario].spines[lado].set_visible(False)


        # Variables de control para saber en que casilla de la cuadrícula nos encontramos
        fila = 0
        columna = dia_semana

        # Recorremos los días del mes para ir recuperando secuencialmente los valores desde
        # la lista de valores recibida por parámetro.
        for n in range(dias_mes):
            if puntero_dia_actual < numero_valores:
                plantilla_mes[fila][columna] = valores[puntero_dia_actual]
                # Mostraremos el valor númerico si así se desea. Calculamos la posición en la que se tiene
                # que imprimir la etiqueta con el texto del mismo
                if mostrar_valores:
                    axs[hoja_calendario].text(
                        columna, fila+0.3, f"{valores[puntero_dia_actual]:0.0f}",
                        ha="center", va="center",
                        fontsize=7*zoom, color="w", alpha=0.8
                    )
                # Mostramos el día del mes si se ha solicitado. Calculamos la posición de la etiqueta    
                if mostrar_dias:
                    axs[hoja_calendario].text(
                        columna+0.2, fila-0.18, f"{n+1:0.0f}",
                        ha="center", va="center",
                        fontsize=6*zoom, color="#003333", alpha=0.8
                    )
                    # Calculamos donde colocar un círculo semitransparente, para resaltar el día
                    Drawing_colored_circle = plt.Circle(( columna+0.2 , fila-0.2 ), 0.2, fc='w', alpha=0.75)
                    axs[hoja_calendario].add_artist(Drawing_colored_circle)            

            # Controlamos donde estará el siguiente elemento de la lista y la posición en la cuadrícula
            # donde debe representarse.
            puntero_dia_actual += 1
            if columna == 6:
                columna = 0
                fila +=1
            else:
                columna += 1
        
        # Mostramos los valores usando el mapa de colores deseado
        axs[hoja_calendario].imshow(plantilla_mes, cmap=paleta, vmin=1, vmax=maximo)  # heatmap
        hoja_calendario += 1

    # En caso de que la cuadrícula del calendario no se rellene completamente, procesamos lo huecos
    # para generar un espacio en blanco
    for mes in range(meses, filas*columnas):
        axs[mes].tick_params(axis=u'both', which=u'both', length=0)
        axs[mes].set_xticklabels([])
        axs[mes].set_yticklabels([])

        for lado in ['left', 'right', 'bottom', 'top']:
            axs[mes].spines[lado].set_visible(False)

    # Mostramos como título el año, o los años a los que corresponden los datos
    fig.text(0.5, 0.95, "\n" + str(years) + "\n", fontsize=16*zoom, ha="center")

    # Creamos escala de colores y la mostramos, si así se ha solicitado
    if mostrar_escala_colores:
        # Cargamos mapa de colores recibido como parámetro
        mapa_de_colores = mpl.cm.get_cmap(paleta)

        # Creamos figura
        ax = fig.add_axes([0.05, 0.05, 0.90, 0.03])

        # Dibujamos equivalencia de la escala de colores
        cb = mpl.colorbar.ColorbarBase(
            ax, 
            orientation='horizontal', 
            cmap=mapa_de_colores,        
            norm=mpl.colors.Normalize(minimo, maximo)
        )

    # Salvamos la imagen del calendario.
    plt.savefig(fichero)
    


