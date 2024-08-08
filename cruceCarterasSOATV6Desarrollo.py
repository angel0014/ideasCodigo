# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 20:09:41 2023

@author: ynorena
"""

import pandas as pd
import numpy as np
from datetime import datetime
import ast
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import tkinter.messagebox as tm
import os
from PIL import ImageTk, Image

# from helper import Helper

##### amparos #####

transporte = 'GASTOS DE TRANSPORTE Y MOVILIZACION DE VICTIMAS'
medico = 'GASTOS MEDICOS, QUIRURGICOS, FARMACEUTICOS Y HOSPI'

#####variable porcentual#####

porcentual = 0.009
porcentual_especial = 0.1

reajuste_iter_1 = (8,11,12)
reajuste_iter_2 = (211,212)#no iter


# ESTILO DE LOS BOTONES Y LAS ETIQUETAS

estilo_comenzar = {
    'bg': '#0099D7',
    'fg': 'black',
    'activebackground': 'orange',
    'activeforeground': 'black',
    'font': ('Abadi', 10, 'bold')
}

estilo_seleccionar = {
    'bg': '#F4E6A3',
    'fg': 'black',
    'activebackground': 'blue',
    'activeforeground': 'black',
    'font': ('Abadi', 10, 'bold')
}


estilo_checkbutton = {
    'bg': '#FFFFFF',
    'fg': 'red',
    'activebackground': 'blue',
    'activeforeground': 'red',
    'font': ('Abadi', 11, 'bold')
}

estilo_informacion = {
    'bg': '#F4E6A3',
    'fg': 'black',
    'activebackground': 'blue',
    'activeforeground': 'black',
    'font': ('Abadi', 11, 'bold')
}

estilo_etiquetas = {
    'bg': '#FFFFFF',
    'fg': 'black',
    'activebackground': 'blue',
    'activeforeground': 'black',
    'font': ('Abadi', 12, 'bold')
}

estilo_etiquetas_titulo = {
    'bg': '#FFFFFF',
    'fg': 'black',
    'activebackground': 'blue',
    'activeforeground': 'black',
    'font': ('Abadi', 15, 'bold')
}

# Helper.cronometro.iniciar()

def mostrar_informacion():
    tm.showinfo("Información", "'hoja_de_ruta': Para poder hacer el cruce es necesario que proporcione el NIT y la FACTURA en la HOJA DE RUTA. \n\n'Comenzar': Para poder hacer el cruce es necesario que proporcione el RADICADO en la HOJA DE RUTA.")

"cabeceras"
encabezados_liq = ['Numero_Radicado_Inicial', 'Fecha_Aviso', 'Reconsideracion',
       'Numero_de_factura', 'Observacion_servicio', 'Cantidad',
       'Valor_Servicio', 'Codigo_glosa_general_id',
       'Codigo_glosa_Especifica_id', 'Observacion_de_la_glosa',
       'Valor_Aprobado_Inicial', 'Valor_glosado_Inicial', 'Valor_Factura',
       'ValorAprobado', 'valorGlosaTotal', 'Centro_de_costo',
       'Codigo_de_servicio', 'NotaCredito']

encabezados_riq = ['detalleservicio_id', 'Numero_Radicado_Inicial',
       'NumeroRadicacion_RIQ_CIQ', 'NumeroFactura', 'Fecha_Aviso',
       'Reconsideracion', 'Observacion_servicio', 'Centro_de_costo',
       'Valor_Servicio', 'Cantidad', 'Codigo_glosa_general_id_RIQ',
       'Codigo_glosa_Especifica_id_RIQ', 'ObservacionGlosa', 'ValorGlosaTotal',
       'ValorAprobado', 'ValorAIPS', 'ValorSRTAIPS', 'ValorRatificado',
       'CodigoServicio']

encabezados_iq_riq = ['Numero_Radicado_Inicial2','Numero_Radicado_Inicial', 'Reconsideracion', 'Observacion_servicio', 'Cantidad',
       'Valor_Servicio', 'Codigo_glosa_general_id',
       'Codigo_glosa_Especifica_id', 'Observacion_de_la_glosa',
       'Valor_Aprobado_Inicial', 'Valor_glosado_Inicial', 'Valor_Factura','ValorAIPS', 'ValorSRTAIPS' ,'Centro_de_costo',
       'Codigo_de_servicio', 'NotaCredito']

encabezados_dev = ['Fechaproceso', 'NumeroRadicacion', 'TipoIdentificacionVictima',
        'NumeroIdentificacionVictima', 'PrimerNombreVictima',
        'SegundoNombreVictima', 'PrimerApellidoVictima',
        'SegundoApellidoVictima', 'NumeroFactura',
        'TipoIdentificacionReclamante', 'NumeroIdentificacionRec',
        'NombreReclamante', 'MotivoCausalDevolucionObjecion', 'TipoAmparo']
encabezados_not = ['NUMERO FACTURA', 'RADICADO', 'ID RECLAMANTE', 'RECLAMANTE', 'F.AVISO2',
        'CONSECUTIVO', 'GUIA', 'CORREO', 'F.NOTIFICACION']
encabezados_man = ['NumeroRadicacion']
encabezados_anu = ['NumeroRadicacion']

encabezados_liqMOK = ['Numero Radicacion', 'Numero Factura', 'Descripcion Servicio',
       'Cantidad Unidades Facturadas', 'Valor Facturado',
       'Codigo Especifico Glosa', 'Observaciones Glosa', 'Valor Autorizado',
       'Valor Glosado', 'Codigo Servicio', 'Origen']

encabezados_devMOK = ['Numero Radicacion', 'Tipo Identificacion Victima',
       'Numero Identificacion Victima', 'Nombres Victima', 'Apellidos Victima',
       'Numero Factura', 'Tipo Identificacion Reclamante',
       'Numero Identificacion Reclamante', 'Nombre Reclamante',
       'Causal Devolucion u Objecion', 'Amparo']

encabezados_notMOK = ['Numero Radicacion', 'Fecha de Notificación', 'Número de Guía',
       'Correo Electrónico', 'Consecutivo de la Comunicación', 'Observación']

# =============================================================================
# Declaracion rutas

# ruta2017_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2017\\"
# ruta2018_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2018\\"
# ruta2019_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2019\\"
# ruta2020_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2020\\"
# ruta2021_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2021\\"
# ruta2022_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2022\\"
# ruta2023_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2023\\"

# Servidor
ruta2017_exp = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data 2017"
ruta2018_exp = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data 2018"
ruta2019_exp = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data 2019"
ruta2020_exp = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data 2020"
ruta2021_exp = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data 2021"
ruta2022_exp = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data 2022"
ruta2023_exp = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data 2023"
ruta2024_exp = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data 2024"
ruta_nov_exp = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\condolidado_novedades_solucionadas"

# "Ruta aceptaciones totales y parciales línea interna"
ruta_acep_linea_interna_parcial = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\aceptaciones"
ruta_acep_total = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\aceptaciones\totales"


# # Local
# ruta2017_exp = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\3. Marzo\data_prueba\Data 2017\\"
# ruta2018_exp = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\3. Marzo\data_prueba\Data 2018\\"
# ruta2019_exp = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\3. Marzo\data_prueba\Data 2019\\"
# ruta2020_exp = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\3. Marzo\data_prueba\Data 2020\\"
# ruta2021_exp = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\3. Marzo\data_prueba\Data 2021\\"
# ruta2022_exp = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\3. Marzo\data_prueba\Data 2022\\"
# ruta2023_exp = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\3. Marzo\data_prueba\Data 2023\\"
# ruta2024_exp = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\5. Mayo\data_prueba\Data 2024\\"

# ruta_nov_exp = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\4. Abril\data_prueba\condolidado_novedades_solucionadas\\"

# #"Ruta aceptaciones totales y parciales línea interna"
# ruta_acep_linea_interna_parcial = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\4. Abril\data_prueba\aceptaciones\\"
# ruta_acep_total = r"C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\4. Abril\data_prueba\aceptaciones\totales\\"


# fin declaracion variables
# =============================================================================

# CARGAR CARTERA
def cargar_cartera():
    global df_cartera
    global boton_hoja_de_ruta
    global boton_comenzar
    
    tipos = (('Excel', '*.xlsx'), ('Texto plano', '*.txt *.csv'), ('Todos los archivos', '*'))
    archivo = fd.askopenfilename(title='Abrir archivo...', initialdir='/', filetypes=tipos)
    if archivo != '':
        try:
            archivo_extension = os.path.splitext(archivo)
            
            if archivo_extension[1] == '.csv':
                df_cartera = pd.read_csv(archivo, delimiter=';', header=0, low_memory=False,on_bad_lines='skip')
                
                #limpiar
                
                tm.showinfo("Carga completada", "Cartera cargada correctamente")
                
                # if df_hr_cartera.empty:
                #     boton_comenzar.config(state="disabled")
                # else:
                #     boton_comenzar.config(state="normal")
                    
            elif archivo_extension[1] == '.xlsx':
                df_cartera = pd.read_excel(archivo, header=0)
                
                #limpiar
                
                tm.showinfo("Carga completada", "Cartera cargada correctamente")
                
                # if df_hr_cartera.empty:
                #     boton_comenzar.config(state="disabled")
                # else:
                #     boton_comenzar.config(state="normal")
            else:
                tm.showwarning("Extension inválida", "El archivo ingresado tiene una extensión incorrecta. \nExtensiones válidas: '.xlsx'")
            
        except Exception as e:
            # Error durante la carga del archivo
            tm.showerror("Error de carga", str(e))
    else:
        tm.showwarning("Elija la Cartera", "Es necesario que elija la Cartera")

# CARGAR HR DE CARTERA
def cargar_hr():
    global df_hr_cartera
    global boton_hoja_de_ruta
    global boton_comenzar
    
    tipos = (('Texto plano', '*.txt *.csv'), ('Excel', '*.xlsx'), ('Todos los archivos', '*'))
    archivo = fd.askopenfilename(title='Abrir archivo...', initialdir='/', filetypes=tipos)
    if archivo != '':
        try:
            archivo_extension = os.path.splitext(archivo)
            
            if archivo_extension[1] == '.csv':
                df_hr_cartera = pd.read_csv(archivo, delimiter='|',encoding='ANSI', on_bad_lines="skip", decimal='.', header=0, low_memory=False)
                
                #limpiar
                
                tm.showinfo("Carga completada", "HOJA DE RUTA cargada correctamente")
                
                if df_hr_cartera.empty:
                    boton_comenzar.config(state="disabled")
                else:
                    boton_comenzar.config(state="normal")
                    
            elif archivo_extension[1] == '.txt':
                df_hr_cartera = pd.read_csv(archivo, delimiter='|', encoding='ANSI', on_bad_lines="skip", decimal='.', header=0, low_memory=False)
                
                #limpiar
                
                tm.showinfo("Carga completada", "HOJA DE RUTA cargada correctamente")
                
                if df_hr_cartera.empty:
                    boton_comenzar.config(state="disabled")
                else:
                    boton_comenzar.config(state="normal")
            else:
                tm.showwarning("Extension inválida", "El archivo ingresado tiene una extensión incorrecta. \nExtensiones válidas: '.csv'")
            
        except Exception as e:
            # Error durante la carga del archivo
            tm.showerror("Error de carga", str(e))
    else:
        tm.showwarning("Elija la HOJA DE RUTA", "Es necesario que elija la HOJA DE RUTA")
    #df_hr_cartera = pd.read_table(r"D:\Proyecto_Carteras\Herramienta\hr\HojaRuta_900615608.txt", sep="|", header=0, encoding="ANSI", on_bad_lines="skip", low_memory=False, decimal='.')

def eliminar_duplicados_y_resetear(df):
    """
    Elimina duplicados de un DataFrame que incluye columnas con listas,
    convierte las listas a cadenas para eliminar duplicados y luego las
    convierte de vuelta a listas. Finalmente, resetea el índice del DataFrame.

    Parámetros:
    - df: DataFrame de pandas a procesar.

    Retorna:
    - DataFrame procesado con duplicados eliminados y índice reseteado.
    """
    # Crear una copia del DataFrame original para no modificarlo directamente
    df_copia = df.copy()

    # Convertir las listas a cadenas para que sean hashables y poder eliminar duplicados
    df_copia['resultado_amparos_agru'] = df_copia['resultado_amparos_agru'].apply(lambda x: str(x) if isinstance(x, list) else x)

    # Eliminar duplicados en la copia
    df_copia = df_copia.drop_duplicates()

    # Convertir cadenas de vuelta a listas (solo las que fueron listas originalmente)
    df_copia['resultado_amparos_agru'] = df_copia['resultado_amparos_agru'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) and x.startswith('[') else x)

    # Resetear el índice en el DataFrame
    df_copia.reset_index(drop=True, inplace=True)

    return df_copia


#Cargue insumos data
#CARGUE 2017 IQ
def data_iq_2017():
    global ruta2017_exp
    global df_liq17
    global df_dev17
    global df_not17
    global df_riq17
    global df_man17
    global df_anu17
    
    # #ruta2017_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2017\\"
    # # df_liq17 = pd.read_csv(ruta2017_exp + 'PJ_DetalleLiquidacion_2017_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_dev17 = pd.read_csv(ruta2017_exp + 'PJ_ReporteObjecionDev_2017_pro.csv', sep='|',encoding='ANSI',header=0)#encoding='ANSI'
    # df_not17 = pd.read_csv(ruta2017_exp + 'PJ_Detallenotificacion_2017_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # # df_riq17 = pd.read_csv(ruta2017_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2017_pro.csv', sep='|')#encoding='ANSI'
    # df_man17 = pd.read_csv(ruta2017_exp + 'PJ_DetalleManual_2017_pro.csv', sep='|')#encoding='ANSI'
    # df_anu17 = pd.read_csv(ruta2017_exp + 'PJ_Anulados_2017_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # # df_liq17 = df_liq17[df_liq17['Valor_glosado_Inicial'] > 0]
    # # df_riq17 = df_riq17[(df_riq17['ValorAIPS'] + df_riq17['ValorSRTAIPS'] + df_riq17['ValorRatificado']) > 0]
    #==========================================================================
    df_dev17 = pd.read_parquet(ruta2017_exp + r'\PJ_ReporteObjecionDev_2017_pro.parquet')
    df_not17 = pd.read_parquet(ruta2017_exp + r'\PJ_Detallenotificacion_2017_pro.parquet')
    df_man17 = pd.read_parquet(ruta2017_exp + r'\PJ_DetalleManual_2017_pro.parquet')
    df_anu17 = pd.read_parquet(ruta2017_exp + r'\PJ_Anulados_2017_pro.parquet')
    #==========================================================================
    
    

#CARGUE 2018 IQ
def data_iq_2018():
    global ruta2018_exp
    global df_liq18
    global df_dev18
    global df_not18
    global df_riq18
    global df_man18
    global df_anu18
    
    # #ruta2018_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2018\\"
    # # df_liq18 = pd.read_csv(ruta2018_exp + 'PJ_DetalleLiquidacion_2018_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_dev18 = pd.read_csv(ruta2018_exp + 'PJ_ReporteObjecionDev_2018_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # df_not18 = pd.read_csv(ruta2018_exp + 'PJ_Detallenotificacion_2018_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # # df_riq18 = pd.read_csv(ruta2018_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2018_pro.csv', sep='|')#encoding='ANSI'
    # df_man18 = pd.read_csv(ruta2018_exp + 'PJ_DetalleManual_2018_pro.csv', sep='|')#encoding='ANSI'
    # df_anu18 = pd.read_csv(ruta2018_exp + 'PJ_Anulados_2018_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # # df_liq18 = df_liq18[df_liq18['Valor_glosado_Inicial'] > 0]
    # # df_riq18 = df_riq18[(df_riq18['ValorAIPS'] + df_riq18['ValorSRTAIPS'] + df_riq18['ValorRatificado']) > 0]
    #==========================================================================
    df_dev18 = pd.read_parquet(ruta2018_exp + r'\PJ_ReporteObjecionDev_2018_pro.parquet')
    df_not18 = pd.read_parquet(ruta2018_exp + r'\PJ_Detallenotificacion_2018_pro.parquet')
    df_man18 = pd.read_parquet(ruta2018_exp + r'\PJ_DetalleManual_2018_pro.parquet')
    df_anu18 = pd.read_parquet(ruta2018_exp + r'\PJ_Anulados_2018_pro.parquet')
    #==========================================================================
    


#CARGUE 2019 IQ
def data_iq_2019():
    global ruta2019_exp
    global df_liq19
    global df_dev19
    global df_not19
    global df_riq19
    global df_man19
    global df_anu19
    
    # #ruta2019_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2019\\"
    # # df_liq19 = pd.read_csv(ruta2019_exp + 'PJ_DetalleLiquidacion_2019_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_dev19 = pd.read_csv(ruta2019_exp + 'PJ_ReporteObjecionDev_2019_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # df_not19 = pd.read_csv(ruta2019_exp + 'PJ_Detallenotificacion_2019_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # # df_riq19 = pd.read_csv(ruta2019_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2019_pro.csv', sep='|')#encoding='ANSI'
    # df_man19 = pd.read_csv(ruta2019_exp + 'PJ_DetalleManual_2019_pro.csv', sep='|')#encoding='ANSI'
    # df_anu19 = pd.read_csv(ruta2019_exp + 'PJ_Anulados_2019_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # # df_liq19 = df_liq19[df_liq19['Valor_glosado_Inicial'] > 0]
    # # df_riq19 = df_riq19[(df_riq19['ValorAIPS'] + df_riq19['ValorSRTAIPS'] + df_riq19['ValorRatificado']) > 0]
    
    #==========================================================================
    df_dev19 = pd.read_parquet(ruta2019_exp + r'\PJ_ReporteObjecionDev_2019_pro.parquet')
    df_not19 = pd.read_parquet(ruta2019_exp + r'\PJ_Detallenotificacion_2019_pro.parquet')
    df_man19 = pd.read_parquet(ruta2019_exp + r'\PJ_DetalleManual_2019_pro.parquet')
    df_anu19 = pd.read_parquet(ruta2019_exp + r'\PJ_Anulados_2019_pro.parquet')
    #==========================================================================    
    
    

#CARGUE 2020 IQ
def data_iq_2020():
    global ruta2020_exp
    global df_liq20
    global df_dev20
    global df_not20
    global df_riq20
    global df_man20
    global df_anu20
    
    # #ruta2020_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2020\\"
    # # df_liq20 = pd.read_csv(ruta2020_exp + 'PJ_DetalleLiquidacion_2020_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_dev20 = pd.read_csv(ruta2020_exp + 'PJ_ReporteObjecionDev_2020_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # df_not20 = pd.read_csv(ruta2020_exp + 'PJ_Detallenotificacion_2020_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # # df_riq20 = pd.read_csv(ruta2020_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2020_pro.csv', sep='|')#encoding='ANSI'
    # df_man20 = pd.read_csv(ruta2020_exp + 'PJ_DetalleManual_2020_pro.csv', sep='|')#encoding='ANSI'
    # df_anu20 = pd.read_csv(ruta2020_exp + 'PJ_Anulados_2020_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # # df_liq20 = df_liq20[df_liq20['Valor_glosado_Inicial'] > 0]
    # # df_riq20 = df_riq20[(df_riq20['ValorAIPS'] + df_riq20['ValorSRTAIPS'] + df_riq20['ValorRatificado']) > 0]
    
    #==========================================================================
    df_dev20 = pd.read_parquet(ruta2020_exp + r'\PJ_ReporteObjecionDev_2020_pro.parquet')
    df_not20 = pd.read_parquet(ruta2020_exp + r'\PJ_Detallenotificacion_2020_pro.parquet')
    df_man20 = pd.read_parquet(ruta2020_exp + r'\PJ_DetalleManual_2020_pro.parquet')
    df_anu20 = pd.read_parquet(ruta2020_exp + r'\PJ_Anulados_2020_pro.parquet')
    #==========================================================================
       
    
    
#CARGUE 2021 IQ
def data_iq_2021():
    global ruta2021_exp
    global df_liq21
    global df_dev21
    global df_not21
    global df_riq21
    global df_man21
    global df_anu21
    
    # #ruta2021_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2021\\"
    # # df_liq21 = pd.read_csv(ruta2021_exp + 'PJ_DetalleLiquidacion_2021_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_dev21 = pd.read_csv(ruta2021_exp + 'PJ_ReporteObjecionDev_2021_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # df_not21 = pd.read_csv(ruta2021_exp + 'PJ_Detallenotificacion_2021_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # # df_riq21 = pd.read_csv(ruta2021_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2021_pro.csv', sep='|')#encoding='ANSI'
    # df_man21 = pd.read_csv(ruta2021_exp + 'PJ_DetalleManual_2021_pro.csv', sep='|')#encoding='ANSI'
    # df_anu21 = pd.read_csv(ruta2021_exp + 'PJ_Anulados_2021_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # # df_liq21 = df_liq21[df_liq21['Valor_glosado_Inicial'] > 0]
    # # df_riq21 = df_riq21[(df_riq21['ValorAIPS'] + df_riq21['ValorSRTAIPS'] + df_riq21['ValorRatificado']) > 0]
    
    #==========================================================================
    df_dev21 = pd.read_parquet(ruta2021_exp + r'\PJ_ReporteObjecionDev_2021_pro.parquet')
    df_not21 = pd.read_parquet(ruta2021_exp + r'\PJ_Detallenotificacion_2021_pro.parquet')
    df_man21 = pd.read_parquet(ruta2021_exp + r'\PJ_DetalleManual_2021_pro.parquet')
    df_anu21 = pd.read_parquet(ruta2021_exp + r'\PJ_Anulados_2021_pro.parquet')
    #==========================================================================
    
    

#CARGUE 2022 IQ
def data_iq_2022():
    global ruta2022_exp
    global df_liq22
    global df_dev22
    global df_not22
    global df_riq22
    global df_man22
    global df_anu22
    
    # #ruta2022_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2022\\"
    # # df_liq22 = pd.read_csv(ruta2022_exp + 'PJ_DetalleLiquidacion_2022_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_dev22 = pd.read_csv(ruta2022_exp + 'PJ_ReporteObjecionDev_2022_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # df_not22 = pd.read_csv(ruta2022_exp + 'PJ_Detallenotificacion_2022_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # # df_riq22 = pd.read_csv(ruta2022_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2022_pro.csv', sep='|')#encoding='ANSI'
    # df_man22 = pd.read_csv(ruta2022_exp + 'PJ_DetalleManual_2022_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # df_anu22 = pd.read_csv(ruta2022_exp + 'PJ_Anulados_2022_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # # df_liq22 = df_liq22[df_liq22['Valor_glosado_Inicial'] > 0]
    # # df_riq22 = df_riq22[(df_riq22['ValorAIPS'] + df_riq22['ValorSRTAIPS'] + df_riq22['ValorRatificado']) > 0]
    
    #==========================================================================
    df_dev22 = pd.read_parquet(ruta2022_exp + r'\PJ_ReporteObjecionDev_2022_pro.parquet')
    df_not22 = pd.read_parquet(ruta2022_exp + r'\PJ_Detallenotificacion_2022_pro.parquet')
    df_man22 = pd.read_parquet(ruta2022_exp + r'\PJ_DetalleManual_2022_pro.parquet')
    df_anu22 = pd.read_parquet(ruta2022_exp + r'\PJ_Anulados_2022_pro.parquet')
    #==========================================================================
    

    
#CARGUE 2023 IQ
def data_iq_2023():
    global ruta2023_exp
    global df_liq23
    global df_dev23
    global df_not23
    global df_riq23
    global df_man23
    global df_anu23
    
    # #ruta2023_exp = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_iq\Data historica PROCESADA\Data 2023\\"
    # # df_liq23 = pd.read_csv(ruta2023_exp + 'PJ_DetalleLiquidacion_2023_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_dev23 = pd.read_csv(ruta2023_exp + 'PJ_ReporteObjecionDev_2023_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # df_not23 = pd.read_csv(ruta2023_exp + 'PJ_Detallenotificacion_2023_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # # df_riq23 = pd.read_csv(ruta2023_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2023_pro.csv', sep='|')#encoding='ANSI'
    # df_man23 = pd.read_csv(ruta2023_exp + 'PJ_DetalleManual_2023_pro.csv', sep='|')#encoding='ANSI'
    # df_anu23 = pd.read_csv(ruta2023_exp + 'PJ_Anulados_2023_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # # df_liq23 = df_liq23[df_liq23['Valor_glosado_Inicial'] > 0]
    # # df_riq23 = df_riq23[(df_riq23['ValorAIPS'] + df_riq23['ValorSRTAIPS'] + df_riq23['ValorRatificado']) > 0]
    
    #==========================================================================
    df_dev23 = pd.read_parquet(ruta2023_exp + r'\PJ_ReporteObjecionDev_2023_pro.parquet')
    df_not23 = pd.read_parquet(ruta2023_exp + r'\PJ_Detallenotificacion_2023_pro.parquet')
    df_man23 = pd.read_parquet(ruta2023_exp + r'\PJ_DetalleManual_2023_pro.parquet')
    df_anu23 = pd.read_parquet(ruta2023_exp + r'\PJ_Anulados_2023_pro.parquet')
    #==========================================================================
    
    

#CARGUE 2024 IQ
def data_iq_2024():
    global ruta2024_exp
    global df_liq24
    global df_dev24
    global df_not24
    global df_riq24
    global df_man24
    global df_anu24
    
    # df_dev24 = pd.read_csv(ruta2024_exp + 'PJ_ReporteObjecionDev_2024_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # df_not24 = pd.read_csv(ruta2024_exp + 'PJ_Detallenotificacion_2024_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # df_man24 = pd.read_csv(ruta2024_exp + 'PJ_DetalleManual_2024_pro.csv', sep='|')#encoding='ANSI'
    # df_anu24 = pd.read_csv(ruta2024_exp + 'PJ_Anulados_2024_pro.csv', sep='|')#encoding='ANSI'
    
    #==========================================================================
    df_dev24 = pd.read_parquet(ruta2024_exp + r'\PJ_ReporteObjecionDev_2024_pro.parquet')
    df_not24 = pd.read_parquet(ruta2024_exp + r'\PJ_Detallenotificacion_2024_pro.parquet')
    df_man24 = pd.read_parquet(ruta2024_exp + r'\PJ_DetalleManual_2024_pro.parquet')
    df_anu24 = pd.read_parquet(ruta2024_exp + r'\PJ_Anulados_2024_pro.parquet')
    #==========================================================================
    
###################
## Liquidaciones ##
###################

def data_iq_2017_liq():
    
    global df_liq17
    global df_riq17
    global ruta2017_exp
    
    # df_liq17 = pd.read_csv(ruta2017_exp + 'PJ_DetalleLiquidacion_2017_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_riq17 = pd.read_csv(ruta2017_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2017_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # df_liq17 = df_liq17[df_liq17['Valor_glosado_Inicial'] > 0]
    # df_riq17 = df_riq17[(df_riq17['ValorAIPS'] + df_riq17['ValorSRTAIPS'] + df_riq17['ValorRatificado']) > 0]
    
    #==========================================================================
    df_liq17 = pd.read_parquet(ruta2017_exp + r'\PJ_DetalleLiquidacion_2017_pro.parquet')
    df_riq17 = pd.read_parquet(ruta2017_exp + r'\PJ_detalleLiquidacion_RIQ_CIQ_2017_pro.parquet')
    df_liq17 = df_liq17[df_liq17['Valor_glosado_Inicial'] > 0]
    df_riq17 = df_riq17[(df_riq17['ValorAIPS'] + df_riq17['ValorSRTAIPS'] + df_riq17['ValorRatificado']) > 0]
    #==========================================================================
    
    
def data_iq_2018_liq():
    
    global df_liq18
    global df_riq18
    global ruta2018_exp
    
    # df_liq18 = pd.read_csv(ruta2018_exp + 'PJ_DetalleLiquidacion_2018_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_riq18 = pd.read_csv(ruta2018_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2018_pro.csv', sep='|')#encoding='ANSI'
    # df_liq18 = df_liq18[df_liq18['Valor_glosado_Inicial'] > 0]
    # df_riq18 = df_riq18[(df_riq18['ValorAIPS'] + df_riq18['ValorSRTAIPS'] + df_riq18['ValorRatificado']) > 0]
    
    #==========================================================================
    df_liq18 = pd.read_parquet(ruta2018_exp + r'\PJ_DetalleLiquidacion_2018_pro.parquet')
    df_riq18 = pd.read_parquet(ruta2018_exp + r'\PJ_detalleLiquidacion_RIQ_CIQ_2018_pro.parquet')
    df_liq18 = df_liq18[df_liq18['Valor_glosado_Inicial'] > 0]
    df_riq18 = df_riq18[(df_riq18['ValorAIPS'] + df_riq18['ValorSRTAIPS'] + df_riq18['ValorRatificado']) > 0]
    #==========================================================================
  

def data_iq_2019_liq():
   
    global df_liq19
    global df_riq19
    global ruta2019_exp
    
    # df_liq19 = pd.read_csv(ruta2019_exp + 'PJ_DetalleLiquidacion_2019_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_riq19 = pd.read_csv(ruta2019_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2019_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # df_liq19 = df_liq19[df_liq19['Valor_glosado_Inicial'] > 0]
    # df_riq19 = df_riq19[(df_riq19['ValorAIPS'] + df_riq19['ValorSRTAIPS'] + df_riq19['ValorRatificado']) > 0]
    
    #==========================================================================
    df_liq19 = pd.read_parquet(ruta2019_exp + r'\PJ_DetalleLiquidacion_2019_pro.parquet')
    df_riq19 = pd.read_parquet(ruta2019_exp + r'\PJ_detalleLiquidacion_RIQ_CIQ_2019_pro.parquet')
    df_liq19 = df_liq19[df_liq19['Valor_glosado_Inicial'] > 0]
    df_riq19 = df_riq19[(df_riq19['ValorAIPS'] + df_riq19['ValorSRTAIPS'] + df_riq19['ValorRatificado']) > 0]
    #==========================================================================
  

def data_iq_2020_liq():
    
    global df_liq20
    global df_riq20
    global ruta2020_exp
    
    # df_liq20 = pd.read_csv(ruta2020_exp + 'PJ_DetalleLiquidacion_2020_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_riq20 = pd.read_csv(ruta2020_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2020_pro.csv', sep='|')#encoding='ANSI'
    # df_liq20 = df_liq20[df_liq20['Valor_glosado_Inicial'] > 0]
    # df_riq20 = df_riq20[(df_riq20['ValorAIPS'] + df_riq20['ValorSRTAIPS'] + df_riq20['ValorRatificado']) > 0]
    
    #==========================================================================
    df_liq20 = pd.read_parquet(ruta2020_exp + r'\PJ_DetalleLiquidacion_2020_pro.parquet')
    df_riq20 = pd.read_parquet(ruta2020_exp + r'\PJ_detalleLiquidacion_RIQ_CIQ_2020_pro.parquet')
    df_liq20 = df_liq20[df_liq20['Valor_glosado_Inicial'] > 0]
    df_riq20 = df_riq20[(df_riq20['ValorAIPS'] + df_riq20['ValorSRTAIPS'] + df_riq20['ValorRatificado']) > 0]
    #==========================================================================
  
    

def data_iq_2021_liq():
    global df_liq21
    global df_riq21
    global ruta2021_exp
    
    # df_liq21 = pd.read_csv(ruta2021_exp + 'PJ_DetalleLiquidacion_2021_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_riq21 = pd.read_csv(ruta2021_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2021_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # df_liq21 = df_liq21[df_liq21['Valor_glosado_Inicial'] > 0]
    # df_riq21 = df_riq21[(df_riq21['ValorAIPS'] + df_riq21['ValorSRTAIPS'] + df_riq21['ValorRatificado']) > 0]
    
    #==========================================================================
    df_liq21 = pd.read_parquet(ruta2021_exp + r'\PJ_DetalleLiquidacion_2021_pro.parquet')
    df_riq21 = pd.read_parquet(ruta2021_exp + r'\PJ_detalleLiquidacion_RIQ_CIQ_2021_pro.parquet')
    df_liq21 = df_liq21[df_liq21['Valor_glosado_Inicial'] > 0]
    df_riq21 = df_riq21[(df_riq21['ValorAIPS'] + df_riq21['ValorSRTAIPS'] + df_riq21['ValorRatificado']) > 0]
    #==========================================================================
  

def data_iq_2022_liq():
    global df_liq22
    global df_riq22
    global ruta2022_exp
    
    # df_liq22 = pd.read_csv(ruta2022_exp + 'PJ_DetalleLiquidacion_2022_pro.csv', sep='|',encoding='utf-8-SIG')#encoding='ANSI'
    # df_riq22 = pd.read_csv(ruta2022_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2022_pro.csv', sep='|')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # df_liq22 = df_liq22[df_liq22['Valor_glosado_Inicial'] > 0]
    # df_riq22 = df_riq22[(df_riq22['ValorAIPS'] + df_riq22['ValorSRTAIPS'] + df_riq22['ValorRatificado']) > 0]
    
    #==========================================================================
    df_liq22 = pd.read_parquet(ruta2022_exp + r'\PJ_DetalleLiquidacion_2022_pro.parquet')
    df_riq22 = pd.read_parquet(ruta2022_exp + r'\PJ_detalleLiquidacion_RIQ_CIQ_2022_pro.parquet')
    df_liq22 = df_liq22[df_liq22['Valor_glosado_Inicial'] > 0]
    df_riq22 = df_riq22[(df_riq22['ValorAIPS'] + df_riq22['ValorSRTAIPS'] + df_riq22['ValorRatificado']) > 0]
    #==========================================================================
  

def data_iq_2023_liq():
    global df_liq23
    global df_riq23
    global ruta2023_exp
    
    # df_liq23 = pd.read_csv(ruta2023_exp + 'PJ_DetalleLiquidacion_2023_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # # df_liq23.info()
    # # b = df_liq23.head(1000)
    # try:
    #     df_riq23 = pd.read_csv(ruta2023_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2023_pro.csv', sep='|')#encoding='ANSI'
    # except:
    #     df_riq23 = pd.read_csv(ruta2023_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2023_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    
    # df_liq23 = df_liq23[df_liq23['Valor_glosado_Inicial'] > 0]
    # df_riq23 = df_riq23[(df_riq23['ValorAIPS'] + df_riq23['ValorSRTAIPS'] + df_riq23['ValorRatificado']) > 0]
    
    #==========================================================================
    df_liq23 = pd.read_parquet(ruta2023_exp + r'\PJ_DetalleLiquidacion_2023_pro.parquet')
    df_riq23 = pd.read_parquet(ruta2023_exp + r'\PJ_detalleLiquidacion_RIQ_CIQ_2023_pro.parquet')
    df_liq23 = df_liq23[df_liq23['Valor_glosado_Inicial'] > 0]
    df_riq23 = df_riq23[(df_riq23['ValorAIPS'] + df_riq23['ValorSRTAIPS'] + df_riq23['ValorRatificado']) > 0]
    #==========================================================================
    

def data_iq_2024_liq():
    global df_liq24
    global df_riq24
    global ruta2024_exp
    
    # df_liq24 = pd.read_csv(ruta2024_exp + 'PJ_DetalleLiquidacion_2024_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # # df_liq23.info()
    # # b = df_liq23.head(1000)
    # try:
    #     df_riq24 = pd.read_csv(ruta2024_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2024_pro.csv', sep='|')#encoding='ANSI'
    # except:
    #     df_riq24 = pd.read_csv(ruta2024_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_2024_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    # #filtrar de liquidacion los valores glosados > 0
    # df_liq24 = df_liq24[df_liq24['Valor_glosado_Inicial'] > 0]
    # df_riq24 = df_riq24[(df_riq24['ValorAIPS'] + df_riq24['ValorSRTAIPS'] + df_riq24['ValorRatificado']) > 0]
    
    #==========================================================================
    df_liq24 = pd.read_parquet(ruta2024_exp + r'\PJ_DetalleLiquidacion_2024_pro.parquet')
    df_riq24 = pd.read_parquet(ruta2024_exp + r'\PJ_detalleLiquidacion_RIQ_CIQ_2024_pro.parquet')
    df_liq24 = df_liq24[df_liq24['Valor_glosado_Inicial'] > 0]
    df_riq24 = df_riq24[(df_riq24['ValorAIPS'] + df_riq24['ValorSRTAIPS'] + df_riq24['ValorRatificado']) > 0]
    #==========================================================================
 
####################
####  Novedades ####
####################   

def data_iq_nov_liq():
    
    global df_liq_nov
    global df_riq_nov
    global ruta_nov_exp
    
    # df_liq_nov = pd.read_csv(ruta_nov_exp + 'PJ_DetalleLiquidacion_nov_pro.csv', sep='|')#encoding='ANSI'
    # try:
    #     try:
    #         df_riq_nov = pd.read_csv(ruta_nov_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_nov_pro.csv', sep='|')#encoding='ANSI'
    #     except:
    #         df_riq_nov = pd.read_csv(ruta_nov_exp + 'PJ_detalleLiquidacion_RIQ_CIQ_nov_pro.csv', sep='|',encoding='ANSI')#encoding='ANSI'
    #     df_riq_nov = df_riq_nov[(df_riq_nov['ValorAIPS'] + df_riq_nov['ValorSRTAIPS'] + df_riq_nov['ValorRatificado']) > 0]        
    # except:
    #     df_riq_nov = pd.DataFrame(columns=encabezados_riq)
    
    # #filtrar de liquidacion los valores glosados > 0
    # df_liq_nov = df_liq_nov[df_liq_nov['Valor_glosado_Inicial'] > 0]
    
    # =========================================================================
    df_liq_nov = pd.read_parquet(ruta_nov_exp + r'\PJ_DetalleLiquidacion_nov_pro.parquet')

    try:
        
        df_riq_nov = pd.read_parquet(ruta_nov_exp + r'\PJ_detalleLiquidacion_RIQ_CIQ_nov_pro.parquet')
        
        df_riq_nov = df_riq_nov[(df_riq_nov['ValorAIPS'] + df_riq_nov['ValorSRTAIPS'] + df_riq_nov['ValorRatificado']) > 0]        
    except:
        df_riq_nov = pd.DataFrame(columns=encabezados_riq)
    
    # Filtrar de liquidacion los valores glosados > 0
    df_liq_nov = df_liq_nov[df_liq_nov['Valor_glosado_Inicial'] > 0]
    #==========================================================================
    
    
def data_iq_aceptaciones():
    
    global ruta2023_exp, ruta2024_exp, ruta_acep_linea_interna_parcial, ruta_acep_total
    global df_ace_p23, df_ace_p24, df_ace_total
    
    # df_ace_p23 = pd.read_csv(ruta2023_exp + 'PJ_Detalleaceptacion_2023_pro.csv', sep='|',encoding='ANSI')#aceptaciones parciales manuales
    # # df_ace_t23 = pd.read_csv(ruta2023_exp + 'PJ_Detalleaceptacion_2023_pro.csv', sep='|',encoding='utf-8-SIG')#aceptaciones totales manuales
    # df_ace_p24 = pd.read_csv(ruta2024_exp + 'PJ_Detalleaceptacion_2024_pro.csv', sep='|',encoding='ANSI')#aceptaciones parciales manuales
    
    # df_ace_linea_interna_parcial = pd.read_excel(ruta_acep_linea_interna_parcial + 'Consolidado_Conciliaciones_Liquidadas_LINEA INTERNA.xlsx', decimal=',')#aceptaciones parciales manuales
    # df_ace_linea_interna_total = pd.read_excel(ruta_acep_total + 'Consolidado_Aceptaciones_OD_ LINEA_INTERNA_TOTALES.xlsx')
    
    # df_ace_total = pd.read_excel(ruta_acep_total + 'aceptaciones_totales_IQ.xlsx')
    
    # =========================================================================
    df_ace_p23 = pd.read_parquet(ruta2023_exp + r'\PJ_Detalleaceptacion_2023_pro.parquet')
    df_ace_p24 = pd.read_parquet(ruta2024_exp + r'\PJ_Detalleaceptacion_2024_pro.parquet')  
    df_ace_linea_interna_parcial = pd.read_parquet(ruta_acep_linea_interna_parcial + r'\Consolidado_Conciliaciones_Liquidadas_LINEA INTERNA.parquet')
    
    df_ace_linea_interna_total = pd.read_parquet(ruta_acep_total + r'\Consolidado_Aceptaciones_OD_ LINEA_INTERNA_TOTALES.parquet')
    df_ace_total = pd.read_parquet(ruta_acep_total + r'\aceptaciones_totales_IQ.parquet')
    
    # df_ace_linea_interna_parcial = pd.read_excel(ruta_acep_linea_interna_parcial + 'Consolidado_Conciliaciones_Liquidadas_LINEA INTERNA.xlsx', decimal=',')  # aceptaciones parciales manuales
    # df_ace_linea_interna_total = pd.read_excel(ruta_acep_total + 'Consolidado_Aceptaciones_OD_LINEA_INTERNA_TOTALES.xlsx')

    # df_ace_total = pd.read_excel(ruta_acep_total + 'aceptaciones_totales_IQ.xlsx')
    
    # ==========================================================================

    
    # Convertir Floatdf_ace_p23
    df_ace_p23['VALOR INICIAL'] = df_ace_p23['VALOR INICIAL'].astype(float)
    df_ace_p23['VALOR ACEPTADO'] = df_ace_p23['VALOR ACEPTADO'].astype(float)
    df_ace_p23['VALOR PAGADO'] = df_ace_p23['VALOR PAGADO'].astype(float)
    df_ace_p23['VALOR NO ACORDADO'] = df_ace_p23['VALOR NO ACORDADO'].astype(float)  
    
    # Convertir Floatdf_ace_p24
    df_ace_p24['VALOR INICIAL'] = df_ace_p24['VALOR INICIAL'].astype(float)
    df_ace_p24['VALOR ACEPTADO'] = df_ace_p24['VALOR ACEPTADO'].astype(float)
    df_ace_p24['VALOR PAGADO'] = df_ace_p24['VALOR PAGADO'].astype(float)
    df_ace_p24['VALOR NO ACORDADO'] = df_ace_p24['VALOR NO ACORDADO'].astype(float) 


    # Transformacion df_ace_linea_interna_parcial
    df_ace_linea_interna_parcial['VALOR INICIAL'] = df_ace_linea_interna_parcial['VALOR INICIAL'].astype(float)
    df_ace_linea_interna_parcial['VALOR ACEPTADO'] = df_ace_linea_interna_parcial['VALOR ACEPTADO'].astype(float)
    df_ace_linea_interna_parcial['VALOR PAGADO'] = df_ace_linea_interna_parcial['VALOR PAGADO'].astype(float)
    df_ace_linea_interna_parcial['VALOR NO ACORDADO'] = df_ace_linea_interna_parcial['VALOR NO ACORDADO'].astype(float)
    
    df_ace_linea_interna_parcial = df_ace_linea_interna_parcial.loc[:,['NIT', 'FACTURA', 'FECHA DE CONCILIACION', 'VALOR INICIAL',
                                                                       'VALOR ACEPTADO', 'VALOR PAGADO', 'VALOR NO ACORDADO']]

    # Transformacion aceptaciones totales IQ Totales + OD LINEA INTERNA
    df_ace_total = df_ace_total.loc[:,['FACTURA IQ','Valor Aceptado Ips']]
    df_ace_linea_interna_total = df_ace_linea_interna_total.loc[:,['FACTURA IQ','Valor Aceptado Ips']]
    
    df_ace_linea_interna_total['Valor Aceptado Ips'] = df_ace_linea_interna_total['Valor Aceptado Ips'].astype(float)
    
    
    # Concatenar aceptaciones LI
    df_ace_p23 = pd.concat([df_ace_p23,df_ace_p24,df_ace_linea_interna_parcial])
    df_ace_p23.reset_index(drop=True, inplace=True)
    
    # Aceptaciones Totales
    df_ace_total = pd.concat([df_ace_linea_interna_total,df_ace_total]) # IQ Totales + OD LINEA INTERNA
    df_ace_total.reset_index(drop=True, inplace=True) 
    df_ace_total = df_ace_total.sort_values('Valor Aceptado Ips', ascending=False)
    df_ace_total = df_ace_total.drop_duplicates(subset='FACTURA IQ', keep='first') # ? Porque Hay duplicados ???
    
    # Resultado => df_ace_p23 y df_ace_total 
    #===========================================================================
  
    
    
def data_iq_maos():
    
    global ruta2023_exp,ruta2024_exp
    global df_mao_p23,df_mao_p24
    
    # try:
    #     df_mao_p23 = pd.read_csv(ruta2023_exp + 'PJ_MAOS_2023_pro.csv', sep='|')#,encoding='ANSI' maos
    # except:
    #     df_mao_p23 = pd.read_csv(ruta2023_exp + 'PJ_MAOS_2023_pro.csv', sep='|',encoding='ANSI')#,encoding='ANSI' maos
    # try:
    #     df_mao_p24 = pd.read_csv(ruta2024_exp + 'PJ_MAOS_2024_pro.csv', sep='|')#,encoding='ANSI' maos
    # except:
    #     df_mao_p24 = pd.read_csv(ruta2024_exp + 'PJ_MAOS_2024_pro.csv', sep='|',encoding='ANSI')#,encoding='ANSI' maos
        
    # df_mao_p23 = pd.concat([df_mao_p23,df_mao_p24])
    
    # =========================================================================
    
    df_mao_p23 = pd.read_parquet(ruta2023_exp + r'\PJ_MAOS_2023_pro.parquet')
   
    df_mao_p24 = pd.read_parquet(ruta2024_exp + r'\PJ_MAOS_2024_pro.parquet')
    
    # Concatenar los DataFrames de 2023 y 2024
    df_mao_p23 = pd.concat([df_mao_p23, df_mao_p24])
    df_mao_p23.reset_index(drop=True, inplace=True)
        
    # =========================================================================
  
    
"cargue DATA MOK"
#==============================================================================

def data_mok():
    
    global rutaMOK
    global df_liqMOK
    global df_devMOK
    global df_notMOK
    
    rutaMOK = r"\\IBM-FSBSRDEL\Gerencia_Siniestros_SOAT\data_mok\Entrega_Mundial_20220531_2\\"
    df_liqMOK = pd.read_csv(rutaMOK + 'MUN Detalle Liquidacion unificado.txt', sep='|')#encoding='ANSI'
    df_devMOK = pd.read_csv(rutaMOK + 'MUN Detalle Devoluciones - Objeciones.txt', sep='|')#encoding='ANSI'
    df_notMOK = pd.read_csv(rutaMOK + 'MUN Detalle Notificacion.txt', sep='|')#encoding='ANSI'

def data_juridico():
    
    global df_jur
    
    # df_jur = pd.read_excel(r'C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\4. Abril\data_prueba\Data juridico\juridico.xlsx')
    # df_jur = pd.read_excel(r'\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data juridico\juridico.xlsx')
    df_jur = pd.read_parquet(r'\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data juridico\juridico.parquet')
    # print(df_jur.info())
    
    
    df_jur = df_jur.loc[:,['NIT','FacturaProceso']]
    df_jur['FacturaProceso'] = df_jur['FacturaProceso'].astype(str).str.upper()
    df_jur['FacturaProceso'] = df_jur['FacturaProceso'].str.replace('[.,\\-#:;/_ ]', '', regex=True)
    
    df_jur['FacturaProceso'] = np.where(df_jur['FacturaProceso'].str.isnumeric , df_jur['FacturaProceso'].str.lstrip('+-0'), df_jur['FacturaProceso'])
    df_jur['NIT'] = df_jur['NIT'].astype(str)
    
    df_jur = df_jur.drop_duplicates()
    
def data_investigaciones():
    
    global df_inv

    # df_inv = pd.read_excel(r'C:\Users\angperilla\OneDrive - Mundial de Seguros S.A\Documentos\Angello\1. Proyectos\2. Cartera\Insumos\4. Abril\data_prueba\Data investigaciones\investigaciones.xlsx')
    # df_inv = pd.read_excel(r'\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data investigaciones\investigaciones.xlsx')
    df_inv = pd.read_parquet(r'\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Data investigaciones\investigaciones.parquet')    
    df_inv = df_inv.loc[:,['Placa','Id_lesionado','Resultado_inv','Consecutivo_inv','Fecha_asignacion','F.accidente']]
    
    # df_inv = df_inv.loc[:,['Placa','Id_lesionado','F.accidente','Resultado_inv','Consecutivo_inv','Fecha_asignacion']]
    
    df_inv['Placa'] = df_inv['Placa'].astype(str).str.upper()
    df_inv['Placa'] = df_inv['Placa'].str.replace('[.,\\-#:;/_ ]', '', regex=True)
    df_inv['Placa'] = np.where(df_inv['Placa'].str.isnumeric , df_inv['Placa'].str.lstrip('+-0'), df_inv['Placa'])
    
    df_inv['Id_lesionado'] = df_inv['Id_lesionado'].astype(str).fillna('-').replace('.0','', regex=True)
    df_inv['Id_lesionado'] = df_inv['Id_lesionado'].astype(str).str.upper()
    df_inv['Id_lesionado'] = df_inv['Id_lesionado'].str.replace('[.,\\-#:;/_ ]', '', regex=True)
    df_inv['Id_lesionado'] = np.where(df_inv['Id_lesionado'].str.isnumeric , df_inv['Id_lesionado'].str.lstrip('+-0'), df_inv['Id_lesionado'])
    
    
    ##==========================================================================
    ## Ajuste Investigaciones
    ##==========================================================================
    
    #--- Conversion Fechas ---
    
    df_inv['F.accidente'] = pd.to_datetime(df_inv['F.accidente'],format='%Y-%m-%d', errors='coerce')
    df_inv['Fecha_asignacion'] = pd.to_datetime(df_inv['Fecha_asignacion'],format='%Y-%m-%d', errors='coerce')
    # # Filtrar las filas donde 'F. accidente' es NaT (Not a Time)
    # df_error_fecha = df_inv[df_inv['F.accidente'].isna()]
    
    
    #--- Ordenar df ---
    
    # Define los valores a reemplazar en un diccionario
    replace_values = {'oNC': 'O.N.C', 'ONC': 'O.N.C', 'ONC ': 'O.N.C'}
    df_inv['Resultado_inv'] = df_inv['Resultado_inv'].replace(replace_values)
    
    # Define el orden personalizado
    custom_order = ['No cubierto', 'Cubierto', 'O.N.C']
    
    # Crea un diccionario que mapea cada valor a su índice en el orden personalizado
    order_dict = {value: i for i, value in enumerate(custom_order)}
    
    # Crea una nueva columna 'order' que contiene el índice de cada valor en el orden personalizado
    df_inv['order'] = df_inv['Resultado_inv'].map(order_dict)
    
    # Ordenar df
    df_inv = df_inv.sort_values(by=['order','F.accidente', 'Fecha_asignacion', 'Placa'], ascending=[True, False, False, True])
        
    
    #--- Eliminar columnas ---
    
    # Eliminar columna order
    df_inv = df_inv.drop(columns=['order'])
    
    # Eliminar duplicados por Placa y F.accidente
    df_inv = df_inv.drop_duplicates(['Placa','F.accidente'], keep='first')
    
    # # Crea una nueva columna 'key' que es la concatenación de 'Placa' y 'F.accidente'
    # # Convertir la columna 'F.accidente' a 'str'
    # df_inv['F.accidente'] = df_inv['F.accidente'].astype(str)
    # df_inv['key'] = df_inv['Placa'] + df_inv['F.accidente']
    # # Filtra los valores de 'key' que aparecen más de una vez en el DataFrame
    # duplicates = df_inv[df_inv.duplicated('key', keep=False)]
    
    ## df_inv = df_inv[df_inv['Resultado_inv']=='No cubierto']
    # df_inv.info()
    
    
    #===========================================================================
    # codigo Anterior Investigaciones
    # df_inv = df_inv.sort_values(['Placa','Id_lesionado','Fecha_asignacion'], ascending = False) 
    # df_inv = df_inv.drop_duplicates(['Placa','Id_lesionado'], keep='first')
    #===========================================================================
    
##******************************************************************************

# !!! 
"Cargue data"
# !!!
##*******************************************************************************

def cargar_data():
    global df_liq,df_liq17,df_liq18,df_liq19,df_liq20,df_liq21,df_liq22,df_liq23,df_liq24,df_liq_nov
    global df_dev,df_dev17,df_dev18,df_dev19,df_dev20,df_dev21,df_dev22,df_dev23,df_dev24
    global df_not,df_not17,df_not18,df_not19,df_not20,df_not21,df_not22,df_not23,df_not24
    global df_riq,df_riq17,df_riq18,df_riq19,df_riq20,df_riq21,df_riq22,df_riq23,df_riq24,df_riq_nov
    global df_man,df_man17,df_man18,df_man19,df_man20,df_man21,df_man22,df_man23,df_man24
    global df_anu,df_anu17,df_anu18,df_anu19,df_anu20,df_anu21,df_anu22,df_anu23,df_anu24
    
    global df_ace_p23, df_ace_total
    
    global df_mao_p23
    
    global df_liqMOK,df_devMOK,df_notMOK
    
    global df_hr_cartera, data_a_cargar_mok
    
    global df_liq_riq, df_liq_riq_agrupado, df_riq2, df_riq
    
    global encabezados_anu,encabezados_dev,encabezados_devMOK,encabezados_iq_riq,encabezados_liq,encabezados_liqMOK,encabezados_man,encabezados_not,encabezados_notMOK,encabezados_riq
    
    global df_jur, df_inv
    
    ######################
    ######################
    "CONCATENAR DATA"
    ######################
    ######################
    
    try:
        data_juridico()
    except:
        tm.showerror("Error cargue juridico**************")
        
    try:
        data_investigaciones()
    except:
        tm.showerror("Error cargue investigaciones**************")
    
    try:
        try:
            if data_a_cargar_iq_2017.get() == "activado":
                data_iq_2017_liq()
            else:
                df_liq17 = pd.DataFrame(columns=encabezados_liq)
                df_riq17 = pd.DataFrame(columns=encabezados_riq)
                # df_dev17 = pd.DataFrame(columns=encabezados_dev)
                # df_not17 = pd.DataFrame(columns=encabezados_not)
                # df_man17 = pd.DataFrame(columns=encabezados_man)
                # df_anu17 = pd.DataFrame(columns=encabezados_anu)
        except:
            tm.showerror("Error cargue 2017 liq**************")
            
        try:
            if data_a_cargar_iq_2018.get() == "activado":
                data_iq_2018_liq()
            else:
                df_liq18 = pd.DataFrame(columns=encabezados_liq)
                df_riq18 = pd.DataFrame(columns=encabezados_riq)
                # df_dev18 = pd.DataFrame(columns=encabezados_dev)
                # df_not18 = pd.DataFrame(columns=encabezados_not)
                # df_man18 = pd.DataFrame(columns=encabezados_man)
                # df_anu18 = pd.DataFrame(columns=encabezados_anu)
        except:
           tm.showerror("Error cargue 2018 liq**************")
        
        try:
            if data_a_cargar_iq_2019.get() == "activado":
                data_iq_2019_liq()
            else:
                df_liq19 = pd.DataFrame(columns=encabezados_liq)
                df_riq19 = pd.DataFrame(columns=encabezados_riq)
                # df_dev19 = pd.DataFrame(columns=encabezados_dev)
                # df_not19 = pd.DataFrame(columns=encabezados_not)
                # df_man19 = pd.DataFrame(columns=encabezados_man)
                # df_anu19 = pd.DataFrame(columns=encabezados_anu)
        except:
            tm.showerror("Error cargue 2019 liq**************")
        
        try:
            if data_a_cargar_iq_2020.get() == "activado":
                data_iq_2020_liq()
            else:
                df_liq20 = pd.DataFrame(columns=encabezados_liq)
                df_riq20 = pd.DataFrame(columns=encabezados_riq)
                # df_dev20 = pd.DataFrame(columns=encabezados_dev)
                # df_not20 = pd.DataFrame(columns=encabezados_not)
                # df_man20 = pd.DataFrame(columns=encabezados_man)
                # df_anu20 = pd.DataFrame(columns=encabezados_anu)
        except:
            tm.showerror("Error cargue 2020 liq**************")
        
        try:
            if data_a_cargar_iq_2021.get() == "activado":
                data_iq_2021_liq()
            else:
                df_liq21 = pd.DataFrame(columns=encabezados_liq)
                df_riq21 = pd.DataFrame(columns=encabezados_riq)
                # df_dev21 = pd.DataFrame(columns=encabezados_dev)
                # df_not21 = pd.DataFrame(columns=encabezados_not)
                # df_man21 = pd.DataFrame(columns=encabezados_man)
                # df_anu21 = pd.DataFrame(columns=encabezados_anu)
        except:
            tm.showerror("Error cargue 2021 liq**************")
            
        try:
            if data_a_cargar_iq_2022.get() == "activado":
                data_iq_2022_liq()
            else:
                df_liq22 = pd.DataFrame(columns=encabezados_liq)
                df_riq22 = pd.DataFrame(columns=encabezados_riq)
                # df_dev22 = pd.DataFrame(columns=encabezados_dev)
                # df_not22 = pd.DataFrame(columns=encabezados_not)
                # df_man22 = pd.DataFrame(columns=encabezados_man)
                # df_anu22 = pd.DataFrame(columns=encabezados_anu)
        except:
            tm.showerror("Error cargue 2022 liq**************")
            
        try:
            if data_a_cargar_iq_2023.get() == "activado":
                data_iq_2023_liq()
            else:
                df_liq23 = pd.DataFrame(columns=encabezados_liq)
                df_riq23 = pd.DataFrame(columns=encabezados_riq)
                # df_dev23 = pd.DataFrame(columns=encabezados_dev)
                # df_not23 = pd.DataFrame(columns=encabezados_not)
                # df_man23 = pd.DataFrame(columns=encabezados_man)
                # df_anu23 = pd.DataFrame(columns=encabezados_anu)
        except:
            tm.showerror("Error cargue 2023 liq**************")
            
        try:
            if data_a_cargar_iq_2024.get() == "activado":
                data_iq_2024_liq()
            else:
                df_liq24 = pd.DataFrame(columns=encabezados_liq)
                df_riq24 = pd.DataFrame(columns=encabezados_riq)
                # df_dev24 = pd.DataFrame(columns=encabezados_dev)
                # df_not24 = pd.DataFrame(columns=encabezados_not)
                # df_man24 = pd.DataFrame(columns=encabezados_man)
                # df_anu24 = pd.DataFrame(columns=encabezados_anu)
        except:
            tm.showerror("Error cargue 2024 liq**************")
            
        try:    
            if data_a_cargar_mok.get() == "activado":
                data_mok()
            else:
                df_liqMOK = pd.DataFrame(columns=encabezados_liqMOK)
                df_devMOK = pd.DataFrame(columns=encabezados_devMOK)
                df_notMOK = pd.DataFrame(columns=encabezados_notMOK)
        except:
            tm.showerror("Error cargue data mok**************")
            
        try:
            "Cargue data funciones"
            data_iq_nov_liq()
            
            data_iq_2017()
            data_iq_2018()
            data_iq_2019()
            data_iq_2020()
            data_iq_2021()
            data_iq_2022()
            data_iq_2023()
            data_iq_2024()
        except:
            tm.showerror("Error al tratar de cargar data general")
        try:
            data_iq_aceptaciones()
        except:
            tm.showerror("Error al tratar de cargar aceptaciones")
        try:
            data_iq_maos()
        except:
            tm.showerror("Error al tratar de cargar maos")  
        
    except:
        tm.showerror("No se tiene conexión a la FTP. Intente conectarse a Citrix e inténtelo nuevamente...")
    ######################
    ######################
    "AJUSTAR DATA"
    ######################
    ######################
    try:
        df_liq = pd.concat([df_liq17,df_liq18,df_liq19,df_liq20,df_liq21,df_liq22,df_liq23,df_liq24,df_liq_nov])
    except:
        tm.showerror("Error al tratar de unificar los datos de la data liquidacion")
    try:    
        df_dev = pd.concat([df_dev17,df_dev18,df_dev19,df_dev20,df_dev21,df_dev22,df_dev23,df_dev24])
    except:
        tm.showerror("Error al tratar de unificar los datos de la data devolucion")
    try:
        df_not = pd.concat([df_not17,df_not18,df_not19,df_not20,df_not21,df_not22,df_not23,df_not24])
    except:
        tm.showerror("Error al tratar de unificar los datos de la data notificacion")
    try:
        df_riq = pd.concat([df_riq17,df_riq18,df_riq19,df_riq20,df_riq21,df_riq22,df_riq23,df_riq24,df_riq_nov])
    except:
        tm.showerror("Error al tratar de unificar los datos de la data liquidacion riq")
    try:
        df_man = pd.concat([df_man17,df_man18,df_man19,df_man20,df_man21,df_man22,df_man23,df_man24])
    except:
        tm.showerror("Error al tratar de unificar los datos de la data manuales")
    try:
        df_anu = pd.concat([df_anu17,df_anu18,df_anu19,df_anu20,df_anu21,df_anu22,df_anu23,df_anu24])
    except:
        tm.showerror("Error al tratar de unificar los datos de la data anulados")
    
    
    df_dev = df_dev.loc[:,['NumeroRadicacion','MotivoCausalDevolucionObjecion']]
    df_not = df_not.loc[:,['RADICADO','CONSECUTIVO', 'GUIA', 'CORREO', 'F.NOTIFICACION']]
    df_not = df_not.drop_duplicates()
    
    ######################
    ######################
    "LIMPIAR DF DE DATA"
    ######################
    ######################
    df_liq17 = ''
    df_dev17 = ''
    df_not17 = ''
    df_riq17 = ''
    df_man17 = ''
    df_anu17 = ''
    
    df_liq18 = ''
    df_dev18 = ''
    df_not18 = ''
    df_riq18 = ''
    df_man18 = ''
    df_anu18 = ''
    
    df_liq19 = ''
    df_dev19 = ''
    df_not19 = ''
    df_riq19 = ''
    df_man19 = ''
    df_anu19 = ''
    
    df_liq20 = ''
    df_dev20 = ''
    df_not20 = ''
    df_riq20 = ''
    df_man20 = ''
    df_anu20 = ''
    
    df_liq21 = ''
    df_dev21 = ''
    df_not21 = ''
    df_riq21 = ''
    df_man21 = ''
    df_anu21 = ''
    
    df_liq22 = ''
    df_dev22 = ''
    df_not22 = ''
    df_riq22 = ''
    df_man22 = ''
    df_anu22 = ''
    
    df_liq23 = ''
    df_dev23 = ''
    df_not23 = ''
    df_riq23 = ''
    df_man23 = ''
    df_anu23 = ''
    
    df_liq24 = ''
    df_dev24 = ''
    df_not24 = ''
    df_riq24 = ''
    df_man24 = ''
    df_anu24 = ''
    
    df_liq_nov = ''
    df_riq_nov = ''
    
    ######################
    ######################
    "AJUSTE LIQUIDACION IQ-CIQ-RIQ DATA"
    ######################
    ######################
    
    #Se crean los campos en liq
    df_liq['ValorAIPS'] = 0
    df_liq['ValorSRTAIPS'] = 0
    df_liq['ValorRatificado'] = 0
    df_liq['Numero_Radicado_Inicial2'] = ''
    
    #Se renombran los campos de riq
    df_riq2 = df_riq.rename(columns={#'Numero_Radicado_Inicial':'Numero_Radicado_Inicial2',
                                   'NumeroRadicacion_RIQ_CIQ':'Numero_Radicado_Inicial2',
                                   'Codigo_glosa_general_id_RIQ':'Codigo_glosa_general_id',
                                   'Codigo_glosa_Especifica_id_RIQ':'Codigo_glosa_Especifica_id',
                                   'ObservacionGlosa':'Observacion_de_la_glosa',
                                   'ValorGlosaTotal':'Valor_Factura',
                                   'ValorAprobado':'Valor_Aprobado_Inicial',
                                   'CodigoServicio':'Codigo_de_servicio'})
    
    df_riq = df_riq.rename(columns={'Numero_Radicado_Inicial':'Numero_Radicado_Inicial2',
                                   'NumeroRadicacion_RIQ_CIQ':'Numero_Radicado_Inicial',
                                   'Codigo_glosa_general_id_RIQ':'Codigo_glosa_general_id',
                                   'Codigo_glosa_Especifica_id_RIQ':'Codigo_glosa_Especifica_id',
                                   'ObservacionGlosa':'Observacion_de_la_glosa',
                                   'ValorGlosaTotal':'Valor_Factura',
                                   'ValorAprobado':'Valor_Aprobado_Inicial',
                                   'CodigoServicio':'Codigo_de_servicio'})
    
    #Se crean los campos en riq
    df_riq['NotaCredito'] = ''
    df_riq['Valor_glosado_Inicial'] = df_riq['ValorRatificado']
    #Se establecen las cabeceras de los campos
    df_liq = df_liq.loc[:,encabezados_iq_riq]
    df_riq = df_riq.loc[:,encabezados_iq_riq]
    
    df_riq2['NotaCredito'] = ''
    df_riq2['Valor_glosado_Inicial'] = df_riq2['ValorRatificado']
    #Se establecen las cabeceras de los campos
    df_riq2 = df_riq2.loc[:,encabezados_iq_riq]
    #se unen las dos tablas de liquidacion
    df_liq_riq = pd.concat([df_liq,df_riq])
    
    #Se renombran las columnas de mok liquidacion
    df_liqMOK = df_liqMOK.rename(columns={'Numero Radicacion':'Numero_Radicado_Inicial',
                                          'Descripcion Servicio':'Observacion_servicio',
                                          'Cantidad Unidades Facturadas':'Cantidad',
                                          'Valor Facturado':'Valor_Servicio',
                                          'Codigo Especifico Glosa':'Codigo_glosa_general_id',
                                          'Observaciones Glosa':'Observacion_de_la_glosa',
                                          'Valor Autorizado':'Valor_Aprobado_Inicial',
                                          'Valor Glosado':'Valor_glosado_Inicial',
                                          'Codigo Servicio':'Codigo_de_servicio',
                                          'Origen':'Centro_de_costo'})
    
    #Se crean las columnas de mok liquidacion
    df_liqMOK['Reconsideracion'] = ''
    df_liqMOK['Codigo_glosa_Especifica_id'] = ''
    df_liqMOK['Valor_Factura'] = 0
    df_liqMOK['ValorAIPS'] = 0 ## Colocar este valor procedente de la data
    df_liqMOK['ValorSRTAIPS'] = 0
    df_liqMOK['ValorRatificado'] = 0
    df_liqMOK['NotaCredito'] = ''
    df_liqMOK['Numero_Radicado_Inicial2'] = ''
    
    #Se seleccionan las columnas
    df_liqMOK = df_liqMOK.loc[:,encabezados_iq_riq]
    df_liqMOK['Codigo_glosa_general_id'] = df_liqMOK['Codigo_glosa_general_id'].fillna(0)
    
    #devoluciones mok
    df_devMOK = df_devMOK.rename(columns={'Numero Radicacion':'NumeroRadicacion',
                                          'Causal Devolucion u Objecion':'MotivoCausalDevolucionObjecion'})
    
    df_devMOK = df_devMOK.loc[:,['NumeroRadicacion','MotivoCausalDevolucionObjecion']]
    
    #notificaciones mok
    df_notMOK = df_notMOK.rename(columns={'Numero Radicacion':'RADICADO',
                                          'Fecha de Notificación':'F.NOTIFICACION',
                                          'Número de Guía':'GUIA',
                                          'Correo Electrónico':'CORREO',
                                          'Consecutivo de la Comunicación':'CONSECUTIVO'})
    
    df_notMOK = df_notMOK.loc[:,['RADICADO', 'CONSECUTIVO', 'GUIA', 'CORREO', 'F.NOTIFICACION']]
    
    "Se concatena la data de mok y la de iq con la estructura ajustada"
    df_liq_riq = pd.concat([df_liq_riq,df_liqMOK])
    df_dev = pd.concat([df_dev,df_devMOK])
    df_not = pd.concat([df_not,df_notMOK])
    
    df_dev = df_dev.drop_duplicates('NumeroRadicacion', keep='first')
    
    
    #==================
    # df_liq = ''
    #=================
    df_riq = ''
        
    ######################
    ######################
    "FIN DATA"
    ######################
    ######################
    # Helper.cronometro.finalizar()
    
    tm.showinfo("Carga completada", "Data cargada correctamente")
    
##******************************************************************************
"Cruce cartera"
##******************************************************************************

def cruce_cartera():
    global df_liq,df_liq17,df_liq18,df_liq19,df_liq20,df_liq21,df_liq22,df_liq23
    global df_dev,df_dev17,df_dev18,df_dev19,df_dev20,df_dev21,df_dev22,df_dev23
    global df_not,df_not17,df_not18,df_not19,df_not20,df_not21,df_not22,df_not23
    global df_riq,df_riq17,df_riq18,df_riq19,df_riq20,df_riq21,df_riq22,df_riq23
    global df_man,df_man17,df_man18,df_man19,df_man20,df_man21,df_man22,df_man23
    global df_anu,df_anu17,df_anu18,df_anu19,df_anu20,df_anu21,df_anu22,df_anu23
    
    global df_ace_p23, df_ace_total
    
    global df_mao_p23
    
    global df_liqMOK,df_devMOK,df_notMOK
    
    global df_hr_cartera, data_a_cargar_mok, df_cartera
    
    global df_liq_riq, df_liq_riq_agrupado, df_riq2, df_riq
    
    global df_jur, df_inv
    
    # Helper.cronometro.iniciar()
    
    #############################*****************************************************JUDICIAL FLAG
    #############################*****************************************************JUDICIAL FLAG
    #############################*****************************************************JUDICIAL FLAG
    
    if cartera_judicial.get() == "activado":
        cartera_judicial_activa = True
    else:
        cartera_judicial_activa = False
    
    #############################*****************************************************JUDICIAL FLAG
    #############################*****************************************************JUDICIAL FLAG
    #############################*****************************************************JUDICIAL FLAG
    # !!! 
    try: #1
        ######################
        ######################
        "CODIGOS DE GLOSA IQ"
        ######################
        ######################
        try:
            #maos_IQ = ()#Depende de la glosa aplicada por el auditor, ya sea facturación, tarifas, soportes, ETC.
            facturacion_IQ = (0,1,4)
            tarifas_IQ = 2
            soportes_IQ = 3
            cobertura_IQ = 5
            pertinencia_IQ = 6
            habilitacion_IQ = (8,9)
            
            ######################
            ######################
            "CODIGOS DE GLOSA MOK"
            ######################
            ######################
            maos_MOK = 1063
            facturacion_MOK = 2061
            tarifas_MOK = (1113,281)
            soportes_MOK = 3321
            cobertura_MOK = 1121
            pertinencia_MOK = (1271,6041,6031,1261,221,0)#se agrega todo lo demas que no este en estas variables como pertinencia
            habilitacion_MOK = 9421
            
        except Exception as e:
            tm.showerror('Error en codigos de obj:', str(e))
        
        "lista de estados error de HR"
        lista_estadosHR_err = (
                           'ERROR EN RADICACION',
                           'ERROR EN RADICACION-AUDITADO SIN FINALIZAR PROCESO',
                           'ERROR EN RADICACION-EN PROCESO DE AUDITORIA',
                           'ERROR EN RADICACION-LIQUIDADO CON PAGO',
                           'ERROR EN RADICACION-LIQUIDADO SIN PAGO',
                           'GLOSA DE MOVIMIENTO POR ERROR ADMINISTRATIVO IQ',
                           'GLOSA DE MOVIMIENTO POR ERROR ADMINISTRATIVO IQ-AU',
                           'GLOSA DE MOVIMIENTO POR ERROR ADMINISTRATIVO IQ-EN',
                           'GLOSA DE MOVIMIENTO POR ERROR ADMINISTRATIVO IQ-LI',
                           'GLOSAR MOVIMIENTO-LIQUIDADO SIN PAGO',
                           'REGISTRO DUPLICADO',
                           'REGISTRO DUPLICADO-AUDITADO SIN FINALIZAR PROCESO',
                           'REGISTRO DUPLICADO-LIQUIDADO SIN PAGO')

        "lista de estados proceso de HR"
        lista_estadosHR_proceso = (
                           'AUDITADO SIN FINALIZAR PROCESO',
                           'EN PROCESO DE AUDITORIA',
                           'FACTURA SIN ASOCIAR A SINIESTRO',
                           'GLOSA SIN ASOCIAR A SINIESTROS',
                           'SIN ASIGNAR A SINIESTRO FACTURA LIQUIDADA EN CONCI')
        #seccion de pruebas
        # !!!
        # !!!
        # cargar_cartera()
        # cargar_hr()
        # # #!!!
        # !!!
        
        "Se crea campo para validar si el registro es un error de hr"
        df_hr_cartera['estadoError'] = df_hr_cartera[['ESTADO ACTUAL FACTURA']].apply(lambda x: 's' if x['ESTADO ACTUAL FACTURA'] in lista_estadosHR_err else 'n', axis=1)
        
        df_hr_cartera['FACTURA_2'] = df_hr_cartera['NUMERO FACTURA']
        # tm.showinfo("p1", "")
        try:
            "Limpieza factura de cartera"
            df_cartera['FACTURA'] = df_cartera['FACTURA'].astype(str).str.upper()
            
            df_cartera['FACTURA'] = df_cartera['FACTURA'].str.replace('[.,\\-#:;/_ ]', '', regex=True)
            
            df_cartera['FACTURA'] = np.where(df_cartera['FACTURA'].str.isnumeric , df_cartera['FACTURA'].str.lstrip('+-0'), df_cartera['FACTURA'])
            df_cartera['NIT'] = df_cartera['NIT'].astype(str)
            # tm.showinfo("Cruce completado", "df cartera")
           
            "Limpieza factura de hr"
            df_hr_cartera['NUMERO FACTURA'] = df_hr_cartera['NUMERO FACTURA'].astype(str).str.upper()
            df_hr_cartera['NUMERO FACTURA'] = df_hr_cartera['NUMERO FACTURA'].str.replace('[.,\\-#:;/_ ]', '', regex=True)
            
            df_hr_cartera['NUMERO FACTURA'] = np.where(df_hr_cartera['NUMERO FACTURA'].str.isnumeric , df_hr_cartera['NUMERO FACTURA'].str.lstrip('+-0'), df_hr_cartera['NUMERO FACTURA'])
            df_hr_cartera['ID RECLAMANTE'] = df_hr_cartera['ID RECLAMANTE'].astype(str)
            
            
            "Convertir formato de fechas de HR"
            df_hr_cartera['F.AVISO'] = pd.to_datetime(df_hr_cartera['F.AVISO'], format='%Y/%m/%d', errors='raise')
            df_hr_cartera['F.LIQUIDACION'] = pd.to_datetime(df_hr_cartera['F.LIQUIDACION'], format='%Y/%m/%d', errors='raise')
            df_hr_cartera['F.CREA FACTURA'] = pd.to_datetime(df_hr_cartera['F.CREA FACTURA'], format='%Y/%m/%d', errors='raise')
       
        except Exception as e:
             tm.showerror("Error limpieza hr y cartera:", str(e))
        try:
            "Se reemplaza los nulos por 0"
            df_hr_cartera['VLR RADICACION'] = df_hr_cartera['VLR RADICACION'].fillna(0)
            df_hr_cartera['VLR APROBADO'] = df_hr_cartera['VLR APROBADO'].fillna(0)
            df_hr_cartera['VLR GLOSADO'] = df_hr_cartera['VLR GLOSADO'].fillna(0)
            
            "Ordenar la hr de mas antigua a reciente"
            df_hr_cartera = df_hr_cartera.sort_values(by=['ID RECLAMANTE','NUMERO FACTURA','F.AVISO'], ascending=True)
            
            "se cruza la cartera contra la hr"
            cruce = pd.merge(df_cartera, df_hr_cartera, left_on=['NIT','FACTURA'], right_on=['ID RECLAMANTE','NUMERO FACTURA'], how='left')
            
            "Se realiza el conteo de 'DUPLICADOS' en hr, para poder evaluar el saldo correspondiente contra el movimiento de la hr"
            cruce['count'] = np.arange(1,len(cruce)+1)
            # a = len(cruce)
            cruce['recuentoFacturaHR'] = ''
            j = 0
            x = 1
            for x in range(len(cruce)):
                if cruce['count'].iloc[x:x+1].values[0] == 1: # Fila 2: Si el valor de la columna 'count' para la fila 2 ==>Reultado:  2
                    cruce['recuentoFacturaHR'].iloc[x:x+1] = 1        
                else:
                    if cruce['ID RECLAMANTE'].iloc[x:x+1].values[0] == cruce['ID RECLAMANTE'].iloc[j-1:j].values[0] and cruce['NUMERO FACTURA'].iloc[x:x+1].values[0] == cruce['NUMERO FACTURA'].iloc[j-1:j].values[0]:
                        cruce['recuentoFacturaHR'].iloc[x:x+1] = cruce['recuentoFacturaHR'].iloc[x-1:x].values[0] + 1
                    else:
                        cruce['recuentoFacturaHR'].iloc[x:x+1] = 1
                j = j + 1
                
            "validacion para que si en hr cruza pero es error y solo es 1 registro, entonces lo mantiene para que no salga como 'no registra'"
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] == 1 and cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] == 1:
                        cruce['estadoError'].iloc[x:x+1] = 'n'
                except:
                        cruce['estadoError'].iloc[x:x+1] = 'n'
            
            "Se quitan los errores de radicacion de HR"
            df_hr_cartera = df_hr_cartera[df_hr_cartera['estadoError'] == 'n']
            
        except Exception as e:
            tm.showerror('Error for inicial:', str(e))
        # tm.showinfo("p2", "")
        #########################
        #########################
        "Punto para insertar validacion por amparos diferentes"
        #########################
        #########################

        "Se valida el saldo solicitado contra el vlr RADICADO de los movimientos de la HR"
        # Se comprueba si el Valor de la Cartera esta en HR 
        try:
            cruce['valida_Saldo_Rad'] = cruce[['VALOR','VLR RADICACION']].apply(lambda x:'s' if x['VALOR'] == x['VLR RADICACION'] else 
                                                                            's' if abs(x['VALOR'] - x['VLR RADICACION']) <= (x['VALOR'] * porcentual_especial) else 'n', axis=1)
            cruce['valida_Saldo_Glo'] = cruce[['VALOR','VLR GLOSADO']].apply(lambda x:'s' if x['VALOR'] == x['VLR GLOSADO'] else 
                                                                            's' if abs(x['VALOR'] - x['VLR GLOSADO']) <= (x['VALOR'] * porcentual_especial)else 'n', axis=1)#cambiar por porcentual si genera mucha diferencia
            cruce['valida_Saldo_Apr'] = cruce[['VALOR','VLR APROBADO']].apply(lambda x:'s' if x['VALOR'] == x['VLR APROBADO'] else  's' if abs(x['VALOR'] - x['VLR APROBADO']) <= (x['VALOR'] * porcentual)else 'n', axis=1)
        
        except Exception as e:
             tm.showerror("Error valida saldos:", str(e))                                                               
        
        "si la coincidencia de 'valida_Saldo_Glo' es == 's', entonces se devuelve el resultado actual a 'n' y el resultado anterior en 'valida_Saldo_Rad' a 's'"
        for x in range(len(cruce)):
            try:
                if cruce['NIT'].iloc[x:x+1].values[0] == cruce['NIT'].iloc[x+1:x+2].values[0] and cruce['FACTURA'].iloc[x:x+1].values[0] == cruce['FACTURA'].iloc[x+1:x+2].values[0] and cruce['valida_Saldo_Glo'].iloc[x:x+1].values[0] == 's':
                    cruce['valida_Saldo_Glo'].iloc[x:x+1] = 'n'
                    cruce['valida_Saldo_Rad'].iloc[x+1:x+2] = 's'
                else:
                    cruce['VLR_APROBADO_POST'].iloc[x:x+1] = 0
            except:
                pass

        # Cruce para Validar Amparos n/s
        "amparo de transporte"#630977
        cruce['tiene_dos_amparos'] = ''
        suma = 0
        x = 0
        for x in range(len(cruce)):
            try:
                if cruce['NIT'].iloc[x:x+1].values[0] == cruce['NIT'].iloc[x+1:x+2].values[0] and cruce['FACTURA'].iloc[x:x+1].values[0] == cruce['FACTURA'].iloc[x+1:x+2].values[0] and (cruce['AMPARO'].iloc[x:x+1].values[0] == transporte or cruce['AMPARO'].iloc[x+1:x+2].values[0] == transporte): # Que el NIT de la fila actual x sea igual al NIT de la fila siguiente x+1.
                    cruce['tiene_dos_amparos'].iloc[x:x+1] = 's'
                else:
                    cruce['tiene_dos_amparos'].iloc[x:x+1] = 'n'
            except:
                if cruce['NIT'].iloc[x:x+1].values[0] == cruce['NIT'].iloc[x-1:x].values[0] and cruce['FACTURA'].iloc[x:x+1].values[0] == cruce['FACTURA'].iloc[x-1:x].values[0] and cruce['AMPARO'].iloc[x:x+1].values[0] == transporte:
                    cruce['tiene_dos_amparos'].iloc[x:x+1] = 's'
                else:
                    cruce['tiene_dos_amparos'].iloc[x:x+1] = 'n'

        "Se reordena para obtener el vlr glosado de transporte reciente y sumarlo"        
        # cruce = cruce.sort_values(by=['ID RECLAMANTE','NUMERO FACTURA','recuentoFacturaHR'], ascending=False)
        # tm.showinfo("p3", "")
        "agrupar resultado amparos"                   
        cruce['resultado_amparos_agru'] = ''
        lista_amparos = []
        x = 0
        for x in range(len(cruce)):
            try:
                if cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] > 1:
                    i = x + 1
                    j = 1
                    flag = 0
                    while cruce['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1:
                        if flag == 0:
                            #if pd.Series(str(cruce['DOCUMENTO DE PAGO '].iloc[i-1:i].values[0])).notnull().any():
                            lista_amparos.append(cruce['tiene_dos_amparos'].iloc[i-1:i].values[0])
                            flag = 1
                        else:
                            #if pd.Series(str(cruce['DOCUMENTO DE PAGO '].iloc[i:i+1].values[0])).notnull().any():
                            lista_amparos.append(cruce['tiene_dos_amparos'].iloc[i:i+1].values[0])
                            i = i + 1
                            j = j + 1
                    cruce['resultado_amparos_agru'].iloc[x:x+1].values[0] = lista_amparos
                else:
                    cruce['resultado_amparos_agru'].iloc[x:x+1] = cruce['tiene_dos_amparos'].iloc[x:x+1]
                lista_amparos = []
                i = 0
            except:
                cruce['resultado_amparos_agru'].iloc[x:x+1] = cruce['tiene_dos_amparos'].iloc[x:x+1]
        
        ""
        for x in range(len(cruce)):
            if cruce['count'].iloc[x:x+1].values[0] > 1:
                if cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] > 1:
                    cruce['resultado_amparos_agru'].iloc[x:x+1] = cruce['resultado_amparos_agru'].iloc[x-1:x]

        ""
        cruce['gt'] = ''
        for x in range(len(cruce)):
            if 's' in cruce['resultado_amparos_agru'].iloc[x:x+1].values[0]:
                cruce['gt'].iloc[x:x+1] = 's'
                
####################************************************************************************************************
        "Se suma, agrupa el VLR APROBADO por registro, es decir, se agrupa el pago desde el movimiento mas antiguo"
        # !!!
        try: # 2 
            cruce['SUMA APROBADO'] = 0
            suma = 0
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] > 1:
                        cruce['SUMA APROBADO'].iloc[x:x+1] = cruce['SUMA APROBADO'].iloc[x-1:x].values[0] + cruce['VLR APROBADO'].iloc[x:x+1].values[0]
                    else:
                        cruce['SUMA APROBADO'].iloc[x:x+1] = cruce['VLR APROBADO'].iloc[x:x+1].values[0]
                    suma = 0
                    i = 0
                except:
                    cruce['SUMA APROBADO'].iloc[x:x+1] = cruce['VLR APROBADO'].iloc[x:x+1].values[0]
            
            # cruce['SUMA APROBADO'] = ''
            # suma = 0
            # x = 0
            # for x in range(len(cruce)):
            #     try:
            #         if cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] > 1:
            #             i = x + 1
            #             j = 1
            #             flag = 0
            #             while cruce['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1:
            #                 if flag == 0:
            #                     suma = cruce['VLR APROBADO'].iloc[i-1:i].values[0]
            #                     flag = 1
            #                 else:
            #                     suma = suma + cruce['VLR APROBADO'].iloc[i:i+1].values[0]
            #                     i = i + 1
            #                     j = j + 1
            #             cruce['SUMA APROBADO'].iloc[x:x+1] = suma
            #         else:
            #             cruce['SUMA APROBADO'].iloc[x:x+1] = cruce['VLR APROBADO'].iloc[x:x+1]
            #         suma = 0
            #         i = 0
            #     except:
            #         cruce['SUMA APROBADO'].iloc[x:x+1] = cruce['VLR APROBADO'].iloc[x:x+1]
            
            "suma aprobado gt"
            cruce['SUMA APROBADO gt'] = 0
            suma = 0
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] > 1 and cruce['gt'].iloc[x+1:x+2].values[0] == 's' and cruce['AMPARO'].iloc[x+1:x+2].values[0] == transporte:
                        i = x + 1
                        j = 1
                        flag = 0
                        while cruce['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1 and cruce['gt'].iloc[i:i+1].values[0] == 's' and cruce['AMPARO'].iloc[i:i+1].values[0] == transporte:
                            if flag == 0:
                                suma = cruce['VLR APROBADO'].iloc[i-1:i].values[0]
                                flag = 1
                            else:    
                                suma = suma + cruce['VLR APROBADO'].iloc[i:i+1].values[0]
                                i = i + 1
                                j = j + 1
                        cruce['SUMA APROBADO gt'].iloc[x:x+1] = suma
                    else:
                        cruce['SUMA APROBADO gt'].iloc[x:x+1] = cruce['VLR APROBADO'].iloc[x:x+1]
                    suma = 0
                    i = 0
                except:
                    cruce['SUMA APROBADO gt'].iloc[x:x+1] = cruce['VLR APROBADO'].iloc[x:x+1]
            
            ""
            for x in range(len(cruce)):
                if cruce['AMPARO'].iloc[x:x+1].values[0] != transporte:
                    cruce['SUMA APROBADO gt'].iloc[x:x+1].values[0] = 0
            
            # tm.showinfo("p4", "")         
            "suma radicado gt"
            cruce['SUMA RADICADO gt'] = 0
            suma = 0
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['NIT'].iloc[x:x+1].values[0] == cruce['NIT'].iloc[x+1:x+2].values[0] and cruce['FACTURA'].iloc[x:x+1].values[0] == cruce['FACTURA'].iloc[x+1:x+2].values[0] and cruce['gt'].iloc[x+1:x+2].values[0] == 's' and (cruce['AMPARO'].iloc[x+1:x+2].values[0] == transporte or cruce['AMPARO'].iloc[x:x+1].values[0] == transporte):
                        i = x + 1
                        j = 1
                        flag = 0
                        # while cruce['NIT'].iloc[x:x+1].values[0] == cruce['NIT'].iloc[x+1:x+2].values[0] and cruce['FACTURA'].iloc[x:x+1].values[0] == cruce['FACTURA'].iloc[x+1:x+2].values[0] and cruce['gt'].iloc[i:i+1].values[0] == 's' and (cruce['AMPARO'].iloc[x+1:x+2].values[0] == transporte or cruce['AMPARO'].iloc[x:x+1].values[0] == transporte):
                        #     if flag == 0:
                        #         suma = cruce['VLR RADICACION'].iloc[i-1:i].values[0]
                        #         flag = 1
                        #     else:    
                        #         suma = suma + cruce['VLR RADICACION'].iloc[i:i+1].values[0]
                        #         i = i + 1
                        #         j = j + 1
                        
                        cruce['SUMA RADICADO gt'].iloc[x:x+1] = cruce['VLR RADICACION'].iloc[x:x+1].values[0] + cruce['VLR RADICACION'].iloc[x+1:x+2].values[0]
                    else:
                        cruce['SUMA RADICADO gt'].iloc[x:x+1] = cruce['VLR RADICACION'].iloc[x:x+1]
                    suma = 0
                    i = 0
                except:
                    cruce['SUMA RADICADO gt'].iloc[x:x+1] = cruce['VLR RADICACION'].iloc[x:x+1]
            
            # for x in range(len(cruce)):
            #     fil1 = cruce['NIT'] == cruce['NIT'].iloc[x:x+1].values[0]
            #     fil2 = cruce['FACTURA'] == cruce['FACTURA'].iloc[x:x+1].values[0]
            #     fil3 = cruce['SUMA APROBADO gt'] > 0
            #     fil4 = cruce['gt'] == 's'
            #     fil5 = cruce['AMPARO'] == transporte
            #     fila = cruce[fil1 & fil2 & fil3 & fil4 & fil5]
            #     # aa = cruce[cruce['SUMA APROBADO gt']>0]
            #     v = fila['SUMA APROBADO gt'].min()
            #     cruce['SUMA APROBADO gt'].iloc[x:x+1].values[0] = v
            #     print(x)
            
                       
               
            cruce_gt = cruce[cruce['SUMA APROBADO gt']>0]
            cruce_gt = cruce_gt.loc[:,['NIT','FACTURA']].drop_duplicates()
            cruce_gt = pd.merge(cruce_gt,cruce, on=['NIT','FACTURA'], how='inner')
            for x in range(len(cruce_gt)):
                fil1 = cruce_gt['NIT'] == cruce_gt['NIT'].iloc[x:x+1].values[0]
                # print(fil1)
                fil2 = cruce_gt['FACTURA'] == cruce_gt['FACTURA'].iloc[x:x+1].values[0]
                fil3 = cruce_gt['SUMA APROBADO gt'] > 0
                fil4 = cruce_gt['gt'] == 's'
                fil5 = cruce_gt['AMPARO'] == transporte
                fila = cruce_gt[fil1 & fil2 & fil3 & fil4 & fil5]
                # print(fila)
                # aa = cruce_gt[cruce_gt['SUMA APROBADO gt']>0]
                v = fila['SUMA APROBADO gt'].min()
                if np.isnan(v).any():
                    v = 0
                cruce_gt['SUMA APROBADO gt'].iloc[x:x+1].values[0] = v
                # print(x)
            cruce_gt = cruce_gt.loc[:,['FACTURA IQ','SUMA APROBADO gt']]
            cruce_gt = cruce_gt.rename(columns={'SUMA APROBADO gt':'SUMA APROBADO gt2'})
            cruce_gt = cruce_gt[cruce_gt['FACTURA IQ'].notnull()]
            cruce = pd.merge(cruce,cruce_gt, on=['FACTURA IQ'], how='left')
            cruce['SUMA APROBADO gt'] = cruce.apply(lambda x: x['SUMA APROBADO gt2'] if x['SUMA APROBADO gt2'] > 0 else x['SUMA APROBADO gt'], axis=1)
            cruce = cruce.drop('SUMA APROBADO gt2', axis=1)
            
                
            "Se ordena de mas reciente a mas antiguo para traer el valor pago total"
            # cruce = cruce.sort_values(by=['NIT','FACTURA','recuentoFacturaHR'], ascending=True)
            
            "Se trae el total del pago realizado"
            cruce['TOTAL APROBADO'] = 0
            # suma = 0
            # x = 0
            # for x in range(len(cruce)):
            #     try:
            #         if cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] == 1:
            #             cruce['TOTAL APROBADO'].iloc[x:x+1] = cruce['TOTAL APROBADO'].iloc[x-1:x]
            #         else:
            #             cruce['TOTAL APROBADO'].iloc[x:x+1] = cruce['SUMA APROBADO'].iloc[x:x+1]
            #     except:
            #         cruce['TOTAL APROBADO'].iloc[x:x+1] = cruce['SUMA APROBADO'].iloc[x:x+1]
            
            # for x in range(len(cruce)):
            #     fil1 = cruce['NIT'] == cruce['NIT'].iloc[x:x+1].values[0]
            #     fil2 = cruce['FACTURA'] == cruce['FACTURA'].iloc[x:x+1].values[0]
            #     fila = cruce[fil1 & fil2]

            #     v = fila['SUMA APROBADO'].max()
            #     cruce['TOTAL APROBADO'].iloc[x:x+1] = v
            
            cruce_pt = cruce[cruce['SUMA APROBADO']>0]
            cruce_pt = cruce_pt.loc[:,['NIT','FACTURA']].drop_duplicates()
            cruce_pt = pd.merge(cruce_pt,cruce, on=['NIT','FACTURA'], how='inner')
            for x in range(len(cruce_pt)):
                fil1 = cruce_pt['NIT'] == cruce_pt['NIT'].iloc[x:x+1].values[0]
                fil2 = cruce_pt['FACTURA'] == cruce_pt['FACTURA'].iloc[x:x+1].values[0]
                fila = cruce_pt[fil1 & fil2]
                # print(x)
                v = fila['SUMA APROBADO'].max()
                cruce_pt['TOTAL APROBADO'].iloc[x:x+1] = v
            cruce_pt = cruce_pt.loc[:,['FACTURA IQ','TOTAL APROBADO']]
            cruce_pt = cruce_pt.rename(columns={'TOTAL APROBADO':'TOTAL APROBADO2'})
            cruce_pt = cruce_pt[cruce_pt['FACTURA IQ'].notnull()]
            cruce = pd.merge(cruce,cruce_pt, on=['FACTURA IQ'], how='left')
            cruce['TOTAL APROBADO'] = cruce.apply(lambda x: x['TOTAL APROBADO2'] if x['TOTAL APROBADO2'] > 0 else x['TOTAL APROBADO'], axis=1)
            cruce = cruce.drop('TOTAL APROBADO2', axis=1)
            
            
            #==================================================================
            # Uso de la función para quitar duplicados del df cruce
            cruce = eliminar_duplicados_y_resetear(cruce)
            
            #==================================================================
            
                        
            "Traer la ultima glosa correspondiente"
            cruce['Ultimo Valor Glosado'] = 0
            suma = 0
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] > 1:
                        i = x + 1
                        j = 1
                        flag = 0
                        while cruce['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1:
                            if flag == 0:
                                suma = cruce['VLR GLOSADO'].iloc[i-1:i].values[0]
                                flag = 1
                            else:    
                                suma = cruce['VLR GLOSADO'].iloc[i:i+1].values[0]
                                i = i + 1
                                j = j + 1
                        cruce['Ultimo Valor Glosado'].iloc[x:x+1] = suma
                    else:
                        cruce['Ultimo Valor Glosado'].iloc[x:x+1] = cruce['VLR GLOSADO'].iloc[x:x+1]
                    suma = 0
                    i = 0
                except:
                    cruce['Ultimo Valor Glosado'].iloc[x:x+1] = cruce['VLR GLOSADO'].iloc[x:x+1]
            
            "ultimo valor glosado, se valida nuevamente para ratificar"
            # for x in range(len(cruce)):
            #     fil1 = cruce['NIT'] == cruce['NIT'].iloc[x:x+1].values[0]
            #     fil2 = cruce['FACTURA'] == cruce['FACTURA'].iloc[x:x+1].values[0]
            #     fila = cruce[fil1 & fil2]
                
            #     v = fila['Ultimo Valor Glosado'].min()
            #     cruce['Ultimo Valor Glosado'].iloc[x:x+1] = v
            
            
            cruce_g = cruce[cruce['VLR GLOSADO']>0]
            cruce_g = cruce_g.loc[:,['NIT','FACTURA']].drop_duplicates()
            cruce_g = pd.merge(cruce_g,cruce, on=['NIT','FACTURA'], how='inner')  
            for x in range(len(cruce_g)):
                fil1 = cruce_g['NIT'] == cruce_g['NIT'].iloc[x:x+1].values[0]
                fil2 = cruce_g['FACTURA'] == cruce_g['FACTURA'].iloc[x:x+1].values[0]
                fila = cruce_g[fil1 & fil2]
                
                v = fila['Ultimo Valor Glosado'].min()
                if np.isnan(v).any():
                    v = 0
                cruce_g['Ultimo Valor Glosado'].iloc[x:x+1] = v
            cruce_g = cruce_g.loc[:,['FACTURA IQ','Ultimo Valor Glosado']]
            cruce_g = cruce_g.rename(columns={'Ultimo Valor Glosado':'Ultimo Valor Glosado2'})
            cruce_g = cruce_g[cruce_g['FACTURA IQ'].notnull()]
            cruce = pd.merge(cruce,cruce_g, on=['FACTURA IQ'], how='left')
            cruce['Ultimo Valor Glosado'] = cruce.apply(lambda x: x['Ultimo Valor Glosado2'] if x['Ultimo Valor Glosado2'] > 0 else x['Ultimo Valor Glosado'], axis=1)
            cruce = cruce.drop('Ultimo Valor Glosado2', axis=1)
            
            #==================================================================
            # Uso de la función para quitar duplicados del df cruce
            cruce = eliminar_duplicados_y_resetear(cruce)
            
            #==================================================================
            
               
            "Traer la ultima glosa de gt correspondiente"
            cruce['Ultimo Valor Glosado gt'] = 0
            for x in range(len(cruce)):
                if cruce['gt'].iloc[x:x+1].values[0] == 's' and cruce['AMPARO'].iloc[x:x+1].values[0] == medico:
                    cruce['Ultimo Valor Glosado gt'].iloc[x:x+1].values[0] = cruce['VLR GLOSADO'].iloc[x:x+1].values[0]
            
            ""
            # for x in range(len(cruce)):
            #     fil1 = cruce['NIT'] == cruce['NIT'].iloc[x:x+1].values[0]
            #     fil2 = cruce['FACTURA'] == cruce['FACTURA'].iloc[x:x+1].values[0]
            #     fil3 = cruce['Ultimo Valor Glosado gt'] != 0
            #     fil4 = cruce['gt'] == 's'
            #     fil5 = cruce['AMPARO'] == medico
            #     fila = cruce[fil1 & fil2 & fil3 & fil4 & fil5]
                
            #     v = fila['Ultimo Valor Glosado gt'].min()
            #     cruce['Ultimo Valor Glosado gt'].iloc[x:x+1].values[0] = v
            
            
            cruce['SUMA APROBADO'] = cruce['SUMA APROBADO'].fillna(0)
            cruce['SUMA APROBADO gt'] = cruce['SUMA APROBADO gt'].fillna(0)
            cruce['SUMA RADICADO gt'] = cruce['SUMA RADICADO gt'].fillna(0)
            cruce['TOTAL APROBADO'] = cruce['TOTAL APROBADO'].fillna(0)
            cruce['Ultimo Valor Glosado'] = cruce['Ultimo Valor Glosado'].fillna(0)
            cruce['VLR RADICACION'] = cruce['VLR RADICACION'].fillna(0)
            cruce['VLR APROBADO'] = cruce['VLR APROBADO'].fillna(0)
            cruce['VLR GLOSADO'] = cruce['VLR GLOSADO'].fillna(0)
            cruce['Ultimo Valor Glosado gt'] = cruce['Ultimo Valor Glosado gt'].fillna(0)
            
            cruce_g_gt = cruce[cruce['gt'] == 's']
            cruce_g_gt = cruce_g_gt.loc[:,['NIT','FACTURA']].drop_duplicates()
            cruce_g_gt = pd.merge(cruce_g_gt,cruce, on=['NIT','FACTURA'], how='inner')
            for x in range(len(cruce_g_gt)):
                fil1 = cruce_g_gt['NIT'] == cruce_g_gt['NIT'].iloc[x:x+1].values[0]
                fil2 = cruce_g_gt['FACTURA'] == cruce_g_gt['FACTURA'].iloc[x:x+1].values[0]
                fil3 = cruce_g_gt['Ultimo Valor Glosado gt'] > 0
                fil4 = cruce_g_gt['gt'] == 's'
                fil5 = cruce_g_gt['AMPARO'] == medico
                fila = cruce_g_gt[fil1 & fil2 & fil3 & fil4 & fil5]
                
                # fila = cruce_g_gt[(cruce_g_gt['NIT'] == cruce_g_gt['NIT'].iloc[x:x+1].values[0])&(cruce_g_gt['FACTURA'] == cruce_g_gt['FACTURA'].iloc[x:x+1].values[0])
                #                   &(cruce_g_gt['Ultimo Valor Glosado gt'] > 0)&(cruce_g_gt['gt'] == 's')&(cruce_g_gt['AMPARO'] == medico)]
                
                v = fila['Ultimo Valor Glosado gt'].min()
                if np.isnan(v).any():
                    v = 0
                cruce_g_gt['Ultimo Valor Glosado gt'].iloc[x:x+1].values[0] = v
            cruce_g_gt = cruce_g_gt.loc[:,['FACTURA IQ','Ultimo Valor Glosado gt']]
            cruce_g_gt = cruce_g_gt.rename(columns={'Ultimo Valor Glosado gt':'Ultimo Valor Glosado gt2'})
            cruce_g_gt = cruce_g_gt[cruce_g_gt['FACTURA IQ'].notnull()]
            cruce = pd.merge(cruce,cruce_g_gt, on=['FACTURA IQ'], how='left')
            cruce['Ultimo Valor Glosado gt'] = cruce.apply(lambda x: x['Ultimo Valor Glosado gt2'] if x['Ultimo Valor Glosado gt2'] > 0 else x['Ultimo Valor Glosado gt'], axis=1)
            cruce = cruce.drop('Ultimo Valor Glosado gt2', axis=1)
            
            #==================================================================
            # Uso de la función para quitar duplicados del df cruce
            cruce = eliminar_duplicados_y_resetear(cruce)
            
            #==================================================================
      
            "valor maximo de gt"
            cruce['max_vlr_radicado_gt'] = ''
            # for x in range(len(cruce)):
            #     fil1 = cruce['NIT'] == cruce['NIT'].iloc[x:x+1].values[0]
            #     fil2 = cruce['FACTURA'] == cruce['FACTURA'].iloc[x:x+1].values[0]
            #     # fil3 = cruce['Ultimo Valor Glosado gt'] != 0
            #     fil4 = cruce['gt'] == 's'
            #     fil5 = cruce['AMPARO'] == transporte
            #     fila = cruce[fil1 & fil2 & fil4 & fil5]
                
            #     v = fila['VLR RADICACION'].max()
            #     cruce['max_vlr_radicado_gt'].iloc[x:x+1].values[0] = v
            
            cruce_max_gt = cruce[cruce['gt'] == 's']
            cruce_max_gt = cruce_max_gt.loc[:,['NIT','FACTURA']].drop_duplicates()
            cruce_max_gt = pd.merge(cruce_max_gt,cruce, on=['NIT','FACTURA'], how='inner')
            for x in range(len(cruce_max_gt)):
                fil1 = cruce_max_gt['NIT'] == cruce_max_gt['NIT'].iloc[x:x+1].values[0]
                fil2 = cruce_max_gt['FACTURA'] == cruce_max_gt['FACTURA'].iloc[x:x+1].values[0]
                # fil3 = cruce['Ultimo Valor Glosado gt'] != 0
                fil4 = cruce_max_gt['gt'] == 's'
                fil5 = cruce_max_gt['AMPARO'] == transporte
                fila = cruce_max_gt[fil1 & fil2 & fil4 & fil5]
                
                v = fila['VLR RADICACION'].max()
                if np.isnan(v).any():
                    v = 0
                cruce_max_gt['max_vlr_radicado_gt'].iloc[x:x+1].values[0] = v
            cruce_max_gt = cruce_max_gt.loc[:,['FACTURA IQ','max_vlr_radicado_gt']]
            cruce_max_gt = cruce_max_gt.rename(columns={'max_vlr_radicado_gt':'max_vlr_radicado_gt2'})
            cruce_max_gt = cruce_max_gt[cruce_max_gt['FACTURA IQ'].notnull()]
            cruce = pd.merge(cruce,cruce_max_gt, on=['FACTURA IQ'], how='left')
            cruce['max_vlr_radicado_gt'] = cruce.apply(lambda x: x['max_vlr_radicado_gt2'] if x['max_vlr_radicado_gt2'] > 0 else x['max_vlr_radicado_gt'], axis=1)
            cruce = cruce.drop('max_vlr_radicado_gt2', axis=1)
            # print(cruce['max_vlr_radicado_gt'])
            
            
            #==================================================================
            # Uso de la función para quitar duplicados del df cruce
            cruce = eliminar_duplicados_y_resetear(cruce)
            
            #==================================================================
                
                
            "valor maximo de gm"
            cruce['max_vlr_radicado_gm'] = 0
            # for x in range(len(cruce)):
            #     fil1 = cruce['NIT'] == cruce['NIT'].iloc[x:x+1].values[0]
            #     fil2 = cruce['FACTURA'] == cruce['FACTURA'].iloc[x:x+1].values[0]
            #     # fil3 = cruce['Ultimo Valor Glosado gt'] != 0
            #     fil4 = cruce['gt'] == 's'
            #     fil5 = cruce['AMPARO'] == medico
            #     fila = cruce[fil1 & fil2 & fil4 & fil5]
                
            #     v = fila['VLR RADICACION'].max()
            #     cruce['max_vlr_radicado_gm'].iloc[x:x+1].values[0] = v
            
            cruce_max_gm = cruce[cruce['gt'] == 's']
            cruce_max_gm = cruce_max_gm.loc[:,['NIT','FACTURA']].drop_duplicates()
            cruce_max_gm = pd.merge(cruce_max_gm,cruce, on=['NIT','FACTURA'], how='inner')
            for x in range(len(cruce_max_gm)):
                fil1 = cruce_max_gm['NIT'] == cruce_max_gm['NIT'].iloc[x:x+1].values[0]
                fil2 = cruce_max_gm['FACTURA'] == cruce_max_gm['FACTURA'].iloc[x:x+1].values[0]
                # fil3 = cruce['Ultimo Valor Glosado gt'] != 0
                fil4 = cruce_max_gm['gt'] == 's'
                fil5 = cruce_max_gm['AMPARO'] == medico
                fila = cruce_max_gm[fil1 & fil2 & fil4 & fil5]
                
                v = fila['VLR RADICACION'].max()
                if np.isnan(v).any():
                    v = 0
                cruce['max_vlr_radicado_gm'].iloc[x:x+1].values[0] = v
            cruce_max_gm = cruce_max_gm.loc[:,['FACTURA IQ','max_vlr_radicado_gm']]
            cruce_max_gm = cruce_max_gm.rename(columns={'max_vlr_radicado_gm':'max_vlr_radicado_gm2'})
            cruce_max_gm = cruce_max_gm[cruce_max_gm['FACTURA IQ'].notnull()]
            cruce = pd.merge(cruce,cruce_max_gm, on=['FACTURA IQ'], how='left')
            cruce['max_vlr_radicado_gm'] = cruce.apply(lambda x: x['max_vlr_radicado_gm2'] if x['max_vlr_radicado_gm2'] > 0 else x['max_vlr_radicado_gm'], axis=1)
            cruce = cruce.drop('max_vlr_radicado_gm2', axis=1)
            
                
            "Traer la ultimo radicado de glosa correspondiente"
            cruce['ULTIMO_RADICADO'] = ''
            ur = ''
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] > 1:
                        i = x + 1
                        j = 1
                        flag = 0
                        while cruce['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1:
                            if flag == 0:
                                ur = cruce['FACTURA IQ'].iloc[i-1:i].values[0]
                                flag = 1
                            else:    
                                ur = cruce['FACTURA IQ'].iloc[i:i+1].values[0]
                                i = i + 1
                                j = j + 1
                        cruce['ULTIMO_RADICADO'].iloc[x:x+1] = ur
                    else:
                        cruce['ULTIMO_RADICADO'].iloc[x:x+1] = cruce['FACTURA IQ'].iloc[x:x+1].values[0]
                    ur = ''
                    i = 0
                except:
                    cruce['ULTIMO_RADICADO'].iloc[x:x+1] = cruce['FACTURA IQ'].iloc[x:x+1].values[0]
            
            "Traer la ultimo ESTADO ACTUAL FACTURA"
            cruce['ULTIMO_ESTADO'] = ''
            ur = ''
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] > 1:
                        i = x + 1
                        j = 1
                        flag = 0
                        while cruce['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1:
                            if flag == 0:
                                ur = cruce['ESTADO ACTUAL FACTURA'].iloc[i-1:i].values[0]
                                flag = 1
                            else:
                                ur = cruce['ESTADO ACTUAL FACTURA'].iloc[i:i+1].values[0]
                                i = i + 1
                                j = j + 1
                        cruce['ULTIMO_ESTADO'].iloc[x:x+1] = ur
                    else:
                        cruce['ULTIMO_ESTADO'].iloc[x:x+1] = cruce['ESTADO ACTUAL FACTURA'].iloc[x:x+1].values[0]
                    ur = ''
                    i = 0
                except:
                    cruce['ULTIMO_RADICADO'].iloc[x:x+1] = cruce['ESTADO ACTUAL FACTURA'].iloc[x:x+1].values[0]
                    
            "Traer la primer fecha de aviso correspondiente"
            cruce['primerFechaAviso'] = ''
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] == 1:           
                        cruce['primerFechaAviso'].iloc[x:x+1] = cruce['F.AVISO'].iloc[x:x+1].values[0]
                    else:
                        cruce['primerFechaAviso'].iloc[x:x+1] = cruce['primerFechaAviso'].iloc[x-1:x].values[0]
                except:
                    #cruce['primerFechaAviso'].iloc[x:x+1] = cruce['F.AVISO'].iloc[x:x+1].values[0]
                    pass
            
            "Traer el primer valor radicado correspondiente"
            cruce['primerValorRadicado'] = 0
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] == 1:           
                        cruce['primerValorRadicado'].iloc[x:x+1] = cruce['VLR RADICACION'].iloc[x:x+1].values[0]
                    else:
                        cruce['primerValorRadicado'].iloc[x:x+1] = cruce['primerValorRadicado'].iloc[x-1:x].values[0]
                except:
                    #cruce['primerFechaAviso'].iloc[x:x+1] = cruce['F.AVISO'].iloc[x:x+1].values[0]
                    pass
            
            
            try:
                cruce['max_vlr_radicado_gm'] = cruce['max_vlr_radicado_gm'].fillna(0).replace('',0,regex=True).astype(float)
            except:
                pass
            try:
                cruce['max_vlr_radicado_gt'] = cruce['max_vlr_radicado_gt'].fillna(0).replace('',0,regex=True).astype(float)
            except:
                pass
            try:
                cruce['primerValorRadicado'] = cruce['primerValorRadicado'].fillna(0).astype(float)
            except:
                pass
            "resultado de gt"
            cruce['primerValorRadicado'] = cruce.apply(lambda x:
                                        x['max_vlr_radicado_gm'] + x['max_vlr_radicado_gt'] if x['max_vlr_radicado_gt'] > 0 else x['primerValorRadicado'], axis = 1)
            
            cruce['VLR_ADEUDADO_GT'] = cruce[['SUMA APROBADO gt','max_vlr_radicado_gt']].apply(lambda x:
                                        x['max_vlr_radicado_gt'] - x['SUMA APROBADO gt'] if x['SUMA APROBADO gt'] > 0 else x['max_vlr_radicado_gt'], axis = 1)
                
            cruce['Ultimo Valor Glosado'] = cruce[['Ultimo Valor Glosado','VLR_ADEUDADO_GT','Ultimo Valor Glosado gt']].apply(lambda x:
                                        x['Ultimo Valor Glosado'] - x['VLR_ADEUDADO_GT'] if x['VLR_ADEUDADO_GT'] > 0 else x['Ultimo Valor Glosado gt'] if x['Ultimo Valor Glosado gt'] > 0 else x['Ultimo Valor Glosado'], axis = 1)
            
            
            cruce['Ultimo Valor Glosado'] = cruce['Ultimo Valor Glosado'].fillna(0).astype(float)
            "Se calcula el valor adeudado real por mundial a la ips, se resta el vlr radicado - el vlr sumado del total aprobado"
            #cruce['primerValorRadicado'] = cruce['primerValorRadicado'].fillna(0).astype(float)
            #cruce['TOTAL APROBADO'] = cruce['TOTAL APROBADO'].fillna(0).astype(float)
            cruce['VALOR ADEUDADO REAL'] = abs(cruce['primerValorRadicado'] - cruce['TOTAL APROBADO'])

            "Traer Los radicados correspondientes agrupadas"
            cruce['RADICADOS_FACTURA'] = ''
            rad = []
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] > 1:
                        i = x + 1
                        j = 1
                        flag = 0
                        while cruce['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1:
                            if flag == 0:
                                #if pd.Series(str(cruce['FACTURA IQ'].iloc[i-1:i].values[0])).notnull().any():
                                rad.append(cruce['FACTURA IQ'].iloc[i-1:i].values[0])
                                flag = 1
                            else:
                                #if pd.Series(str(cruce['FACTURA IQ'].iloc[i:i+1].values[0])).notnull().any():
                                rad.append(cruce['FACTURA IQ'].iloc[i:i+1].values[0])
                                i = i + 1
                                j = j + 1
                        cruce['RADICADOS_FACTURA'].iloc[x:x+1].values[0] = rad
                    else:
                        cruce['RADICADOS_FACTURA'].iloc[x:x+1] = cruce['FACTURA IQ'].iloc[x:x+1]
                    rad = []
                    i = 0
                except:
                    cruce['RADICADOS_FACTURA'].iloc[x:x+1] = cruce['FACTURA IQ'].iloc[x:x+1]

            "Traer Las ordenes de pago correspondientes agrupadas"
            #cruce['DOCUMENTO DE PAGO '] = cruce['DOCUMENTO DE PAGO '].astype(str)
            cruce['Num OPS agrupadas'] = ''
            op = []
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] > 1:
                        i = x + 1
                        j = 1
                        flag = 0
                        while cruce['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1:
                            if flag == 0:
                                #if pd.Series(str(cruce['DOCUMENTO DE PAGO '].iloc[i-1:i].values[0])).notnull().any():
                                op.append(cruce['DOCUMENTO DE PAGO '].iloc[i-1:i].values[0])
                                flag = 1
                            else:
                                #if pd.Series(str(cruce['DOCUMENTO DE PAGO '].iloc[i:i+1].values[0])).notnull().any():
                                op.append(cruce['DOCUMENTO DE PAGO '].iloc[i:i+1].values[0])
                                i = i + 1
                                j = j + 1
                        cruce['Num OPS agrupadas'].iloc[x:x+1].values[0] = op
                    else:
                        cruce['Num OPS agrupadas'].iloc[x:x+1] = cruce['DOCUMENTO DE PAGO '].iloc[x:x+1]
                    op = []
                    i = 0
                except:
                    cruce['Num OPS agrupadas'].iloc[x:x+1] = cruce['DOCUMENTO DE PAGO '].iloc[x:x+1]

            "Traer Las fechas de giro de pago correspondientes agrupadas"
            cruce['Fechas Giro agrupadas'] = ''
            opFg = []
            x = 0
            for x in range(len(cruce)):
                try:
                    if cruce['recuentoFacturaHR'].iloc[x+1:x+2].values[0] > 1:
                        i = x + 1
                        j = 1
                        flag = 0
                        while cruce['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1:
                            if flag == 0:
                                #if str(cruce['F.GIRO'].iloc[i-1:i].values[0]).notnull():
                                opFg.append(cruce['F.GIRO'].iloc[i-1:i].values[0])
                                flag = 1
                            else:
                                #if str(cruce['F.GIRO'].iloc[i:i+1].values[0]).notnull():
                                opFg.append(cruce['F.GIRO'].iloc[i:i+1].values[0])
                                i = i + 1
                                j = j + 1
                        cruce['Fechas Giro agrupadas'].iloc[x:x+1].values[0] = opFg
                    else:
                        cruce['Fechas Giro agrupadas'].iloc[x:x+1] = cruce['F.GIRO'].iloc[x:x+1]
                    opFg = []
                    i = 0
                except:
                    cruce['Fechas Giro agrupadas'].iloc[x:x+1] = cruce['F.GIRO'].iloc[x:x+1]
            
            "ordenes de pago maximo de gt"
            cruce['ordenes_pago_gt'] = ''
            for x in range(len(cruce)):
                if cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] == 1 and cruce['gt'].iloc[x:x+1].values[0] == 's':
                    cruce['ordenes_pago_gt'].iloc[x:x+1].values[0] = cruce['Num OPS agrupadas'].iloc[x:x+1].values[0]
                elif cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] > 1 and cruce['gt'].iloc[x:x+1].values[0] == 's':
                    cruce['ordenes_pago_gt'].iloc[x:x+1].values[0] = cruce['ordenes_pago_gt'].iloc[x-1:x].values[0]
                else:
                    cruce['ordenes_pago_gt'].iloc[x:x+1].values[0] = '0'
                    
            "fechas de pago maximo de gt"
            cruce['fechas_pago_gt'] = ''
            for x in range(len(cruce)):
                if cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] == 1 and cruce['gt'].iloc[x:x+1].values[0] == 's':
                    cruce['fechas_pago_gt'].iloc[x:x+1].values[0] = cruce['Fechas Giro agrupadas'].iloc[x:x+1].values[0]
                elif cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] > 1 and cruce['gt'].iloc[x:x+1].values[0] == 's':
                    cruce['fechas_pago_gt'].iloc[x:x+1].values[0] = cruce['fechas_pago_gt'].iloc[x-1:x].values[0]
                else:
                    cruce['fechas_pago_gt'].iloc[x:x+1].values[0] = '0'
            # tm.showinfo("p5", "")    
            ##############################
            ##############################
            "Validaciones cartera"
            ##############################
            ##############################
            
            "Obtener el radicado de apertura"
            cruce['CORRELATIVO RADICADO'] = cruce['CORRELATIVO RADICADO'].fillna(0)
            cruce['CONSECUTIVO'] = cruce['CONSECUTIVO'].fillna(0)
            cruce = cruce.sort_values(by=['NIT','FACTURA','CORRELATIVO RADICADO'], ascending=True)
            cruce['count_correlativo'] = np.arange(1,len(cruce)+1)
            cruce['RADICADO_APERTURA'] = ''
            # for x in range(len(cruce)):
            #     # try:
            #     if cruce['CORRELATIVO RADICADO'].iloc[x:x+1].values[0] == 0:
            #         cruce['RADICADO_APERTURA'].iloc[x:x+1] = 0
            #     else:
            #         if cruce['CORRELATIVO RADICADO'].iloc[x:x+1].values[0] == 1:
            #             cruce['RADICADO_APERTURA'].iloc[x:x+1] = cruce['FACTURA IQ'].iloc[x:x+1].values[0]
            #         else:
            #             cruce['RADICADO_APERTURA'].iloc[x:x+1] = cruce['RADICADO_APERTURA'].iloc[x-1:x].values[0]
            #     # except:
            #         # cruce['RADICADO_APERTURA'].iloc[x:x+1] = cruce['RADICADO_APERTURA'].iloc[x-1:x].values[0]
            for x in range(len(cruce)):
                if cruce['AMPARO'].iloc[x:x+1].values[0] != medico:
                    cruce['RADICADO_APERTURA'].iloc[x:x+1] = 0
                else:
                    if cruce['CONSECUTIVO'].iloc[x:x+1].values[0] == 0:
                        cruce['RADICADO_APERTURA'].iloc[x:x+1] = 0
                    else:
                        if cruce['CONSECUTIVO'].iloc[x:x+1].values[0] == 1 and cruce['AMPARO'].iloc[x:x+1].values[0] == medico:
                            cruce['RADICADO_APERTURA'].iloc[x:x+1] = cruce['FACTURA IQ'].iloc[x:x+1].values[0]
                        else:
                            cruce['RADICADO_APERTURA'].iloc[x:x+1] = cruce['RADICADO_APERTURA'].iloc[x-1:x].values[0]
                if cruce['RADICADO_APERTURA'].iloc[x:x+1].values[0] == 0 and cruce['count_correlativo'].iloc[x:x+1].values[0] > 1:
                    cruce['RADICADO_APERTURA'].iloc[x:x+1].values[0] = cruce['RADICADO_APERTURA'].iloc[x-1:x].values[0]

            # cruce = cruce.sort_values(by=['NIT','FACTURA','CORRELATIVO RADICADO'], ascending=False)  
            
            "Se ordena el conteo de NIT FACTURA cruzado, para obneter desde el registro mas reciente al mas antiguo"
            cruce = cruce.sort_values(by=['NIT','FACTURA','recuentoFacturaHR'], ascending=False)

            "Se validan en este orden los campos comparados contra el saldo IPS y confirmar si el registro evaluado tiene similitud"
            try:
                cruce['valida_Saldo_Rad_gt'] = cruce[['VALOR','VLR RADICACION','SUMA RADICADO gt']].apply(lambda x:'s' if x['VALOR'] == x['SUMA RADICADO gt'] or x['VALOR'] == x['SUMA RADICADO gt'] else 
                                                                                's' if abs(x['VALOR'] - x['SUMA RADICADO gt']) <= (x['VALOR'] * porcentual_especial) else 'n', axis=1)
                cruce['valida_Saldo_Glo_gt'] = cruce[['VALOR','VLR GLOSADO','VLR_ADEUDADO_GT']].apply(lambda x:'s' if x['VALOR'] == x['VLR GLOSADO'] or x['VALOR'] == x['VLR_ADEUDADO_GT'] else 
                                                                                's' if abs(x['VALOR'] - x['VLR GLOSADO']) <= (x['VALOR'] * porcentual_especial)else 'n', axis=1)#cambiar por porcentual si genera mucha diferencia
                # cruce['valida_Saldo_Apr'] = cruce[['VALOR','VLR APROBADO']].apply(lambda x:'s' if x['VALOR'] == x['VLR APROBADO'] else  's' if abs(x['VALOR'] - x['VLR APROBADO']) <= (x['VALOR'] * porcentual)else 'n', axis=1)
            except Exception as e:
                 tm.showerror("Error valida saldos gt:", str(e))
            
            # cruce['SUMA_APROBADO_gt_v'] = 0
            # for x in range(len(cruce)):
            #     if cruce['valida_Saldo_Rad_gt'].iloc[x:x+1].values[0] == 's' and cruce['gt'].iloc[x:x+1].values[0] == 's':
            #         cruce['TOTAL APROBADO'].iloc[x:x+1] = 
                 
            cruce['RegistroCoincideConSaldoIPS'] = cruce[['valida_Saldo_Rad',
                                                          'valida_Saldo_Glo',
                                                          'valida_Saldo_Apr']].apply(
                                                              lambda x:'s' if 
                                                              x['valida_Saldo_Rad'] == 's' or
                                                              x['valida_Saldo_Glo'] == 's' or
                                                              x['valida_Saldo_Apr'] == 's' 
                                                               # or x['valida_Saldo_Apr'] == 's'#agregado de transporte
                                                              else 'n', axis=1)
            
            "trasnporte validacion"
            cruce['RegistroCoincideConSaldoIPS'] = cruce[['RegistroCoincideConSaldoIPS','valida_Saldo_Rad_gt','gt']].apply(
                                                              lambda x:'s' if x['gt'] == 's' and x['valida_Saldo_Rad_gt'] =='s'
                                                              else x['RegistroCoincideConSaldoIPS'], axis=1)                          
            # tm.showinfo("Cruce completado", "ok for")
            ####################
            "Se valida que las facturas que no tuvieron ninguna coincidencia por saldo IPS vs hr no se eliminen más adelante por el momento"
            cruce['NoCoincideConSaldoIPS'] = ''
            
            # suma = 0
            # x = 0
            # lista = []
            # for x in range(len(cruce)):
            #     #try:
            #         #if cruce['recuentoFacturaHR'].iloc[x:x+1].values[0] > 1:
            #             i = x
            #             j = 1
            #             flag = 0
            
            #             for n in range(cruce['recuentoFacturaHR'].iloc[x:x+1].values[0]):
            #                 lista.append(cruce['RegistroCoincideConSaldoIPS'].iloc[i:i+1].values[0])
            
            #                 i = i + 1
            #                 j = j + 1
            #             if 's' in lista:
            #                 cruce['NoCoincideConSaldoIPS'].iloc[x:x+1].values[0] = lista
            #             else:
            #                 cruce['NoCoincideConSaldoIPS'].iloc[x:x+1].values[0] = lista
            
            #             suma = 0
            #             i = 0
            #             n = 0
            #             lista = []
            #     #except:
            #     #    cruce['NoCoincideConSaldoIPS'].iloc[x:x+1] = 'n'

            cruce['count2'] = np.arange(1,len(cruce)+1)
            j = 0
            x = 1
            for x in range(len(cruce)):
                if cruce['count2'].iloc[x:x+1].values[0] == 1:
                    cruce['NoCoincideConSaldoIPS'].iloc[x:x+1] = 1        
                else:
                    if cruce['ID RECLAMANTE'].iloc[x:x+1].values[0] == cruce['ID RECLAMANTE'].iloc[j-1:j].values[0] and cruce['NUMERO FACTURA'].iloc[x:x+1].values[0] == cruce['NUMERO FACTURA'].iloc[j-1:j].values[0]:
                        cruce['NoCoincideConSaldoIPS'].iloc[x:x+1] = cruce['NoCoincideConSaldoIPS'].iloc[x-1:x].values[0] + 1
                    else:
                        cruce['NoCoincideConSaldoIPS'].iloc[x:x+1] = 1
                j = j + 1
        
        # !!!
        # Fin Try 2
                
        except Exception as e: #2
             tm.showerror("Error ciclos for 1:", str(e))
    
        cruce['NoCoincideConSaldoIPS'] = cruce[['NoCoincideConSaldoIPS','RegistroCoincideConSaldoIPS']].apply(lambda x:'s' if x['NoCoincideConSaldoIPS'] == 1 and x['RegistroCoincideConSaldoIPS'] == 'n' else 'n', axis=1)
        # tm.showinfo("p6", "")
        ######################
        "Eliminar duplicados, solo conservar los registros más recientes bajo las coincidencias expuestas anteriormente"
        ######################
        "Reordenar bajo el primer conteo 'count'"
        # cruce = cruce.sort_values(by='count', ascending=True)
        # tm.showinfo("p7", "")
        "validar nuevamente para no incluir falsos positivos"
        x = 1
        v = 0
        for x in range(len(cruce)):
            v = cruce[(cruce['NIT'].iloc[x:x+1].values[0] == cruce['NIT']) & (cruce['FACTURA'].iloc[x:x+1].values[0] == cruce['FACTURA']) & (cruce['RegistroCoincideConSaldoIPS'] == 's')]['FACTURA'].count()
            if v > 0:
                cruce['NoCoincideConSaldoIPS'].iloc[x:x+1] = 'n'
            else:
                cruce['NoCoincideConSaldoIPS'].iloc[x:x+1] = 's'
            v = 0
        # tm.showinfo("p8", "")
        "se crea campo para unicicar conceptos de validacion anterior"
        cruce['UnificarConceptosDeCoincidenciasSaldo'] = cruce[['NoCoincideConSaldoIPS','RegistroCoincideConSaldoIPS']].apply(lambda x:'s' if x['NoCoincideConSaldoIPS'] == 's' or x['RegistroCoincideConSaldoIPS'] == 's' else 'n', axis=1)
        
        "codigo para obtener el resultado mas reciente, actualmente no se ejecuta, está eliminando información"
        # cruce['UnificarConceptosDeCoincidenciasSaldo2'] = ''
        
        # for x in range(len(cruce)):
        #     if cruce['UnificarConceptosDeCoincidenciasSaldo'].iloc[x:x+1].values[0] == 's' and cruce['UnificarConceptosDeCoincidenciasSaldo'].iloc[x+1:x+2].values[0] == 's' and cruce['NIT'].iloc[x:x+1].values[0] == cruce['NIT'].iloc[x+1:x+2].values[0] and cruce['FACTURA'].iloc[x:x+1].values[0] == cruce['FACTURA'].iloc[x+1:x+2].values[0]:
        #         cruce['UnificarConceptosDeCoincidenciasSaldo2'].iloc[x:x+1] = 'n'
        #     else:
        #         cruce['UnificarConceptosDeCoincidenciasSaldo2'].iloc[x:x+1] = 's'
        # aa = cruce[cruce['FACTURA']=='HSFA23817']
        # print(df_ace_total.info())
        # print(df_ace_total['Valor Aceptado Ips'].sum())
        
        
        # aaa = cruce2[cruce2['FACTURA']=='661877']
        # # aa = cruce2[cruce2['RECLAMANTE'].notnull()]
        # aa = cruce4[cruce4['FACTURA']=='FEDV119581']#629730
        # # aa = df_hr_cartera[df_hr_cartera['NUMERO FACTURA'].str.contains('20530')]
        # aa = df_hr_cartera[df_hr_cartera['FACTURA IQ']== 'CMVIQ034000001359822']
        # # # # df_liq23.columns
        # ab = df_liq23[df_liq23['Numero_Radicado_Inicial']=='CMVIQ034000001648718']
        
        if cartera_judicial.get() == "activado":
            
            cruce2 = cruce
            
            "Reordenar bajo el primer conteo 'count'"
            cruce2 = cruce2.sort_values(by='count', ascending=True)
            
        else:
            "Se filtran la unificacion de resultado para solo traer las 's'"
            cruce2 = cruce[cruce['UnificarConceptosDeCoincidenciasSaldo']=='s']
            # tm.showinfo("p9", "")
            "Reordenar para obtener el concepto más reciente"
            #cruce2 = cruce2.sort_values(by=['NIT','FACTURA','F.AVISO'], ascending=False)
            
            "Se conservan unicamente los primeros registros que anteriormente se ordenaron con 'count'"
            cruce2 = cruce2.drop_duplicates(['NIT','FACTURA'], keep='first')
            
            "Reordenar bajo el primer conteo 'count'"
            cruce2 = cruce2.sort_values(by='count', ascending=True)
            
        # "resultado de gt"
        # cruce2['primerValorRadicado'] = cruce2[['max_vlr_radicado_gm','max_vlr_radicado_gt','primerValorRadicado']].apply(lambda x:
        #                             x['max_vlr_radicado_gm'] + x['max_vlr_radicado_gt'] if x['max_vlr_radicado_gt'] > 0 else x['primerValorRadicado'], axis = 1)
        
        # cruce2['VLR_ADEUDADO_GT'] = cruce2[['SUMA APROBADO gt','max_vlr_radicado_gt']].apply(lambda x:
        #                             x['max_vlr_radicado_gt'] - x['SUMA APROBADO gt'] if x['SUMA APROBADO gt'] > 0 else x['max_vlr_radicado_gt'], axis = 1)
            
        # cruce2['Ultimo Valor Glosado'] = cruce2[['Ultimo Valor Glosado','VLR_ADEUDADO_GT']].apply(lambda x:
        #                             x['Ultimo Valor Glosado'] - x['VLR_ADEUDADO_GT'] if x['VLR_ADEUDADO_GT'] > 0 else x['Ultimo Valor Glosado'], axis = 1)
        
        
        #######################
        #######################
        "Se realiza el cruce contra la data de operadores"
        #######################
        #######################
        "Cruce contra 'detalle liquidacion'"
        
        df_liq_riq = df_liq_riq.drop_duplicates()
        
        df_liq_riq_agrupado = df_liq_riq
        
        df_liq_riq_agrupado = df_liq_riq_agrupado.drop_duplicates()
        # ======================================================================
        # Se cambia el codigo de glosa para que tome el primero
        #!!!
        
        if glosa_anterior.get() == "activado":
            
            
            #==================================================================
            print("="*41)
            
            
            df_liq = df_liq.drop_duplicates()
            df_riq2 = df_riq2.drop_duplicates()
            
            df_hr_cartera2 = df_hr_cartera.loc[:,['FACTURA IQ','F.LIQUIDACION']].drop_duplicates('FACTURA IQ', keep='first').rename(columns={'FACTURA IQ':'Numero_Radicado_Inicial'})
            df_hr_cartera2 = df_hr_cartera2.drop_duplicates()
            
            df_liq2 = pd.merge(df_hr_cartera2, df_liq, left_on='Numero_Radicado_Inicial', right_on='Numero_Radicado_Inicial', how='right')
            df_liq2 = df_liq2[df_liq2['F.LIQUIDACION'].fillna('na') != 'na']
            
            df_liq2 = df_liq2.drop_duplicates()
        
            
            df_riq22 = pd.merge(df_hr_cartera2, df_riq2, left_on='Numero_Radicado_Inicial', right_on='Numero_Radicado_Inicial2', how='right')
            df_riq22 = df_riq22.drop_duplicates()
            
            df_riq22 = df_riq22[df_riq22['Numero_Radicado_Inicial_x'].fillna('na').str.contains('0')].rename(columns={'Numero_Radicado_Inicial_y':'Numero_Radicado_Inicial'}).drop('Numero_Radicado_Inicial_x', axis=1)
            df_liq_riq2 = pd.concat([df_liq2,df_riq22]).sort_values(['Numero_Radicado_Inicial','F.LIQUIDACION'], ascending=False).drop('F.LIQUIDACION', axis=1)
            
            
            df_liq2 = df_liq2.drop_duplicates()
            df_riq22 = df_riq22.drop_duplicates()
            df_liq_riq2 =  df_liq_riq2.drop_duplicates()
            
            
            
            # Convertir la columna 'Codigo_glosa_general_id' a tipo numérico, manejando errores
            df_liq_riq2['Codigo_glosa_general_id'] = pd.to_numeric(df_liq_riq2['Codigo_glosa_general_id'], errors='coerce')
            
            # df_liq_riq2.info()            
            #==================================================================
            
            "v1"
            for r in range(len(df_liq_riq2)):
                l = df_liq_riq2[df_liq_riq2['Numero_Radicado_Inicial'] == df_liq_riq2['Numero_Radicado_Inicial'].iloc[r:r+1].values[0]]
                if df_liq_riq2['Codigo_glosa_general_id'].iloc[r:r+1].values[0] == 9.0:
                    for w in range(len(l)):
                        if df_liq_riq2['Codigo_de_servicio'].iloc[r:r+1].values[0] == l['Codigo_de_servicio'].iloc[w:w+1].values[0] and l['Codigo_glosa_general_id'].iloc[w:w+1].values[0].astype(int) != 9 and df_liq_riq2['Valor_Servicio'].iloc[r:r+1].values[0] == l['Valor_Servicio'].iloc[w:w+1].values[0]:
                            df_liq_riq2['Codigo_glosa_general_id'].iloc[r:r+1].values[0] = l['Codigo_glosa_general_id'].iloc[w:w+1].values[0]
                            continue
            
            df_liq_riq2 =  df_liq_riq2.drop_duplicates()
            
         
            
            
            for r in range(len(df_liq_riq2)):
                if df_liq_riq2['Numero_Radicado_Inicial2'].iloc[r:r+1].values[0] == '':
                    df_liq_riq2['Numero_Radicado_Inicial2'].iloc[r:r+1].values[0] = df_liq_riq2['Numero_Radicado_Inicial'].iloc[r:r+1].values[0]
            
            df_liq_riq2 = df_liq_riq2.rename(columns={'Numero_Radicado_Inicial2':'Numero_Radicado_Inicial','Numero_Radicado_Inicial':'Numero_Radicado_Inicial2'})
            
            df_liq_riq_agrupado = df_liq_riq2
            
            print("="*41)
            #==================================================================
        #!!!
            
    
        df_liq_riq_agrupado['centro_costo_maos'] = np.where(df_liq_riq_agrupado['Centro_de_costo'].str.contains('steos'), 's','n')
        
        df_liq_riq_agrupado['Codigo_glosa_general_id'] = df_liq_riq_agrupado['Codigo_glosa_general_id'].fillna(0)
        
        df_liq_riq_agrupado = df_liq_riq_agrupado.groupby(['Numero_Radicado_Inicial','Codigo_glosa_general_id','centro_costo_maos'])[['Valor_Servicio','Valor_Aprobado_Inicial','Valor_glosado_Inicial','ValorAIPS','ValorSRTAIPS']].sum()
     
       
        df_liq_riq_agrupado = df_liq_riq_agrupado.reset_index()
        
        
        if cartera_judicial.get() == "activado":
            
            "Se cruza contra liquidacion"
            "se cambia la logica, se cruza con todos los radicados de hr para traer cda detalle"
            cruce2 = pd.merge(cruce2, df_liq_riq_agrupado, left_on='FACTURA IQ', right_on='Numero_Radicado_Inicial', how='left')
            
        else:
            "Se cruza contra liquidacion"
            cruce2 = pd.merge(cruce2, df_liq_riq_agrupado, left_on='ULTIMO_RADICADO', right_on='Numero_Radicado_Inicial', how='left')
        
        "Se clasifican los rubros de glosa"
        try:
            cruce2['RUBRO_OBJ'] = cruce2[['Codigo_glosa_general_id','centro_costo_maos']].apply(lambda x: 
                                            'MAOS' if x['Codigo_glosa_general_id'] > 0 and x['centro_costo_maos'] == 's' or
                                            x['Codigo_glosa_general_id'] == maos_MOK else
                                            'FACTURACION' if x['Codigo_glosa_general_id'] == facturacion_IQ[0] or 
                                            x['Codigo_glosa_general_id'] == facturacion_IQ[1] or 
                                            x['Codigo_glosa_general_id'] == facturacion_IQ[2] or
                                            x['Codigo_glosa_general_id'] == facturacion_MOK and x['centro_costo_maos'] == 'n' else
                                            'TARIFAS' if x['Codigo_glosa_general_id'] == tarifas_IQ or
                                            x['Codigo_glosa_general_id'] == tarifas_MOK[0] or 
                                            x['Codigo_glosa_general_id'] == tarifas_MOK[1] and 
                                            x['centro_costo_maos'] == 'n' else
                                            'SOPORTES' if x['Codigo_glosa_general_id'] == soportes_IQ or
                                            x['Codigo_glosa_general_id'] == soportes_MOK and x['centro_costo_maos'] == 'n' else
                                            'COBERTURA' if x['Codigo_glosa_general_id'] == cobertura_IQ or
                                            x['Codigo_glosa_general_id'] == cobertura_MOK and x['centro_costo_maos'] == 'n' else
                                            'PERTINENCIA' if x['Codigo_glosa_general_id'] == pertinencia_IQ or
                                            x['Codigo_glosa_general_id'] == pertinencia_MOK[0] or 
                                            x['Codigo_glosa_general_id'] == pertinencia_MOK[1] or
                                            x['Codigo_glosa_general_id'] == pertinencia_MOK[2] or 
                                            x['Codigo_glosa_general_id'] == pertinencia_MOK[3] or 
                                            x['Codigo_glosa_general_id'] == pertinencia_MOK[4] or
                                            x['Codigo_glosa_general_id'] == pertinencia_MOK[5] and x['centro_costo_maos'] == 'n' else
                                            'HABILITACION' if x['Codigo_glosa_general_id'] == habilitacion_IQ[0] or x['Codigo_glosa_general_id'] == habilitacion_IQ[1] or
                                            x['Codigo_glosa_general_id'] == habilitacion_MOK and x['centro_costo_maos'] == 'n' else 'NoAplica' ,axis=1)
                
        except Exception as e:
             tm.showerror("Error rubro objecion:", str(e))
        
        "opción 1, agrupación de maos: se agrupa nuevamente, ya que el rubro de MAOS se encuentra en diferentes códigos de glosa general id"
        cruce_agrup = cruce2
        "se agrupa por concepto de RUBRO_OBJ"
        cruce_agrup = cruce_agrup.groupby(['Numero_Radicado_Inicial','RUBRO_OBJ'])[['Valor_Servicio','Valor_Aprobado_Inicial','Valor_glosado_Inicial','ValorAIPS','ValorSRTAIPS']].sum()
        cruce_agrup = cruce_agrup.reset_index(['Numero_Radicado_Inicial','RUBRO_OBJ'])
        cruce_agrup = cruce_agrup.rename(columns={'Numero_Radicado_Inicial':'radicado_agrupado','RUBRO_OBJ':'RUBRO_OBJ'})
        
        
        "se quitan los campos de la tabla cruce2, para recalcular agrupación en cruce_agrup"
        cruce2 = cruce2.loc[:,['NIT', 'FACTURA', 'VALOR', 'Unnamed: 0', 'SUCURSAL', 'FACTURA IQ',
                'LOTE IQ', 'SINIESTRO', 'PLACA', 'NRO. POLIZA', 'CLASE VEHICULO',
                'NUMERO FACTURA', 'COD CIUDAD RECLAMACION FACTURA',
                'CIUDAD RECLAMACION FACTURA', 'VLR CONSTITUCION RVA', 'VLR RADICACION',
                'VLR APROBADO', 'VLR GLOSADO', 'AMPARO', 'TD RECLA', 'ID RECLAMANTE',
                'RECLAMANTE', 'ENT. EMBARGADA', 'DPTO RECLAMANTE', 'MUNC RECLAMANTE',
                'F.OCURRENCIA', 'COD MUNC OCURRENCIA', 'MUNC OCURRENCIA', 'TD VICTIMA',
                'DOC VICTIMA', 'VICTIMA', 'CORRELATIVO RADICADO', 'CONSECUTIVO',
                'USUARIO CREADOR FACTURA', 'USUARIO CREADOR RESERVA', 'F.FACTURA',
                'F.AVISO', 'F.CREA FACTURA', 'F.ENT AUDITOR', 'F.CREA RESERVA',
                'DIAS F.AVISO A F.CREA RESER', 'ANALISTA LIQUIDADOR', 'F.LIQUIDACION',
                'ESTADO ACTUAL FACTURA', 'F.SOLICITUD DE PAGO', 'F.ORDEN PAGO',
                'NUMERO ORDEN DE PAGO', 'F.GIRO', 'DOCUMENTO DE PAGO ',
                'DIAS VENCI: F.AVISO A F.GIRO', 'F.AVISO CHEQUE', 'F. NOTIFICACION',
                'OPERADOR ADMINISTRADOR', 'estadoError', 'FACTURA_2', 'count',
                'recuentoFacturaHR', 'valida_Saldo_Rad', 'valida_Saldo_Glo',
                'valida_Saldo_Apr', 'SUMA APROBADO', 'TOTAL APROBADO', 'gt',
                'Ultimo Valor Glosado', 'ULTIMO_RADICADO','ULTIMO_ESTADO', 'primerFechaAviso',
                'primerValorRadicado', 'VALOR ADEUDADO REAL', 'RADICADOS_FACTURA',
                'Num OPS agrupadas', 'Fechas Giro agrupadas', 'RADICADO_APERTURA',
                'RegistroCoincideConSaldoIPS', 'NoCoincideConSaldoIPS', 'count2',
                'UnificarConceptosDeCoincidenciasSaldo', 'Numero_Radicado_Inicial',
                'Codigo_glosa_general_id','fechas_pago_gt','ordenes_pago_gt']]
        
        "se eliminan los registros de los bucles for anteriores, esto ya se encuentra en la tabla cruce_agup"
        cruce0 = cruce2[~cruce2['FACTURA IQ'].notnull()]
        cruce0['RADICADO_APERTURA'] = ''
        
        cruce2 = cruce2[cruce2['FACTURA IQ'].notnull()].drop_duplicates(subset='FACTURA IQ', keep='first')
        
        cruce2 = pd.concat([cruce2,cruce0])
        
        if cartera_judicial.get() == "activado":
            
            "Se cruza contra cruce_agrup para traer los datos de valores de la liquidación reagrupados, para eliminar los conceptos duplicados"
            cruce2 = pd.merge(cruce2, cruce_agrup, left_on='FACTURA IQ', right_on='radicado_agrupado', how='left')
            
        else:
            "Se cruza contra cruce_agrup para traer los datos de valores de la liquidación reagrupados, para eliminar los conceptos duplicados"
            cruce2 = pd.merge(cruce2, cruce_agrup, left_on='ULTIMO_RADICADO', right_on='radicado_agrupado', how='left')
            
            "se deja el ultimo radicado como FACTURA IQ"
            cruce2 = cruce2.drop('FACTURA IQ', axis=1)
            cruce2 = cruce2.rename(columns={'ULTIMO_RADICADO':'FACTURA IQ'})
        
        # "Se ordena nuevamente por radicado y conteo de radicado"
        # cruce2 = cruce2.sort_values(by=['NIT','FACTURA','recuentoFacturaHR'], ascending=False)
        
        # "Se suma por el concepto, para que MAOS quede unificado"        
        # cruce2['MAOS_SUM'] = ''
        # suma = 0
        # x = 0
        # for x in range(len(cruce2)):
        #     try:
        #         if cruce2['recuentoFacturaHR'].iloc[x+1:x+2].values[0] == 1:
        #             i = x + 1
        #             j = 1
        #             flag = 0
        #             while cruce2['recuentoFacturaHR'].iloc[i:i+1].values[0] > 1:
        #                 if cruce2['RUBRO_OBJ'].iloc[i:i+1].values[0] == 'MAOS':
        #                     suma = suma + cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0]
        #                     i = i + 1
        #                     j = j + 1
        #             cruce2['MAOS_SUM'].iloc[x:x+1] = suma
        #         else:
        #             cruce2['MAOS_SUM'].iloc[x:x+1] = cruce2['MAOS_SUM'].iloc[x-1:x].values[0]
        #             # cruce2['MAOS_SUM'].iloc[x:x+1] = cruce2['Valor_glosado_Inicial'].iloc[x:x+1]
        #         suma = 0
        #         i = 0
        #     except:
        #         cruce2['MAOS_SUM'].iloc[x:x+1] = cruce2['MAOS_SUM'].iloc[x-1:x].values[0]
        
        # "Se deja nuevamente el orden de los rubros para continuar"
        # cruce2 = cruce2.sort_values(by='count', ascending=True)
        
        # !!!
        # !!!
        
        "Se cruza contra liquidacion"
        #cruce2 = pd.merge(cruce2, df_liq_riq_agrupado, left_on='FACTURA IQ', right_on='Numero_Radicado_Inicial', how='left')
        #cruce2 = pd.merge(cruce2, df_liq_riq_agrupado, left_on='ULTIMO_RADICADO', right_on='Numero_Radicado_Inicial', how='left')
    
        
        "Extraer info de aceptaciones RIQ-CIQ"
        cruce2['aceptacion1'] = cruce2['ValorAIPS']
        
        "Filtrar las aceptaciones por nit"
        df_ace = df_ace_p23
        df_ace['NIT'] = df_ace['NIT'].astype(str)
        df_ace = df_ace[df_ace['NIT']==str(df_cartera['NIT'].iloc[0:1].values[0])]#se debe cruzar con merge por si aplica para mas nit pendienteSI
        
        df_ace['FECHA DE CONCILIACION'] = pd.to_datetime(df_ace['FECHA DE CONCILIACION'], format='%d/%m/%Y',  errors='coerce')
       
        # # Filtra las filas donde la conversión resultó en NaT (Not a Time)
        # filas_error = df_ace[df_ace['FECHA DE CONCILIACION'].isna()]
        
        "Limpieza FACTURA de aceptaciones"
        df_ace['FACTURA'] = df_ace['FACTURA'].astype(str)
        df_ace['FACTURA'] = df_ace['FACTURA'].astype(str).str.upper()
        
        # Eliminar los caracteres innecesarios
        df_ace['FACTURA'] = df_ace['FACTURA'].str.replace('[.,\\-#:;/_ ]', '', regex=True)
        df_ace['FACTURA'] = np.where(df_ace['FACTURA'].str.isnumeric , df_ace['FACTURA'].str.lstrip('+-0'), df_ace['FACTURA'])
        
       
    
        df_cru = pd.merge(df_ace, df_hr_cartera, left_on=['NIT','FACTURA'], right_on=['ID RECLAMANTE','NUMERO FACTURA'], how='left')
        df_cru['F.LIQUIDACION'] = pd.to_datetime(df_cru['F.LIQUIDACION'], format='%Y/%m/%d')
        df_cru['validacion'] = np.where(~df_cru['F.LIQUIDACION'].notnull(),'nulo',
                                        np.where((df_cru['FECHA DE CONCILIACION'] <= df_cru['F.LIQUIDACION']) & 
                                                 (abs(df_cru['VALOR ACEPTADO'] - df_cru['VLR GLOSADO'])<=df_cru['VLR GLOSADO']*.004) | 
                                                 (abs(df_cru['VALOR INICIAL'] - df_cru['VLR GLOSADO'])<=df_cru['VLR GLOSADO']*.004),'s','n'))
        
        
        
        
        df_cru = df_cru.sort_values(by=['F.LIQUIDACION'], ascending=False)
                
        df_cru['validacion2'] = ''
        v = 0
        for x in range(len(df_cru)):
            v = df_cru[(df_cru['NIT'].iloc[x:x+1].values[0] == df_cru['NIT']) & (df_cru['FACTURA'].iloc[x:x+1].values[0] == df_cru['FACTURA']) & (df_cru['validacion'] == 's')]['FACTURA'].count()
            if v > 0:
                df_cru['validacion2'].iloc[x:x+1] = 'n'
            else:
                df_cru['validacion2'].iloc[x:x+1] = 's'
            v = 0
        
        df_cru = df_cru[df_cru['validacion']=='s']
        df_cru = df_cru.drop_duplicates(subset='FACTURA IQ', keep='first')
        
        df_cru = df_cru.loc[:,['FACTURA IQ','FECHA DE CONCILIACION','VALOR ACEPTADO', 'VALOR NO ACORDADO']]
        df_cru = df_cru.rename(columns={'FACTURA IQ':'RADICADO_ACEP','VALOR ACEPTADO':'aceptacion2'})
    
        cruce2 = pd.merge(cruce2, df_cru, left_on='FACTURA IQ', right_on='RADICADO_ACEP', how='left')
        # cruce2['aceptacion2'] = 0
    
        "Aceptaciones totales"        
        
        cant_liqTotal = len(cruce2)
        "Se realiza el conteo de 'DUPLICADOS' en hr por RADICADOS, para poder evaluar el saldo correspondiente contra el movimiento de la hr"
        cruce2['count3'] = np.arange(1,len(cruce2)+1)
        # a = len(cruce2)
        cruce2['recuentoRadHR'] = ''
        j = 0
        x = 1
        for x in range(len(cruce2)):
            if cruce2['count3'].iloc[x:x+1].values[0] == 1:
                cruce2['recuentoRadHR'].iloc[x:x+1] = 1        
            else:
                if cruce2['FACTURA IQ'].iloc[x:x+1].values[0] == cruce2['FACTURA IQ'].iloc[j-1:j].values[0]:
                    cruce2['recuentoRadHR'].iloc[x:x+1] = cruce2['recuentoRadHR'].iloc[x-1:x].values[0] + 1
                else:
                    cruce2['recuentoRadHR'].iloc[x:x+1] = 1
            j = j + 1
        
        # x = 0
        # for j in range(len(cruce2)):
        #     if cruce2['count3'].iloc[x:x+1].values[0] == 1:
        #         cruce2['recuentoRadHR'].iloc[x:x+1] = 's'      
        #     else:
        #         # if cruce2['FACTURA IQ'].iloc[x:x+1].values[0] == cruce2['FACTURA IQ'].iloc[j-1:j].values[0]:
        #         #     cruce2['recuentoRadHR'].iloc[x:x+1] = cruce2['recuentoRadHR'].iloc[x-1:x].values[0] + 1
        #         # else:
        #         cruce2['recuentoRadHR'].iloc[x:x+1] = 'n'
        #     x = x + 1
        
        
        "Traer los valores correspondientes a MAOS"
        cruce2['MAOS'] = 0
        vlr = 0
        # x = 1
        # less = 0
        for x in range(cant_liqTotal):
                i = x
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:
                    vlr = 0
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:  
                    q = cruce2[cruce2['FACTURA IQ'] == cruce2['FACTURA IQ'].iloc[x:x+1].values[0]]['FACTURA IQ'].count()
                    if q > 1:   
                        for rad in range(q):
                            try:
                                if cruce2['RUBRO_OBJ'].iloc[i:i+1].values[0] == 'MAOS' and cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0] > 0:
                                    vlr = cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0]                       
                            except:
                                vlr = 0
                            i = i + 1
                    else:
                        if cruce2['RUBRO_OBJ'].iloc[x:x+1].values[0] == 'MAOS' and cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0] > 0:
                            vlr = cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0]                       
                cruce2['MAOS'].iloc[x:x+1] = vlr   
                
        "Trar los valores correspondientes a FACTURACION"
        cruce2['FACTURACION'] = 0
        vlr = 0
        # x = 1
        # less = 0
        for x in range(cant_liqTotal):
                i = x
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:
                    vlr = 0
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:  
                    q = cruce2[cruce2['FACTURA IQ'] == cruce2['FACTURA IQ'].iloc[x:x+1].values[0]]['FACTURA IQ'].count()
                    if q > 1:   
                        for rad in range(q):
                            try:
                                if cruce2['RUBRO_OBJ'].iloc[i:i+1].values[0] == 'FACTURACION' and cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0] > 0:
                                    vlr = cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0]                                   
                            except:
                                vlr = 0
                            i = i + 1
                    else:
                        if cruce2['RUBRO_OBJ'].iloc[x:x+1].values[0] == 'FACTURACION' and cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0] > 0:
                            vlr = cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0]                     
                cruce2['FACTURACION'].iloc[x:x+1] = vlr        
        
        "Trar los valores correspondientes a TARIFAS"
        cruce2['TARIFAS'] = 0
        vlr = 0
        # x = 1
        # less = 0
        for x in range(cant_liqTotal):
                i = x
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:
                    vlr = 0
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:  
                    q = cruce2[cruce2['FACTURA IQ'] == cruce2['FACTURA IQ'].iloc[x:x+1].values[0]]['FACTURA IQ'].count()
                    if q > 1:   
                        for rad in range(q):
                            try:
                                if cruce2['RUBRO_OBJ'].iloc[i:i+1].values[0] == 'TARIFAS' and cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0] > 0:
                                    vlr = cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0]
                            except:
                                vlr = 0
                            i = i + 1
                    else:
                        if cruce2['RUBRO_OBJ'].iloc[x:x+1].values[0] == 'TARIFAS' and cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0] > 0:
                            vlr = cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0]              
                cruce2['TARIFAS'].iloc[x:x+1] = vlr
        
        
        "Trar los valores correspondientes a SOPORTES"
        cruce2['SOPORTES'] = 0
        vlr = 0
        # x = 1
        # less = 0
        for x in range(cant_liqTotal):
                i = x
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:
                    vlr = 0
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:  
                    q = cruce2[cruce2['FACTURA IQ'] == cruce2['FACTURA IQ'].iloc[x:x+1].values[0]]['FACTURA IQ'].count()
                    if q > 1:   
                        for rad in range(q):
                            try:
                                if cruce2['RUBRO_OBJ'].iloc[i:i+1].values[0] == 'SOPORTES' and cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0] > 0:
                                    vlr = cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0]
                            except:
                                vlr = 0
                            i = i + 1
                    else:
                        if cruce2['RUBRO_OBJ'].iloc[x:x+1].values[0] == 'SOPORTES' and cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0] > 0:
                            vlr = cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0]                      
                cruce2['SOPORTES'].iloc[x:x+1] = vlr
        
        "Trar los valores correspondientes a PERTINENCIA"
        cruce2['PERTINENCIA'] = 0
        vlr = 0
        # x = 1
        # less = 0
        for x in range(cant_liqTotal):
                i = x
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:
                    vlr = 0
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:  
                    q = cruce2[cruce2['FACTURA IQ'] == cruce2['FACTURA IQ'].iloc[x:x+1].values[0]]['FACTURA IQ'].count()
                    if q > 1:   
                        for rad in range(q):
                            try:
                                if cruce2['RUBRO_OBJ'].iloc[i:i+1].values[0] == 'PERTINENCIA' and cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0] > 0:
                                    vlr = cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0]
                            except:
                                vlr = 0
                            i = i + 1
                    else:
                        if cruce2['RUBRO_OBJ'].iloc[x:x+1].values[0] == 'PERTINENCIA' and cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0] > 0:
                            vlr = cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0]                    
                cruce2['PERTINENCIA'].iloc[x:x+1] = vlr
                
        "Trar los valores correspondientes a COBERTURA"
        cruce2['COBERTURA'] = 0
        vlr = 0
        # x = 0
        # less = 0
        for x in range(cant_liqTotal):
                i = x
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:
                    vlr = 0
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:  
                    q = cruce2[cruce2['FACTURA IQ'] == cruce2['FACTURA IQ'].iloc[x:x+1].values[0]]['FACTURA IQ'].count()
                    if q > 1:   
                        for rad in range(q):
                            try:
                                if cruce2['RUBRO_OBJ'].iloc[i:i+1].values[0] == 'COBERTURA' and cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0] > 0:
                                    vlr = cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0]
                            except:
                                vlr = 0
                            i = i + 1
                    else:
                        if cruce2['RUBRO_OBJ'].iloc[x:x+1].values[0] == 'COBERTURA' and cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0] > 0:
                            vlr = cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0]              
                cruce2['COBERTURA'].iloc[x:x+1] = vlr
        
                
        "Trar los valores correspondientes a HABILITACION"
        cruce2['HABILITACION'] = 0
        vlr = 0
        # x = 1
        # less = 0
        for x in range(cant_liqTotal):
                i = x
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:
                    vlr = 0
                if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:  
                    q = cruce2[cruce2['FACTURA IQ'] == cruce2['FACTURA IQ'].iloc[x:x+1].values[0]]['FACTURA IQ'].count()
                    if q > 1:   
                        for rad in range(q):
                            try:
                                if cruce2['RUBRO_OBJ'].iloc[i:i+1].values[0] == 'HABILITACION' and cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0] > 0:
                                    vlr = cruce2['Valor_glosado_Inicial'].iloc[i:i+1].values[0]
                            except:
                                vlr = 0
                            i = i + 1
                    else:
                        if cruce2['RUBRO_OBJ'].iloc[x:x+1].values[0] == 'HABILITACION' and cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0] > 0:
                            vlr = cruce2['Valor_glosado_Inicial'].iloc[x:x+1].values[0]                      
                cruce2['HABILITACION'].iloc[x:x+1] = vlr
                
        # !!!
        # !!!
        
        try:
            cruce2['MAOS'] = cruce2['MAOS'].astype(float)
            cruce2['FACTURACION'] = cruce2['FACTURACION'].astype(float)
            cruce2['TARIFAS'] = cruce2['TARIFAS'].astype(float)
            cruce2['SOPORTES'] = cruce2['SOPORTES'].astype(float)
            cruce2['COBERTURA'] = cruce2['COBERTURA'].astype(float)
            cruce2['PERTINENCIA'] = cruce2['PERTINENCIA'].astype(float)
            cruce2['HABILITACION'] = cruce2['HABILITACION'].astype(float)
        except Exception as e:
            tm.showerror("Error valores rubros:", str(e))
            
        # tm.showinfo("Cruce completado", "ok for2")
        ##############################***********************************************************************************************************
        ##############################
        "FIN CRUCE LIQUIDACION Y AJUSTE"
        ##############################
        ##############################
        
        ##############################***********************************************************************************************************
        ##############################
        "QUITAR NUEVAMENTE DUPLICIDADES"
        ##############################
        ##############################
        # cruce2 = cruce2.loc[:,['RADICADO_APERTURA','NIT', 'FACTURA','FACTURA_2', 'VALOR', 'Unnamed: 0', 'SUCURSAL', 'FACTURA IQ',
        #        'LOTE IQ', 'SINIESTRO', 'PLACA', 'NRO. POLIZA', 'CLASE VEHICULO',
        #        'NUMERO FACTURA', 'COD CIUDAD RECLAMACION FACTURA',
        #        'CIUDAD RECLAMACION FACTURA', 'VLR CONSTITUCION RVA', 'VLR RADICACION',
        #        'VLR APROBADO', 'VLR GLOSADO', 'AMPARO', 'TD RECLA', 'ID RECLAMANTE',
        #        'RECLAMANTE', 'ENT. EMBARGADA', 'DPTO RECLAMANTE', 'MUNC RECLAMANTE',
        #        'F.OCURRENCIA', 'COD MUNC OCURRENCIA', 'MUNC OCURRENCIA', 'TD VICTIMA',
        #        'DOC VICTIMA', 'VICTIMA','CONSECUTIVO',
        #        'F.FACTURA','fechas_pago_gt','ordenes_pago_gt',
        #        'F.AVISO', 'F.CREA FACTURA', 'F.ENT AUDITOR', 'F.CREA RESERVA',
        #        'DIAS F.AVISO A F.CREA RESER', 'ANALISTA LIQUIDADOR', 'F.LIQUIDACION',
        #        'ESTADO ACTUAL FACTURA', 'F.SOLICITUD DE PAGO', 'F.ORDEN PAGO',
        #        'NUMERO ORDEN DE PAGO', 'F.GIRO', 'DOCUMENTO DE PAGO ',
        #        'F. NOTIFICACION','gt', 'TOTAL APROBADO','gt',
        #        'OPERADOR ADMINISTRADOR', 'count', 'recuentoFacturaHR',
        #        'valida_Saldo_Rad', 'valida_Saldo_Glo', 'valida_Saldo_Apr',
        #        'SUMA APROBADO', 'primerFechaAviso','primerValorRadicado','Ultimo Valor Glosado', 'Num OPS agrupadas',
        #        'Fechas Giro agrupadas', 'RegistroCoincideConSaldoIPS',
        #        'NoCoincideConSaldoIPS', 'count2',
        #        'UnificarConceptosDeCoincidenciasSaldo', 'ValorAIPS', 'ValorSRTAIPS',
        #        'count3', 'recuentoRadHR', 'MAOS', 'FACTURACION', 'TARIFAS', 'SOPORTES',
        #        'COBERTURA', 'PERTINENCIA', 'HABILITACION','VALOR ADEUDADO REAL','RADICADOS_FACTURA','aceptacion1','aceptacion2','VALOR NO ACORDADO']]
        
        cruce3 = cruce2.groupby(['FACTURA IQ'])[['ValorAIPS','ValorSRTAIPS']].sum()
        
        if cartera_judicial.get() == "activado":
            
            cruce2= cruce2.drop_duplicates(['NIT','FACTURA','F.AVISO'], keep='first')
            
        else:
            cruce2= cruce2.drop_duplicates(['NIT','FACTURA'], keep='first')
        
        cruce2 = pd.merge(cruce2, cruce3, on='FACTURA IQ', how='left')
        # tm.showinfo("Cruce completado", "cruce 2 vs 3r")
        cruce2 = cruce2.rename(columns={'ValorAIPS_y':'Valor Aceptado IPS - liq',
                                        'ValorSRTAIPS_y':'Valor NoReclamado IPS'})
        
        cruce2 = cruce2.drop(['ValorAIPS_x','ValorSRTAIPS_x','USUARIO CREADOR FACTURA', 'USUARIO CREADOR RESERVA','Unnamed: 0',
                              'DIAS VENCI: F.AVISO A F.GIRO', 'F.AVISO CHEQUE','DIAS F.AVISO A F.CREA RESER', 'ANALISTA LIQUIDADOR',
                              'F.ENT AUDITOR','COD CIUDAD RECLAMACION FACTURA','SUCURSAL', 'LOTE IQ'], axis=1)
        
        ##############################****************************************************************************************************************
        ##############################
        "Cruce con la fuente DEVOLUCIONES"
        ##############################
        ##############################
        # df_dev.columns
        
        cruce2 = pd.merge(cruce2, df_dev, left_on='FACTURA IQ', right_on='NumeroRadicacion', how='left')
        
        ##############################****************************************************************************************************************
        ##############################
        "Cruce con la fuente NOTIFICACIONES"
        ##############################
        ##############################
        # df_not = df_not.drop(['F.AVISO'], axis=1)
        cruce2 = pd.merge(cruce2, df_not, left_on='FACTURA IQ', right_on='RADICADO', how='left')
        
        ##############################****************************************************************************************************************
        ##############################
        "Cruce con la fuente MANUALES"
        ##############################
        ##############################
        # df_man.columns
        cruce2 = pd.merge(cruce2, df_man, left_on='FACTURA IQ', right_on='NumeroRadicacion', how='left')
        
        ##############################****************************************************************************************************************
        ##############################
        "Cruce con la fuente ANULADOS"
        ##############################
        ##############################
        # df_anu.columns
        cruce2 = pd.merge(cruce2, df_anu, left_on='FACTURA IQ', right_on='NumeroRadicacion', how='left')
        
        cruce2['RadicadoAnulado'] = cruce2[['NumeroRadicacion','FACTURA IQ']].apply(lambda x: 's' if x['NumeroRadicacion'] == x['FACTURA IQ'] else 'n', axis=1)
        cruce2['RadicadoManual'] = cruce2[['NumeroRadicacion_y','FACTURA IQ']].apply(lambda x: 's' if x['NumeroRadicacion_y'] == x['FACTURA IQ'] else 'n', axis=1)
        
        cruce2 = cruce2.drop(['NumeroRadicacion_y','NumeroRadicacion','NumeroRadicacion_x','RADICADO'], axis=1)
        
        if cartera_judicial.get() == "activado":
            
            cruce2 = cruce2.drop_duplicates(['NIT','FACTURA','F.AVISO'], keep='first')
            
        else:
            cruce2 = cruce2.drop_duplicates(['NIT','FACTURA'], keep='first')
        
        ##############################
        ##############################
        "Observaciones"
        ##############################
        ##############################
        "Se crean las observaciones"
        if cartera_judicial.get() == "activado":
            
            cruce2['ESTADO ACTUAL FACTURA'] = cruce2['ESTADO ACTUAL FACTURA'].astype(str)
            
        else:
            # cruce2['ESTADO ACTUAL FACTURA'] = cruce2['ESTADO ACTUAL FACTURA'].astype(str)
            cruce2['ESTADO ACTUAL FACTURA'] = cruce2['ULTIMO_ESTADO'].astype(str)
            
        cruce2['Fecha_Aviso_vs_Hoy'] = abs(datetime.now() - cruce2['F.AVISO']).dt.days
        
        cruce2['OBSERVACIONES_MUNDIAL'] = cruce2.apply(lambda x:
                                                   'No Registra' if len(str(x['FACTURA IQ'])) < 5 else                                                                                  
                                                   'Pago Total' if x['valida_Saldo_Apr'] == 's' else
                                                   #'Valor Aceptado IPS' if x[''] else #valor aceptado total ips                                           
                                                   'Objecion Parcial' if (x['valida_Saldo_Glo'] == 's' or #objecion parcial
                                                   (x['VLR APROBADO'] + x['VLR GLOSADO']) == x['VALOR'] or 
                                                   abs((x['VLR APROBADO'] + x['VLR GLOSADO']) - x['VALOR']) <= x['VALOR'] * porcentual) and ~pd.Series(x['ESTADO ACTUAL FACTURA']).str.contains('COMUNICACI').any() else 
                                                   #'Devolucion' if pd.Series(x['ESTADO ACTUAL FACTURA']).str.contains('COMUNICACI').any() and #Devolucion                                           
                                                   #pd.Series(str(x['ESTADO ACTUAL FACTURA'])).str.contains('DEVOLUCI').any() and 
                                                   #abs((x['VLR RADICACION']) - x['VALOR']) <= x['VALOR'] * porcentual else 
                                                   'Objecion' if pd.Series(x['ESTADO ACTUAL FACTURA']).str.contains('COMUNICACI').any() and #Objecion
                                                   pd.Series(str(x['ESTADO ACTUAL FACTURA'])).str.contains('OBJECI').any() else
                                                   'Devolucion' if pd.Series(x['ESTADO ACTUAL FACTURA']).str.contains('COMUNICACI').any() #Devolucion
                                                   else
                                                   'En Terminos' if x['Fecha_Aviso_vs_Hoy'] <= 30 else  #En Terminos
                                                   'Diferencia en Saldos' if x['valida_Saldo_Apr'] == 'n' and x['valida_Saldo_Glo'] == 'n' and x['gt'] != 's' and x['valida_Saldo_Rad'] == 'n' else
                                                   'En Tramite' if abs((x['VLR RADICACION']) - x['VALOR']) <= x['VALOR'] * porcentual and x['ESTADO ACTUAL FACTURA'] in lista_estadosHR_proceso else
                                                   '',#No definido
                                                   axis=1)
        # tm.showinfo("Cruce completado", "observaciones")    
        cruce2['PrimerFecha_Aviso_vs_Hoy'] = abs(datetime.now() - pd.to_datetime(cruce2['primerFechaAviso'], format='%Y/%m/%d')).dt.days
        cruce2['FechaStro_vs_PrimerFecha_Aviso'] = abs(pd.to_datetime(cruce2['primerFechaAviso'], format='%Y/%m/%d') - pd.to_datetime(cruce2['F.OCURRENCIA'], format='%Y/%m/%d')).dt.days
            
        "Crear campo observaciones"
        mensaje_precripcion = 'FENÓMENO EXTINTIVO DE PRESCRIPCIÓN- ARTÍCULO 1081 DEL CÓDIGO DE COMERCIO'
        cruce2['OBSERVACIONES'] = cruce2[['OBSERVACIONES_MUNDIAL','PrimerFecha_Aviso_vs_Hoy','FechaStro_vs_PrimerFecha_Aviso']].apply(lambda x:
                                                                                                    mensaje_precripcion if x['FechaStro_vs_PrimerFecha_Aviso'] > 730 or 
                                                                                                    x['PrimerFecha_Aviso_vs_Hoy'] > 730 else '', axis=1)#si la fecha de aviso vs stro es superior a 730 dias, entonces prescrito 
        # tm.showinfo("Cruce completado", "ok prescripcion")
        "Crear campo mensaje"
        cruce2['MENSAJE'] = cruce2[['RadicadoManual']].apply(lambda x:'Radicado manual' if x['RadicadoManual']=='s' else '', axis=1)# +', '+ cruce2[['RadicadoAnulado']].apply(lambda x:'Radicado anulado' if x['RadicadoAnulado'] == 's' else '', axis=1)
        
        # for x in range(8769):
        #     if cruce2['recuentoRadHR'].iloc[x:x+1].values[0] == 1:
        
        ##############################
        ##############################
        "Creacion estructura carteras"
        ##############################
        ##############################
        "Clasificar el operador mediante el radicado"
        cruce2['FACTURA IQ'] = cruce2['FACTURA IQ'].astype(str)
        cruce2['OPERADOR'] = np.where(cruce2['FACTURA IQ'].str.contains('IQ') , 'IQ', np.where(cruce2['FACTURA IQ'].str.contains('MK'), 'MOK','NO CLASIFICA'))
        # tm.showinfo("Cruce completado", "ok operador")
        "Rubros de glosa"
        #cruce2['MAOS'] = ''
        # cruce['FACTURACION'] = ''
        # cruce['TARIFAS'] = ''
        # cruce['SOPORTES'] = ''
        # cruce['COBERTURA'] = ''
        # cruce['PERTINENCIA'] = ''
        # cruce['HABILITACION'] = ''
        
        "Pagos"
        # cruce2['VALOR_PAGO_MUNDIAL'] = cruce2[['SUMA APROBADO','VALOR']].apply(lambda x: 
        #                                                                x['SUMA APROBADO'] if x['SUMA APROBADO'] == x['VALOR'] or 
        #                                                                abs(x['VALOR'] - x['SUMA APROBADO']) <= x['VALOR'] * porcentual else 0,axis=1)
        # cruce2['VALOR_PAGO_MUNDIAL'] = cruce2[['SUMA APROBADO','gt','TOTAL APROBADO']].apply(lambda x: x['TOTAL APROBADO'] if x['gt'] == 's' else x['SUMA APROBADO'], axis = 1)#transporte
        "si esto no trae el valor real entonces la base es: cruce2['VALOR_PAGO_MUNDIAL'] = cruce2['TOTAL APROBADO'], y complementar la regla de ser necesario"
        
        if cartera_judicial.get() == "activado":
            cruce2['VALOR_PAGO_MUNDIAL'] = cruce2['VLR APROBADO']
            cruce2['NUMERO_DOCUMENTO_DE_PAGO'] = cruce2['DOCUMENTO DE PAGO ']
            cruce2['FECHA_PAGO'] = cruce2['F.GIRO']
        else:
            cruce2['VALOR_PAGO_MUNDIAL'] = cruce2.apply(lambda x: x['TOTAL APROBADO'] if x['VLR RADICACION'] > x['TOTAL APROBADO'] else x['VLR APROBADO'], axis=1)
            # cruce2['VALOR_PAGO_MUNDIAL'] = cruce2['SUMA APROBADO']
            # cruce2['NUMERO_DOCUMENTO_DE_PAGO'] = cruce2[['Num OPS agrupadas','VALOR_PAGO_MUNDIAL']].apply(lambda x: x['Num OPS agrupadas'] if x['VALOR_PAGO_MUNDIAL'] > 0 else 0,axis=1)
            # cruce2['FECHA_PAGO'] = cruce2[['Fechas Giro agrupadas','VALOR_PAGO_MUNDIAL']].apply(lambda x: x['Fechas Giro agrupadas'] if x['VALOR_PAGO_MUNDIAL'] > 0 else 0,axis=1)
            # cruce2['NUMERO_DOCUMENTO_DE_PAGO'] = cruce2[['Num OPS agrupadas','gt','ordenes_pago_gt']].apply(lambda x: x['ordenes_pago_gt'] if x['gt'] == 's' else x['Num OPS agrupadas'], axis = 1)#transporte
            cruce2['NUMERO_DOCUMENTO_DE_PAGO'] = cruce2['Num OPS agrupadas']
            # cruce2['FECHA_PAGO'] = cruce2[['Fechas Giro agrupadas','gt','fechas_pago_gt']].apply(lambda x: x['fechas_pago_gt'] if x['gt'] == 's' else x['Fechas Giro agrupadas'], axis = 1)#transporte
            cruce2['FECHA_PAGO'] = cruce2['Fechas Giro agrupadas']
        
        
        
        "Aceptaciones"
        cruce2['VALOR_ACEPTADO_IPS'] = 0
        
        "Objeciones parciales"
        cruce2['VALOR_OBJECION_PARCIAL_PRESCRITA'] = cruce2[['OBSERVACIONES_MUNDIAL','VLR GLOSADO','OBSERVACIONES']].apply(lambda x:
                                                                                   x['VLR GLOSADO'] if x['OBSERVACIONES_MUNDIAL'] == 'Objecion Parcial' and
                                                                                   x['OBSERVACIONES'] == mensaje_precripcion else 0, axis=1)
        # tm.showinfo("Cruce completado", "obj parciales")
        cruce2['VALOR_OBJECION_PARCIAL'] = cruce2[['VALOR_OBJECION_PARCIAL_PRESCRITA','MAOS','TARIFAS','SOPORTES','COBERTURA','PERTINENCIA','HABILITACION','FACTURACION','OBSERVACIONES_MUNDIAL','VLR GLOSADO']].apply(lambda x: x['VLR GLOSADO']
                                                                     if (x['TARIFAS'] + x['SOPORTES'] + x['COBERTURA'] + x['PERTINENCIA'] + x['HABILITACION'] + x['FACTURACION'] + x['MAOS']) == 0 and x['VALOR_OBJECION_PARCIAL_PRESCRITA'] == 0 else
                                                                     (x['TARIFAS'] + x['SOPORTES'] + x['COBERTURA'] + x['PERTINENCIA'] + x['HABILITACION'] + x['FACTURACION'] + x['MAOS']) if x['VALOR_OBJECION_PARCIAL_PRESCRITA'] == 0 else 0, axis=1)
        cruce2['VALOR_OBJECION_PARCIAL'] = cruce2['VALOR_OBJECION_PARCIAL'].fillna(0).astype(float)
        # aa = cruce2[cruce2['FACTURA']=='FE53981']
        "Objeciones/Devoluciones"
        cruce2['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'] = cruce2[['OBSERVACIONES_MUNDIAL','VALOR','OBSERVACIONES']].apply(lambda x:
                                                                                   x['VALOR'] if x['OBSERVACIONES_MUNDIAL'] == 'Devolucion' or
                                                                                   x['OBSERVACIONES_MUNDIAL'] == 'Objecion' and
                                                                                   x['OBSERVACIONES'] == mensaje_precripcion else 0, axis=1)
            
        cruce2['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'] = cruce2.apply(lambda x: 0 if x['OBSERVACIONES'] != mensaje_precripcion else x['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'], axis=1)
        cruce2['VALOR_OBJECION_PARCIAL_PRESCRITA'] = cruce2.apply(lambda x: 0 if x['OBSERVACIONES'] != mensaje_precripcion else x['VALOR_OBJECION_PARCIAL_PRESCRITA'], axis=1)
        
        cruce2['CAUSAL_OBJECION'] = cruce2[['MotivoCausalDevolucionObjecion','OBSERVACIONES_MUNDIAL','OBSERVACIONES']].apply(lambda x: x['MotivoCausalDevolucionObjecion'] if 
                                                                                   x['OBSERVACIONES_MUNDIAL'] == 'Devolucion' or
                                                                                   x['OBSERVACIONES_MUNDIAL'] == 'Objecion' else '', axis=1)
        
        cruce2['VALOR_OBJECION_DEVOLUCION'] = cruce2[['OBSERVACIONES_MUNDIAL','VALOR','OBSERVACIONES']].apply(lambda x:
                                                                                   x['VALOR'] if x['OBSERVACIONES_MUNDIAL'] == 'Devolucion' or
                                                                                   x['OBSERVACIONES_MUNDIAL'] == 'Objecion' else 0, axis=1)
        
        "En terminos/revision/novedades"
        cruce2['EN_TERMINOS_O_REVISION'] = cruce2[['OBSERVACIONES_MUNDIAL','VALOR']].apply(lambda x:
                                                                                   x['VALOR'] if x['OBSERVACIONES_MUNDIAL'] == 'En Terminos' else 0, axis=1)
        
        cruce2['NO_REGISTRADAS'] = cruce2[['OBSERVACIONES_MUNDIAL','VALOR']].apply(lambda x:
                                                                                   x['VALOR'] if x['OBSERVACIONES_MUNDIAL'] == 'No Registra' else 0, axis=1)
        
        cruce2['DIFERENCIA_EN_SALDOS'] = cruce2[['OBSERVACIONES_MUNDIAL','VALOR']].apply(lambda x:
                                                                                   x['VALOR'] if x['OBSERVACIONES_MUNDIAL'] == 'Diferencia en Saldos' else 0, axis=1)
        # tm.showinfo("Cruce completado", "ok demas campos")
        # "Observaciones finales"
        # cruce2['OBSERVACIONES_MUNDIAL'] = ''
        # cruce2['OBSERVACIONES'] = ''
        
        # "Mensaje"
        # cruce2['MENSAJE'] = ''
        # cruce2.info()
        cruce2['VALOR_RADICADO_FACTURA'] = cruce2['primerValorRadicado']
        
        "Notificacion"
        cruce2['CONSECUTIVO_y'] = cruce2['CONSECUTIVO_y'].fillna('null')
        # cruce2['NUMERO_DE_COMUNICADO'] = cruce2[['CONSECUTIVO_y','CONSECUTIVO_x']].apply(lambda x:
        #                                                                            x['CONSECUTIVO_y'] if x['CONSECUTIVO_y'] != 'null' else x['CONSECUTIVO_x'], axis=1)
        cruce2['NUMERO_DE_COMUNICADO'] = cruce2['CONSECUTIVO_y']
        
        # tm.showinfo("Cruce completado", "consec y")
        cruce2['GUIA_DE_ENVIO'] = cruce2['GUIA']
        cruce2['F.NOTIFICACION'] = cruce2['F.NOTIFICACION'].fillna('null')
        cruce2['FECHA_DE_ENVIO'] = cruce2[['F.NOTIFICACION','F. NOTIFICACION']].apply(lambda x:
                                                                                   x['F.NOTIFICACION'] if x['F.NOTIFICACION'] != 'null' else x['F. NOTIFICACION'], axis=1)
        # tm.showinfo("Cruce completado", "not")
        cruce2['EMPRESA_POSTAL'] = ''
        cruce2['CORREO_ELECTRONICO'] = cruce2['CORREO']
        
        if cartera_judicial.get() == "activado":
            cruce2['SALDO_REGISTRADO_IPS'] = cruce2['VLR RADICACION']
            cruce2['SALDO_IPS'] = cruce2['VALOR']
            cruce2['SALDO_REGISTRADO_IPS_HR'] = cruce2.apply(lambda x: x['VLR GLOSADO'] if x['VLR GLOSADO'] > 0 else x['VLR RADICACION'], axis=1)
        else:
            cruce2['SALDO_REGISTRADO_IPS'] = cruce2['VALOR']
        
        "Nombre IPS, esto se extrae de HR"
        cruce2['NOMBRE_IPS'] = ''
        
        "se elimina el valor glosado del registro que coincide saldo, y se reemplaza por el ultimo movimiento"
        if cartera_judicial.get() == "activado":
            cruce2['VALOR_OBJECION_PARCIAL'] = cruce2['VLR GLOSADO']
        else:
            cruce2['VLR GLOSADO'] = cruce2['Ultimo Valor Glosado']
            cruce2['VALOR_OBJECION_PARCIAL'] = cruce2['Ultimo Valor Glosado'].astype(float)
        
        if cartera_judicial.get() == "activado":
            cruce2 = cruce2.loc[:,[
                'OPERADOR',
                'FACTURA IQ',
                'RADICADOS_FACTURA',
                'RADICADO_APERTURA',
                'ESTADO ACTUAL FACTURA',
                'F.LIQUIDACION',
                'NIT',
                'FACTURA',
                'FACTURA_2',
                'SINIESTRO',
                'PLACA',
                'TD VICTIMA',
                'DOC VICTIMA',
                'VICTIMA',
                'primerFechaAviso',
                'F.AVISO',
                'F.OCURRENCIA',
                'VALOR_RADICADO_FACTURA',
                'SALDO_REGISTRADO_IPS',
                'SALDO_IPS',
                'SALDO_REGISTRADO_IPS_HR',
                'MAOS',
                'FACTURACION',
                'TARIFAS',
                'SOPORTES',
                'COBERTURA',
                'PERTINENCIA',
                'HABILITACION',
                'VALOR_OBJECION_PARCIAL',
                'VALOR_OBJECION_PARCIAL_PRESCRITA',
                'VALOR_ACEPTADO_IPS',
                'VALOR NO ACORDADO',
                'aceptacion1','aceptacion2',
                'CAUSAL_OBJECION',
                'VALOR_OBJECION_DEVOLUCION',
                'VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA',
                'EN_TERMINOS_O_REVISION',
                'NO_REGISTRADAS',
                'DIFERENCIA_EN_SALDOS',
                'VALOR_PAGO_MUNDIAL',
                'NUMERO_DOCUMENTO_DE_PAGO',
                'FECHA_PAGO',
                'VALOR ADEUDADO REAL',
                'OBSERVACIONES_MUNDIAL',
                'OBSERVACIONES',
                'MENSAJE',
                'NUMERO_DE_COMUNICADO',
                'GUIA_DE_ENVIO',
                'FECHA_DE_ENVIO',
                'EMPRESA_POSTAL',
                'CORREO_ELECTRONICO',
                'NOMBRE_IPS',
                'gt',
                'VLR APROBADO',
                'DOCUMENTO DE PAGO ',
                'F.GIRO',
                ]]
        else:
            cruce2 = cruce2.loc[:,[
                'OPERADOR',
                'FACTURA IQ',
                'RADICADOS_FACTURA',
                'RADICADO_APERTURA',
                'ESTADO ACTUAL FACTURA',
                'F.LIQUIDACION',
                'NIT',
                'FACTURA',
                'FACTURA_2',
                'SINIESTRO',
                'PLACA',
                'TD VICTIMA',
                'DOC VICTIMA',
                'VICTIMA',
                'primerFechaAviso',
                'F.AVISO',
                'F.OCURRENCIA',
                'VALOR_RADICADO_FACTURA',
                'SALDO_REGISTRADO_IPS',
                # 'SALDO_IPS',
                # 'SALDO_REGISTRADO_IPS_HR',
                'MAOS',
                'FACTURACION',
                'TARIFAS',
                'SOPORTES',
                'COBERTURA',
                'PERTINENCIA',
                'HABILITACION',
                'VALOR_OBJECION_PARCIAL',
                'VALOR_OBJECION_PARCIAL_PRESCRITA',
                'VALOR_ACEPTADO_IPS',
                'VALOR NO ACORDADO',
                'aceptacion1','aceptacion2',
                'CAUSAL_OBJECION',
                'VALOR_OBJECION_DEVOLUCION',
                'VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA',
                'EN_TERMINOS_O_REVISION',
                'NO_REGISTRADAS',
                'DIFERENCIA_EN_SALDOS',
                'VALOR_PAGO_MUNDIAL',
                'NUMERO_DOCUMENTO_DE_PAGO',
                'FECHA_PAGO',
                'VALOR ADEUDADO REAL',
                'OBSERVACIONES_MUNDIAL',
                'OBSERVACIONES',
                'MENSAJE',
                'NUMERO_DE_COMUNICADO',
                'GUIA_DE_ENVIO',
                'FECHA_DE_ENVIO',
                'EMPRESA_POSTAL',
                'CORREO_ELECTRONICO',
                'NOMBRE_IPS',
                'gt',
                'VLR APROBADO',
                'DOCUMENTO DE PAGO ',
                'F.GIRO',
                ]]
        #########################*******************************************************************************************************************
        #########################
        "Jerarquías"
        #########################
        #########################*******************************************************************************************************************
        cruce4 = cruce2
        #======================================================================
        # Codigo Anterior Investigaciones
        # df_inv['Id_lesionado'] = df_inv['Id_lesionado'].astype(str)
        # df_inv['Id_lesionado'] = np.where(df_inv['Id_lesionado'].str.isnumeric , df_inv['Id_lesionado'].str.lstrip('+-0'), df_inv['Id_lesionado'])
        # df_inv['Id_lesionado'] = df_inv['Id_lesionado'].astype(str).fillna('-').replace('.0','', regex=True)
        
        # cruce4['DOC VICTIMA'] = cruce4['DOC VICTIMA'].astype(str)
        # cruce4['DOC VICTIMA'] = np.where(cruce4['DOC VICTIMA'].str.isnumeric , cruce4['DOC VICTIMA'].str.lstrip('+-0'), cruce4['DOC VICTIMA'])
        # cruce4['DOC VICTIMA'] = cruce4['DOC VICTIMA'].astype(str).fillna('na').replace('.0','', regex=True)
        #======================================================================
        # df_inv.info()
        cruce4['F.OCURRENCIA'] = pd.to_datetime(cruce4['F.OCURRENCIA'], format='%Y/%m/%d', errors='coerce')
        cruce4 = pd.merge(cruce4,df_inv, left_on=['PLACA','F.OCURRENCIA'], right_on=['Placa','F.accidente'], how='left')
        # cruce4.info()
        #======================================================================
        # Codigo Anterior Investigaciones
        
        # cruce4 = pd.merge(cruce4,df_inv, left_on=['PLACA','DOC VICTIMA'], right_on=['Placa','Id_lesionado'], how='left') # Cruce4 con Investigaciones
        #======================================================================
        # ???
        # ???
        #########################################################################################################
      
     
        
        cruce4 = pd.merge(cruce4,df_jur, left_on=['NIT','FACTURA'], right_on=['NIT','FacturaProceso'], how='left')
        
        cruce4['Tiene Investigación'] = cruce4.apply(lambda x: 'Si' if x['Placa'] == x['PLACA'] else '', axis=1)
        cruce4['Cartera Jurídica'] = cruce4.apply(lambda x: 'Si' if x['FacturaProceso'] == x['FACTURA'] else '', axis=1)
        
        cruce4 = cruce4.drop(['Placa','FacturaProceso','Id_lesionado'], axis=1)
        
        cruce4['primerFechaAviso'] = pd.to_datetime(cruce4['primerFechaAviso'], format='%Y/%m/%d').dt.date
        
        try:
            "ratificaciones"
            prefijos_ratificacion = ('CIQ','RIQ','CMK','RMK')
            
            "filtrar nombre de reclamante"
            df_nom = df_hr_cartera.loc[:,['ID RECLAMANTE','RECLAMANTE']]
            df_nom = df_nom[df_nom['RECLAMANTE'].notnull()]
            df_nom = df_nom.drop_duplicates()
            
            "se cruza el nombre ips"
            cruce4 = pd.merge(cruce4, df_nom, left_on='NIT', right_on='ID RECLAMANTE', how='left')
            cruce4['NOMBRE_IPS'] = cruce4['RECLAMANTE']
            cruce4 = cruce4.drop(['ID RECLAMANTE','RECLAMANTE'], axis=1)
            
            "Se limpian las aceptaciones 1 y 2"
            cruce4['aceptacion1'] = cruce4['aceptacion1'].fillna(0).astype(float)
            cruce4['aceptacion2'] = cruce4['aceptacion2'].fillna(0).astype(float)
            
            "Ajustar el valor de las obecjones parciales según lo anterior"
            #contexto idea, si tiene una diferencia en saldos, aplica
            
            "Se actualiza el valor aceptado IPS"
            cruce4['VALOR_ACEPTADO_IPS'] = cruce4.apply(lambda x: x['aceptacion1'] if abs(x['aceptacion1'] - x['aceptacion2']) <= x['aceptacion2'] * 0.001 and x['aceptacion1'] > 0 else x['aceptacion1'] + x['aceptacion2'], axis=1)
            # cruce4['VALOR_ACEPTADO_IPS'] = (cruce4['aceptacion1'] + cruce4['aceptacion2'])
            
            "se cruzan las aceptaciones TOTALES de la operación"
            cruce4 = pd.merge(cruce4, df_ace_total, on='FACTURA IQ', how='left')
            
            cruce4['VALOR_ACEPTADO_IPS'] = cruce4.apply(lambda x: x['Valor Aceptado Ips'] if x['Valor Aceptado Ips'] > 0 else x['VALOR_ACEPTADO_IPS'], axis=1)
            
            "Ajustar el valor adeudado real restando las aceptaciones 1 y 2"
            cruce4['VALOR ADEUDADO REAL'] = abs(cruce4['VALOR ADEUDADO REAL'] - cruce4['VALOR_ACEPTADO_IPS'])#Restar las aceptaciones pendienteNO
            
            # tm.showinfo("Cruce completado", "cruce4")
            cruce4['OBSERVACIONES_MUNDIAL'] = ''
            
            "transporte"
            cruce4['validar'] = ''
            
            cruce4 = cruce4.drop(['aceptacion1','aceptacion2'], axis=1)
            cruce4['iteracion'] = 0 
            
        except Exception as e:
             tm.showerror("Error preliminar for:", str(e))
        
        
        
        # !!!
        try:#3
            for x in range(len(cruce4)):
                
                "si contiene error, es que solo tiene un registro en hr y se encuentra en error y esto lo soluciona es el operador"
                if cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].values[0] in lista_estadosHR_err:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Error en HR'#Ob
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Esta factura solo cuenta con un registro en HR y se encuentra en error, por lo que no cuenta con valores aprobados u objetados. Notificar al operador para su reproceso)'#el saldo solicitado es menor al de hr real
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 0
                
                "version pre de valor pago total, dejar como objecion parcial"
                "nuevo re ajuste, valores que tienen aceptaciones, objecion parcial y pagos inferiores al saldo solicitado por el prestador 1_1"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] > 0 and (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]) <= cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] * porcentual_especial) and abs(cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0]) <= cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] * porcentual_especial:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    # cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    # cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    # cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    # cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'#Ob
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Objeción parcial, no novedad, validar = no/opcional)'#el saldo solicitado es menor al de hr real
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 1
                    
                "VALOR PAGO MUNDIAL 1"
                if (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0]) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]*porcentual)) :
                    #cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Pago Total'
                    if cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                        cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Está con la tolerancia del %' + str(porcentual) + ', validar = si/opcional)'
                        cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 2
                
                "VALOR PAGO MUNDIAL 2"
                if cruce4['iteracion'].iloc[x:x+1].values[0] == 2 and cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] >= cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion:                       
                        if cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] < cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]:
                            cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                        else:
                            cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]
                    else:
                        if cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] < cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]:
                            cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                        else:
                            cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Pasa por la iteracion 211 no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 211
                    
                "VALOR PAGO MUNDIAL 3"
                if cruce4['iteracion'].iloc[x:x+1].values[0] == 2 and cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0 and (cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] + cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0]) == cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion:                       
                        if cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] < cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]:
                            cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                        else:
                            cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]
                    else:
                        if cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] < cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]:
                            cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                        else:
                            cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Pasa por la iteracion 212 no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 212
            
                "VALOR ACEPTADO IPS 1"
                if (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0]) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]*porcentual)) :
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    #cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Valor Aceptado IPS'
                    if cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                        cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Está con la tolerancia del %' + str(porcentual) + ', validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 3
                    
                "VALOR ACEPTADO IPS 2"
                if cruce4['iteracion'].iloc[x:x+1].values[0] == 3 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] > 0:
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    # cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    # cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    # cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # #cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion:                       
                        cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]
                    else:
                        cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] 
                    # cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    # cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Valor Aceptado IPS'
                    # if cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Se reajusta valores, se deja el valor adeudado real como obj parcial)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 311
            
            
                "VALOR OBJECION PARCIAL PRESCRITA"
                if (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - (cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] + cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]*porcentual)) and cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] > 0:
                    #cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    #cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    #cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    if cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                        cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Está con la tolerancia del %' + str(porcentual) + ', validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 4
                
                if (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] + cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0]) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]*porcentual)) and cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] > 0:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] + cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    #cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    #cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    if cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                        cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Está con la tolerancia del %' + str(porcentual) + ', validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 5
                    
                if (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0]) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]*porcentual)) and cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] > 0 :
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    #cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    if cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                        cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Está con la tolerancia del %' + str(porcentual) + ', validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 6
                    
                "Validacion para rectificar prescripcion parcial"
                if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 :
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0]
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    #cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 7
                    
                if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion and cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] > 0 and cruce4['iteracion'].iloc[x:x+1].values[0] not in reajuste_iter_2:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    #cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 8
                    
                    
                "valor objecion parcial"
                if abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - abs(cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] * porcentual) and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] > 0:
                    #cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    #cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    #cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    if cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                        cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Está con la tolerancia del %' + str(porcentual) + ', validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 9
                    
                "VALOR OBJECION PARCIAL 2"
                if cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] != 0 and (cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0]) < cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] and (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - (cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] * porcentual)) and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] > 0:
                    #cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # if cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] == 0:
                    #     cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    #cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Está con la tolerancia del %' + str(porcentual) + ', se ajustan valores, validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 10
                  
                "VALOR OBJECION PARCIAL 2.1"
                if cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] != 0 and (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - (cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] * porcentual)) and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] > 0:
                    diferencia_a_retirar_de_rubros = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    flag_r = False
                    #cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0 #si se deja, aparece diferencia en saldos
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # if cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] == 0:
                    #     cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0]
                    if diferencia_a_retirar_de_rubros > 0 and cruce4['HABILITACION'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['HABILITACION'].iloc[x:x+1].values[0] = cruce4['HABILITACION'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['PERTINENCIA'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = cruce4['PERTINENCIA'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['COBERTURA'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['COBERTURA'].iloc[x:x+1].values[0] = cruce4['COBERTURA'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['FACTURACION'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['FACTURACION'].iloc[x:x+1].values[0] = cruce4['FACTURACION'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    # elif diferencia_a_retirar_de_rubros > 0 and cruce4['MAOS'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                    #     cruce4['MAOS'].iloc[x:x+1].values[0] = cruce4['MAOS'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                    #     flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['TARIFAS'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['TARIFAS'].iloc[x:x+1].values[0] = cruce4['TARIFAS'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    #cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Está con la tolerancia del %' + str(porcentual) + ', se ajustan valores, validar = no/opcional)'
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = '10_2'
                    
        # !!! 
                
                "VALOR OBJECION PARCIAL 3"
                if cartera_judicial_activa == False and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] == 0 and (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0]) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] * porcentual)) and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] > 0:
                    #cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # if cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] == 0:
                    #     cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Pago Total'
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = '10_1'
                    
                if (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - (cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]*porcentual)) and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] < cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    #cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    #cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    if cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                        cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Está con la tolerancia del %' + str(porcentual) + ', validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 11
                    
                if cartera_judicial_activa == False and (abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0]) <= (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]*porcentual)) and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and ~cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].str.contains('COMUNICACI').any():
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    #cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    #cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    #cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    #cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    #cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 12
                    
                            
                "VALOR OBJECION TOTAL O DEVOLUCION PRESCRITA"
                if cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] > 0:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    concepto = ''
                    if cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].str.contains('COMUNICACI').any() and cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].str.contains('OBJECI').any() or cruce4['CAUSAL_OBJECION'].iloc[x:x+1].str.contains('OBJECI').any():
                        concepto = 'Objecion'
                    else:
                        concepto = 'Devolucion'
                    
                    if cruce4['CAUSAL_OBJECION'].iloc[x:x+1].str.contains('OBJECI').any():
                        concepto = 'Objecion'
                    if cruce4['CAUSAL_OBJECION'].iloc[x:x+1].str.contains('DEVOL').any():
                        concepto = 'Devolucion'
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = concepto
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 13
            
            
                "VALOR OBJECION TOTAL O DEVOLUCION"
                if cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] > 0:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    #cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    #cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    concepto = ''
                    if cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].str.contains('COMUNICACI').any() and cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].str.contains('OBJECI').any() or cruce4['CAUSAL_OBJECION'].iloc[x:x+1].str.contains('OBJECI').any():
                        concepto = 'Objecion'
                    else:
                        concepto = 'Devolucion'
                        
                    if cruce4['CAUSAL_OBJECION'].iloc[x:x+1].str.contains('OBJECI').any():
                        concepto = 'Objecion'
                    if cruce4['CAUSAL_OBJECION'].iloc[x:x+1].str.contains('DEVOL').any():
                        concepto = 'Devolucion'
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = concepto
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 14
                    
            
                "EN TERMINOS O REVISION"
                if cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] > 0:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    #cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'En Terminos'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 15
            
                "NO REGISTRADAS"
                if cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] > 0 and cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].values[0] not in lista_estadosHR_err:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0
                    #cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'No Registra'
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = ''
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 16
                
                if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion and cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] < cruce4['VALOR_RADICADO_FACTURA'].iloc[x:x+1].values[0] and cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and abs((cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] + cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]) - cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]) <= cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] * porcentual:
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 17
                    
                "SE AJUSTAN LOS VALORES QUE NO CRUZAN EN VALIDACIONES ANTERIORES, SE DEJAN COMO PRESCRIPCION"###OBJECION PARCIAL
                if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion and cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] < cruce4['VALOR_RADICADO_FACTURA'].iloc[x:x+1].values[0] and cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '':
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 171
                    
                "SE AJUSTAN LOS VALORES QUE NO CRUZAN EN VALIDACIONES ANTERIORES, SE DEJAN COMO PRESCRIPCION"###DEVOLUCION
                if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion and cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] == cruce4['VALOR_RADICADO_FACTURA'].iloc[x:x+1].values[0] and cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '':
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Devolucion'
                    # cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 18
            
                
                
                
            "Se crea nuevo ciclo for, muy necesario para contrarestar las diferencias en saldos"   
            for x in range(len(cruce4)):

                "nuevo re ajuste, valores que tienen aceptaciones, objecion parcial y pagos inferiores al saldo solicitado por el prestador"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and (cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] == cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0]) and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] == 0:
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Pago Total'#Pago Total 2
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Saldo solicitado no corresponde a saldo actual en HR, se dejan los datos recientes, validar = si/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 19
                
                # "nuevo re ajuste, valores que tienen aceptaciones, objecion parcial y pagos inferiores al saldo solicitado por el prestador 2"
                # if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0  and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] == cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]:
                #     cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                #     cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                #     cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                #     cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                #     cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                #     cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                #     cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                #     cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                #     cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                #     # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                #     cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                #     # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                #     # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                #     # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                #     # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                #     # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                #     # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                #     # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                #     # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                #     cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'#Ob_adeudado
                #     cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Saldo solicitado no corresponde a saldo actual en HR, se dejan los datos recientes)'
                    
                "nuevo re ajuste, valores que tienen aceptaciones, objecion parcial y pagos inferiores al saldo solicitado por el prestador 3"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and ((cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0]) - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0]) > cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] >= cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    diferencia_a_retirar_de_rubros = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] - cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                    flag_r = False
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0#abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                    if diferencia_a_retirar_de_rubros > 0 and cruce4['HABILITACION'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['HABILITACION'].iloc[x:x+1].values[0] = cruce4['HABILITACION'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['PERTINENCIA'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = cruce4['PERTINENCIA'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['COBERTURA'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['COBERTURA'].iloc[x:x+1].values[0] = cruce4['COBERTURA'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['FACTURACION'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['FACTURACION'].iloc[x:x+1].values[0] = cruce4['FACTURACION'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    # elif diferencia_a_retirar_de_rubros > 0 and cruce4['MAOS'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                    #     cruce4['MAOS'].iloc[x:x+1].values[0] = cruce4['MAOS'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                    #     flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['TARIFAS'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['TARIFAS'].iloc[x:x+1].values[0] = cruce4['TARIFAS'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'#Ob
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Objeción parcial, el saldo que solicita la ips es inferior, se ajusta la objeción parcial y los rubros de objeción con el valor saldo IPS, validar = no/opcional)'#el saldo solicitado es menor al de hr real
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 21
                   
                "nuevo re ajuste, valores que tienen aceptaciones, objecion parcial y pagos inferiores al saldo solicitado por el prestador 3.1"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] > cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] != cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'#Ob
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Objeción parcial, el valor solicitado es menor al adeudado y la obj parcial es menor al saldo solicitado, validar = si/opcional)'#el saldo solicitado es menor al de hr real
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 22
                    
                if cruce4['iteracion'].iloc[x:x+1].values[0] == 22 and cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] != cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] and cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = cruce4['F.GIRO'].iloc[x:x+1].values[0]
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = cruce4['DOCUMENTO DE PAGO '].iloc[x:x+1].values[0]
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = cruce4['VLR APROBADO'].iloc[x:x+1].values[0]
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'#Ob
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(REVISIÓN ITERACION 221)'#el saldo solicitado es menor al de hr real
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 221
                    
                "nuevo re ajuste, valores que tienen aceptaciones, objecion parcial y pagos inferiores al saldo solicitado por el prestador 3.2"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and (cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] + cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0]) == 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] != cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'#Ob
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Objeción parcial, pero con diferencias en saldo, validar = no/opcional)'#el saldo solicitado es menor al de hr real
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 23
                    
                "nuevo re ajuste, valores que tienen aceptaciones, objecion parcial y pagos inferiores al saldo solicitado por el prestador 3.3"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] == cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]:
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0#abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                    # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'#Ob
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Objeción parcial, el saldo registrado por la IPS es realmente lo que se adeuda, pero el último movimiento en HR no concuerda con el saldo solicitado, validar movimientos en HR, se ajusta al saldo IPS solicitado, validar = si/opcional)'#el saldo solicitado es menor al de hr real
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 24
                    
                "nuevo re ajuste, valores que tienen aceptaciones, objecion parcial y pagos inferiores al saldo solicitado por el prestador 3.4"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] == cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] and (cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0]) > cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'#Ob
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Objeción parcial, la objeción parcial es igual a lo adeudado, es lo que realmente se debe, validar = no/opcional)'#el saldo solicitado es menor al de hr real
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 25
                
                "nuevo re ajuste, valores que tienen aceptaciones, objecion parcial y pagos inferiores al saldo solicitado por el prestador 4"
                "Se resta el saldo menos los campos para obtener la variable negativa, si es asi, se aplica condicion para dejar un valor menos que condicion posterior"                    
                diferencia_en_saldos_ref = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0]    
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] > 0 and diferencia_en_saldos_ref < 0:
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'#objecion negativos
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 26
                    
                "nuevo re ajuste, valor pagado es igual al saldo registrad ips"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and (cruce4['VALOR_RADICADO_FACTURA'].iloc[x:x+1].values[0] == cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0]) and cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] > 0 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] == 0:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    # cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                    # cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Pago Total'#Pago Total3
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Diferencia en Saldos'
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Saldo solicitado no corresponde a saldo actual en HR, pero la factura ya se encuentra pagada totalmente, aunque presenta diferencia en saldos, validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 27
                
                "PREVIA DIFERENCIA EN SALDOS"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and (cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] + cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]) == cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] and cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].values[0] not in lista_estadosHR_proceso:
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion:                       
                        cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]
                    else:
                        cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]
                    # cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0])
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Objeción Parcial, no trae detalle objeción parcial)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 271
                    
                "DIFERENCIA EN SALDOS, y se descartan los estados de hr que se encuentren en procesos"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].values[0] not in lista_estadosHR_proceso:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Diferencia en saldos'
                    if cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] == 0:
                        cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Saldo solicitado no corresponde a saldo actual en HR, pero la factura ya se encuentra pagada totalmente, aunque presenta diferencia en saldos)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 28
                    
                if cruce4['iteracion'].iloc[x:x+1].values[0] == 28 and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] > 0:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0]
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial'
                    # if cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] == 0:
                        # cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Saldo solicitado no corresponde a saldo actual en HR, pero la factura ya se encuentra pagada totalmente, aunque presenta diferencia en saldos)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 281
                    
                    #==============================================================
                    # Modificación Iteración 281 
                    #==============================================================
                
                "Factura presenta doble amparo"
                if (cruce4['iteracion'].iloc[x:x+1].values[0] == 281 
                    and cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0] > 0 
                    and cruce4['gt'].iloc[x:x+1].values[0] == 's'):
                    
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0]
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial / Pago Total'
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + ' (Por favor confirmar pagos, la factura presenta doble amparo, validar = si )) '
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 282
        
                    #==============================================================
                    # Modificación Iteración 281 
                    #==============================================================
                    
                    
                "Se validan los estados actuales de las facturas para clasificarlas como en proceso"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == '' and cruce4['ESTADO ACTUAL FACTURA'].iloc[x:x+1].values[0] in lista_estadosHR_proceso:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0 #abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Facturas en Proceso'
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Esta factura se encuentra en trámite según su estado actual de HR, validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 29 
              
                ####################################################################################
                "re ajuste (1) para las iteraciones anteriores para que no tengan diferencias en saldo"
                if cruce4['iteracion'].iloc[x:x+1].values[0] in reajuste_iter_1 and cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0: #and (cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] + cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0]) > cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    diferencia_a_retirar_de_rubros = cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0]
                    flag_r = False
                    # cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    # cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion:
                        cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    else:
                        cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = (cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    if diferencia_a_retirar_de_rubros > 0 and cruce4['HABILITACION'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:
                        cruce4['HABILITACION'].iloc[x:x+1].values[0] = cruce4['HABILITACION'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['PERTINENCIA'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = cruce4['PERTINENCIA'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['COBERTURA'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['COBERTURA'].iloc[x:x+1].values[0] = cruce4['COBERTURA'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['FACTURACION'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['FACTURACION'].iloc[x:x+1].values[0] = cruce4['FACTURACION'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    # elif diferencia_a_retirar_de_rubros > 0 and cruce4['MAOS'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                    #     cruce4['MAOS'].iloc[x:x+1].values[0] = cruce4['MAOS'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                    #     flag_r = True
                    elif diferencia_a_retirar_de_rubros > 0 and cruce4['TARIFAS'].iloc[x:x+1].values[0] >= diferencia_a_retirar_de_rubros and flag_r == False:    
                        cruce4['TARIFAS'].iloc[x:x+1].values[0] = cruce4['TARIFAS'].iloc[x:x+1].values[0] - diferencia_a_retirar_de_rubros
                        flag_r = True
                    # cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    # cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    # cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    # cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    # cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    # cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    # cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Facturas en Proceso'
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Se ajustan valores para que diferencia en saldos sea 0, validar = no/opcional)'
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0])
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 30
                
                "Ajuste de iteración 30, donde quedan valores negativos y el VALOR ADEUDADO REAL es == a saldo ips"
                if cruce4['iteracion'].iloc[x:x+1].values[0] == 30 and cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] <= cruce4['VALOR ADEUDADO REAL'].iloc[x:x+1].values[0]:
                    cruce4['FECHA_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['NUMERO_DOCUMENTO_DE_PAGO'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_PAGO_MUNDIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0 #abs(cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] - cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] - cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0])
                    cruce4['NO_REGISTRADAS'].iloc[x:x+1].values[0] = 0
                    cruce4['EN_TERMINOS_O_REVISION'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_TOTAL_O_DEVOLUCION_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    cruce4['VALOR_OBJECION_DEVOLUCION'].iloc[x:x+1].values[0] = 0
                    cruce4['CAUSAL_OBJECION'].iloc[x:x+1].values[0] = ''
                    cruce4['VALOR_ACEPTADO_IPS'].iloc[x:x+1].values[0] = 0
                    # cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = 0
                    if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == mensaje_precripcion:                       
                        cruce4['VALOR_OBJECION_PARCIAL_PRESCRITA'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                    else:
                        cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]
                    # cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] = 0
                    cruce4['HABILITACION'].iloc[x:x+1].values[0] = 0
                    cruce4['PERTINENCIA'].iloc[x:x+1].values[0] = 0
                    cruce4['COBERTURA'].iloc[x:x+1].values[0] = 0
                    cruce4['SOPORTES'].iloc[x:x+1].values[0] = 0
                    cruce4['FACTURACION'].iloc[x:x+1].values[0] = 0
                    cruce4['MAOS'].iloc[x:x+1].values[0] = 0
                    cruce4['TARIFAS'].iloc[x:x+1].values[0] = 0
                    cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] = 'Objecion Parcial '
                    # cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + '(Esta factura se encuentra en trámite según su estado actual de HR, validar = no/opcional)'
                    cruce4['validar'].iloc[x:x+1].values[0] = 'no/opcional'
                    cruce4['iteracion'].iloc[x:x+1].values[0] = 31
                    
                "OBSERVACIONES"
                "DIFERENCIA EN SALDOS"
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == 'Objecion Parcial' and cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] != mensaje_precripcion and (cruce4['FACTURA IQ'].iloc[x:x+1:3].values[0][:3] == prefijos_ratificacion[0] or cruce4['FACTURA IQ'].iloc[x:x+1:3].values[0][:3] == prefijos_ratificacion[1] or cruce4['FACTURA IQ'].iloc[x:x+1:3].values[0][:3] == prefijos_ratificacion[2] or cruce4['FACTURA IQ'].iloc[x:x+1:3].values[0][:3] == prefijos_ratificacion[3]):
                    cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] = 'Ratificado'
                    
                if cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == 'Objecion Parcial' and cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] != mensaje_precripcion and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] == cruce4['VALOR_RADICADO_FACTURA'].iloc[x:x+1].values[0] and cruce4['VALOR_OBJECION_PARCIAL'].iloc[x:x+1].values[0] == cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0]:
                    cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] = 'Respuesta no subsanada'
                
                if cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] == '' and cruce4['OBSERVACIONES_MUNDIAL'].iloc[x:x+1].values[0] == 'Objecion Parcial':
                    cruce4['OBSERVACIONES'].iloc[x:x+1].values[0] = 'Sin respuesta'
                
                "transporte"
                if cruce4['VALOR_RADICADO_FACTURA'].iloc[x:x+1].values[0] < cruce4['SALDO_REGISTRADO_IPS'].iloc[x:x+1].values[0] and cruce4['iteracion'].iloc[x:x+1].values[0] != 16:
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + ' (El valor saldo IPS es mayor al valor radicado) '
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                
                if cruce4['gt'].iloc[x:x+1].values[0] == 's':
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + ' (El valor de la factura contiene gastos de transporte) '
                
                if cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                    cruce4['validar'].iloc[x:x+1].values[0] = 'si/opcional'
                
                "Juridico"
                if cartera_judicial_activa == True and cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] > 0:
                    cruce4['DIFERENCIA_EN_SALDOS'].iloc[x:x+1].values[0] = 0
                    cruce4['MENSAJE'].iloc[x:x+1].values[0] = cruce4['MENSAJE'].iloc[x:x+1].values[0] + ' (Se retira la diferencia en saldos no correspondiente por ser juridica) '
        
        # !!!
        except Exception as e:#3
             tm.showerror("Error for:", str(e))
             
        cruce4 = cruce4.drop(['gt','VLR APROBADO','DOCUMENTO DE PAGO ','F.GIRO','Valor Aceptado Ips'], axis=1)
    
        #########################################################**************************************************************FASE2
        #########################################################**************************************************************FASE2
        try:
            "Detalle Objecion Parcial"
            
            cruce5 = cruce4
            cruce5 = cruce5[cruce5['VALOR_OBJECION_PARCIAL'] > 0]
            cruce5 = cruce5.loc[:,['RADICADO_APERTURA','FACTURA IQ','NIT','FACTURA','F.LIQUIDACION']]
            cruce5 = cruce5.drop_duplicates()
            #!!!
        
            
            
            if glosa_anterior.get() == 'activado':
                cruce5 = pd.merge(cruce5, df_liq_riq2, left_on='RADICADO_APERTURA', right_on='Numero_Radicado_Inicial', how='left')#cambiar el radicado a radicado inicial real
            else:
                cruce5 = pd.merge(cruce5, df_liq_riq, left_on='RADICADO_APERTURA', right_on='Numero_Radicado_Inicial', how='left')
                
            cruce6 = cruce5[cruce5['Centro_de_costo'].fillna('na').str.contains('steos')]
            cruce5 = cruce5[~cruce5['Centro_de_costo'].fillna('na').str.contains('steos')]
            cruce5['Numero_Radicado_Inicial'] = cruce5['Numero_Radicado_Inicial'].fillna('sin data')
            cruce6['Numero_Radicado_Inicial'] = cruce6['Numero_Radicado_Inicial'].fillna('sin data')
            
            cruce5['RadicadoInicial'] = 's'
            cruce6['RadicadoInicial'] = 's'
        except Exception as e:
            tm.showerror("Error fase 2:", str(e))
        
        #########################################################**************************************************************FASE3
        #########################################################**************************************************************FASE3
        "Detalle Objecion Parcial 3"
        try:
            cruce5_2 = cruce4
            cruce5_2 = cruce5_2[(cruce5_2['VALOR_OBJECION_PARCIAL'] > 0) & (cruce5_2['RADICADO_APERTURA']!='')]
            cruce5_2 = cruce5_2.loc[:,['RADICADO_APERTURA','FACTURA IQ','NIT','FACTURA','F.LIQUIDACION']]
            cruce5_2 = cruce5_2.drop_duplicates()
            #!!!
            
            if glosa_anterior.get() == 'activado':
                cruce5_2 = pd.merge(cruce5_2, df_liq_riq2, left_on='FACTURA IQ', right_on='Numero_Radicado_Inicial', how='left')
            else:
                cruce5_2 = pd.merge(cruce5_2, df_liq_riq, left_on='FACTURA IQ', right_on='Numero_Radicado_Inicial', how='left')#cambiar el radicado a radicado inicial real
            
            cruce6_2 = cruce5_2[cruce5_2['Centro_de_costo'].fillna('na').str.contains('steos')]
            cruce5_2 = cruce5_2[~cruce5_2['Centro_de_costo'].fillna('na').str.contains('steos')]
            cruce5_2['Numero_Radicado_Inicial'] = cruce5_2['Numero_Radicado_Inicial'].fillna('sin data')
            cruce6_2['Numero_Radicado_Inicial'] = cruce6_2['Numero_Radicado_Inicial'].fillna('sin data')
            
            cruce5_2['RadicadoInicial'] = 'n'
            cruce6_2['RadicadoInicial'] = 'n'

            "Concatenar resultados de fase2, fase3"
            cruce5 = pd.concat([cruce5,cruce5_2])#objeciones diferentes a maos
            cruce6 = pd.concat([cruce6,cruce6_2])#objeciones de maos
        
        except Exception as e:
            tm.showerror("Error fase 3:", str(e))
            
        ########################################################
        
        # !!!
        try:#4
            cruce5['OBJETADO_POR'] = cruce5[['Codigo_glosa_general_id']].apply(lambda x: 
                                                'FACTURACION' if x['Codigo_glosa_general_id'] == facturacion_IQ[0] or 
                                                x['Codigo_glosa_general_id'] == facturacion_IQ[1] or
                                                x['Codigo_glosa_general_id'] == facturacion_IQ[2] or
                                                x['Codigo_glosa_general_id'] == facturacion_MOK and x['centro_costo_maos'] == 'n' else
                                                'TARIFAS' if x['Codigo_glosa_general_id'] == tarifas_IQ or
                                                x['Codigo_glosa_general_id'] == tarifas_MOK[0] or 
                                                x['Codigo_glosa_general_id'] == tarifas_MOK[1] and 
                                                x['centro_costo_maos'] == 'n' else
                                                'SOPORTES' if x['Codigo_glosa_general_id'] == soportes_IQ or
                                                x['Codigo_glosa_general_id'] == soportes_MOK and x['centro_costo_maos'] == 'n' else
                                                'COBERTURA' if x['Codigo_glosa_general_id'] == cobertura_IQ or
                                                x['Codigo_glosa_general_id'] == cobertura_MOK and x['centro_costo_maos'] == 'n' else
                                                'PERTINENCIA' if x['Codigo_glosa_general_id'] == pertinencia_IQ or
                                                x['Codigo_glosa_general_id'] == pertinencia_MOK[0] or 
                                                x['Codigo_glosa_general_id'] == pertinencia_MOK[1] or
                                                x['Codigo_glosa_general_id'] == pertinencia_MOK[2] or 
                                                x['Codigo_glosa_general_id'] == pertinencia_MOK[3] or 
                                                x['Codigo_glosa_general_id'] == pertinencia_MOK[4] or
                                                x['Codigo_glosa_general_id'] == pertinencia_MOK[5] and x['centro_costo_maos'] == 'n' else
                                                'HABILITACION' if x['Codigo_glosa_general_id'] == habilitacion_IQ[0] or x['Codigo_glosa_general_id'] == habilitacion_IQ[1] or
                                                x['Codigo_glosa_general_id'] == habilitacion_MOK and x['centro_costo_maos'] == 'n' else 'NoAplica' ,axis=1)
            
            
            ####################################
            "Obtener el material de MAOS por servicio mediante cruce de relacionamiento entre MAOS y Liq iq, riq"
            cruce7 = cruce6
            
            df_mao_p23['Valor unitario facturado'] = df_mao_p23['Valor unitario facturado'].replace(',','.', regex=True).astype(float)
            df_mao_p23['Valor total facturado'] = df_mao_p23['Valor total facturado'].replace(',','.', regex=True).astype(float)
            cruce7['id'] = np.arange(1,len(cruce7)+1)
            cruce7 = pd.merge(cruce6, df_mao_p23, left_on='RADICADO_APERTURA', right_on='No Radicado', how='left')
            try:
                cruce7['validacion'] = cruce7[['Valor total facturado','Valor_Aprobado_Inicial','Valor_glosado_Inicial','Valor_Servicio']].apply(lambda x:
                                     's' if x['Valor total facturado'] == x['Valor_Servicio'] else 'n', axis=1)
            # except Exception as e:
            #     tm.showerror('Ha ocurrido un error, la información de la cartera vs la HR puede no concordar, revise y cargue nuevamente la información: ', str(e))
            except:
                cruce7['validacion'] = 's'
                pass
            cruce7 = cruce7.sort_values(by=['id'], ascending=True)
            cruce7_1 = cruce7[cruce7['No Radicado'].notnull()]
            cruce7_1 = cruce7_1[cruce7_1['validacion'] == 's']
            cruce7_2 = cruce7[~cruce7['No Radicado'].notnull()]
            
            cruce7 = pd.concat([cruce7_1,cruce7_2])
            cruce7 = cruce7.drop_duplicates(subset=['id'], keep='first')
            
            
            cruce5['radicado_resultado'] = np.where(cruce5['FACTURA IQ'] == cruce5['Numero_Radicado_Inicial'],'Movimiento correspondiente','Otro movimiento')
            cruce7['radicado_resultado'] = np.where(cruce7['FACTURA IQ'] == cruce7['Numero_Radicado_Inicial'],'Movimiento correspondiente','Otro movimiento')
            
            "se seleccionan las cabeceras"
            cruce5 = cruce5.loc[:,['RADICADO_APERTURA', 'NIT', 'FACTURA','F.LIQUIDACION',
                    'Numero_Radicado_Inicial','radicado_resultado', 'Observacion_servicio', 'Cantidad', 'Valor_Servicio',
                    'Codigo_glosa_general_id', 'Codigo_glosa_Especifica_id',
                    'Observacion_de_la_glosa', 'Valor_Aprobado_Inicial',
                    'Valor_glosado_Inicial', 'Valor_Factura', 'ValorAIPS', 'ValorSRTAIPS',
                    'Centro_de_costo', 'Codigo_de_servicio', 'NotaCredito','RadicadoInicial','OBJETADO_POR']]
            
            cruce7 = cruce7.loc[:,['RADICADO_APERTURA', 'NIT', 'FACTURA','F.LIQUIDACION',
                    'Numero_Radicado_Inicial','radicado_resultado',
                    'Observacion_servicio', 'Cantidad', 'Valor_Servicio',
                    'Codigo_glosa_general_id', 'Codigo_glosa_Especifica_id',
                    'Observacion_de_la_glosa', 'Valor_Aprobado_Inicial',
                    'Valor_glosado_Inicial', 'Valor_Factura', 'ValorAIPS', 'ValorSRTAIPS',
                    'Centro_de_costo', 'Codigo_de_servicio', 'NotaCredito',
                    'Nombre MAOS','NIT Proveedor','Razón Social Proveedor', 'Unidades', 'Valor unitario facturado',
                    'Valor total facturado','RadicadoInicial']]
        except Exception as e: #4
            tm.showerror("Error fase final:", str(e))
            
            
        "novedades hr, diferencias en saldos"
        try:
            cruce8 = cruce4
            cruce8 = cruce8[cruce8['DIFERENCIA_EN_SALDOS'] > 0]
            cruce8 = cruce8.loc[:,['NIT','FACTURA','SALDO_REGISTRADO_IPS']].drop_duplicates(subset=['NIT','FACTURA'], keep='first')
            cruce8 = pd.merge(cruce8, cruce, on=['NIT','FACTURA'], how='left')
            
        except Exception as e:
            tm.showerror("Error fase final - errores diferencias en saldo:", str(e))
            
            
        #######################################################################
        #======================================================================
        #======================================================================
        #######################################################################
        # Ajuste Codigo Glosas Iniciales
        
        # for r in range(len(cruce5)):
        #     l = cruce5[cruce5['RADICADO_APERTURA'] == cruce5['RADICADO_APERTURA'].iloc[r:r+1].values[0]]
        #     if cruce5['Codigo_glosa_general_id'].iloc[r:r+1].values[0] == 9.0:
        #         for w in range(len(l)):
        #             if cruce5['Codigo_de_servicio'].iloc[r:r+1].values[0] == l['Codigo_de_servicio'].iloc[w:w+1].values[0] and l['Codigo_glosa_general_id'].iloc[w:w+1].values[0].astype(int) != 9 and cruce5['Valor_Servicio'].iloc[r:r+1].values[0] == l['Valor_Servicio'].iloc[w:w+1].values[0]:
        #                 cruce5['Codigo_glosa_general_id'].iloc[r:r+1].values[0] = l['Codigo_glosa_general_id'].iloc[w:w+1].values[0]
        #                 continue
        
        #######################################################################
        #======================================================================
        #======================================================================

        #######################################################################
        "Exportar la informacion cruzada"
        try:
            id_reclamante = df_cartera['NIT'].iloc[0:1].values[0]
            dt = str(datetime.now().date()) +'_'+ str(datetime.now().hour) + str(datetime.now().minute) + str(datetime.now().second)
            # tm.showinfo("1", '')
            
            if cartera_judicial.get() == "activado":
                excel = pd.ExcelWriter(r'resultado_cartera_judicial_' + id_reclamante + '_' + dt + '.xlsx', engine='xlsxwriter')       
            else:
                excel = pd.ExcelWriter('resultado_cartera_' + id_reclamante + '_' + dt + '.xlsx', engine='xlsxwriter')
           
            # excel = pd.ExcelWriter(r'C:\Users\ynorena\Downloads\resultado_cartera_' + id_reclamante + '_' + dt + '.xlsx', engine='xlsxwriter')#pruebas
            # tm.showinfo("2", '')
            cruce4.to_excel(excel, sheet_name='Cruce_cartera', index=False)
            cruce8.to_excel(excel, sheet_name='Novedades_HR', index=False)
            cruce5.to_excel(excel, sheet_name='Obj_parcial', index=False)
            #cruce6.to_excel(excel, sheet_name='Obj_MAOS', index=False)#Objecion MAOS sin detalle de materiales
            cruce7.to_excel(excel, sheet_name='Obj_MAOS_detalle', index=False)
            
            "Se exporta la cartera"
            excel.close()
            
            # Helper.cronometro.finalizar()
        except Exception as e:
            tm.showerror("Error exportación:", str(e))
        #cruce4.to_excel(r'resultado_cartera_' + dt + '.xlsx', index=False)
        "mensaje de cruce exitoso"
        tm.showinfo("Cruce completado", "La cartera a cruzar se ha exportado exitosamente")
    
    # !!! Fin 1
    
    except Exception as e:
          tm.showerror("Error cruce:", str(e))
         #cruce4.to_excel(r'C:\Users\ynorena\Downloads\resultado_cartera8_4.xlsx', index=False)
        
   

###############################################################################
##################################### MAIN ####################################
###############################################################################

def main():
    global ventana
    global estilo_etiquetas 
    global estilo_etiquetas_titulo
    global boton_hoja_de_ruta
    global boton_comenzar
    
    global data_a_cargar_iq_2017,data_a_cargar_iq_2018,data_a_cargar_iq_2019,data_a_cargar_iq_2020,data_a_cargar_iq_2021,cartera_judicial
    global data_a_cargar_iq_2022,data_a_cargar_iq_2023,data_a_cargar_iq_2024,data_a_cargar_mok, glosa_anterior
    
    
    ventana = tk.Tk()
    ventana.title('CRUCE CARTERAS')
    ventana.geometry("600x450")
    ventana.resizable(False, False)
    
    
    estilo_etiquetas = {
         'bg': '#E3F2FD',
         'fg': 'black',
         'activebackground': 'blue',
         'activeforeground': 'black',
         'font': ('Helvetica', 11, 'bold')
     }
    estilo_etiquetas_titulo = {
         'bg': '#E3F2FD',
         'fg': 'black',
         'activebackground': 'blue',
         'activeforeground': 'black',
         'font': ('Helvetica', 14, 'bold')
     }
    
    #==========================================================================
    # Configuración Img de Fondo Aplicativo
    #==========================================================================
    
    # Ruta al archivo de imagen
    path_imagen = r"\\Ibm-fsbsrdel\Direccion_Siniestros_SOAT\yeferson\data_prueba\Img\background_sm.png"
    
    # Abrir la imagen con Pillow
    imagen_pil = Image.open(path_imagen)

    # Redimensionar la imagen al tamaño de la ventana
    imagen_pil = imagen_pil.resize((600, 450), Image.LANCZOS)

    # Convertir la imagen de PIL a PhotoImage de Tkinter
    photo = ImageTk.PhotoImage(imagen_pil)

    # Crear un widget Label para mostrar la imagen, ajustado a la ventana
    label = tk.Label(ventana, image=photo)
    label.image = photo  # Guardar una referencia a la imagen para evitar que se destruya por el recolector de basura
    label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #==========================================================================
    
    
    
    # Estilos
    style = ttk.Style()
    style.theme_use('alt')  # Puedes probar otros temas como 'alt', 'default', 'classic'
    style.configure("TLabel", background='#E3F2FD', foreground='black')
    style.configure("TButton", background='#E3F2FD', foreground='white', font=('Helvetica', 11, 'bold'))
    style.configure("TCheckbutton", background='#E3F2FD', font=('Helvetica', 11))
    
    #Variables de controles
    data_a_cargar_iq_2017 = tk.StringVar(value="desactivado")
    data_a_cargar_iq_2018 = tk.StringVar(value="desactivado")
    data_a_cargar_iq_2019 = tk.StringVar(value="desactivado")
    data_a_cargar_iq_2020 = tk.StringVar(value="activado")
    data_a_cargar_iq_2021 = tk.StringVar(value="activado")
    data_a_cargar_iq_2022 = tk.StringVar(value="activado")
    data_a_cargar_iq_2023 = tk.StringVar(value="activado")
    data_a_cargar_iq_2024 = tk.StringVar(value="activado")
    data_a_cargar_mok = tk.StringVar(value="desactivado")
    cartera_judicial = tk.StringVar(value="desactivado")
    
    #==========================================================================
    
    glosa_anterior = tk.StringVar(value="activado")
    
    #==========================================================================
    
    
    checkbutton_data_iq_2017 = ttk.Checkbutton(text="Data 2017", 
                                        variable=data_a_cargar_iq_2017, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    checkbutton_data_iq_2018 = ttk.Checkbutton(text="Data 2018", 
                                        variable=data_a_cargar_iq_2018, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    checkbutton_data_iq_2019 = ttk.Checkbutton(text="Data 2019", 
                                        variable=data_a_cargar_iq_2019, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    checkbutton_data_iq_2020 = ttk.Checkbutton(text="Data 2020", 
                                        variable=data_a_cargar_iq_2020, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    checkbutton_data_iq_2021 = ttk.Checkbutton(text="Data 2021", 
                                        variable=data_a_cargar_iq_2021, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    checkbutton_data_iq_2022 = ttk.Checkbutton(text="Data 2022", 
                                        variable=data_a_cargar_iq_2022, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    checkbutton_data_iq_2023 = ttk.Checkbutton(text="Data 2023", 
                                        variable=data_a_cargar_iq_2023, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    checkbutton_data_iq_2024 = ttk.Checkbutton(text="Data 2024", 
                                        variable=data_a_cargar_iq_2024, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    checkbutton_data_mok = ttk.Checkbutton(text="Data MOK", 
                                        variable=data_a_cargar_mok, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    checkbutton_cartera_judicial = ttk.Checkbutton(text="¿Es una cartera judicial?", 
                                        variable=cartera_judicial, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    
    #==========================================================================
    # Creación Chekbutton Ajuste Codigos Glosa Inicial
    
    checkbutton_glosa_anterior = ttk.Checkbutton(text="¿Mantener Conceptos Objeción Iniciales?", 
                                        variable=glosa_anterior, 
                                        onvalue="activado", 
                                        offvalue="desactivado",
                                        style="EstiloCheckbutton.TCheckbutton")
    
    
    #==========================================================================
    
    
    boton_informacion = tk.Button(ventana, text="?", command=mostrar_informacion, width=2,**estilo_informacion)
    
    etiqueta_titulo = tk.Label(ventana, text="CRUCE CARTERAS", **estilo_etiquetas_titulo)
    
    etiqueta_hojas = tk.Label(ventana, text="DATA", **estilo_etiquetas_titulo)
    
    etiqueta_filtros_grupo_ips = tk.Label(ventana, text="CARTERA JUDICIAL", **estilo_etiquetas_titulo)
    
   
    boton_hoja_de_ruta = tk.Button(ventana, text="Cargar HR", command= cargar_hr, **estilo_seleccionar)
    boton_investigaciones = tk.Button(ventana, text="Cargar Cartera", command= cargar_cartera, **estilo_seleccionar)
    cargar_datos = tk.Button(ventana, text="Cargar Data", command= cargar_data, **estilo_seleccionar)

    boton_comenzar = tk.Button(ventana, text="Realizar Cruce", command= cruce_cartera, **estilo_comenzar)
    boton_comenzar.config(state="normal")
    
    # Centrar el label en la ventana
    etiqueta_titulo.place(relx=0.5, y=20, anchor='n')
    etiqueta_hojas.place(x=100, y=100)
    etiqueta_filtros_grupo_ips.place(x=375, y=100)
    
    boton_hoja_de_ruta.place(x=170, y=400)
    boton_investigaciones.place(x=250, y=400)
    cargar_datos.place(x=80, y=400)
    boton_comenzar.place(x=400, y=400)
    boton_informacion.place(x=553, y=5)
    
    checkbutton_data_iq_2017.place(x=80, y=140)
    checkbutton_data_iq_2018.place(x=80, y=170)
    checkbutton_data_iq_2019.place(x=80, y=200)
    checkbutton_data_iq_2020.place(x=80, y=230)
    checkbutton_data_iq_2021.place(x=80, y=260)
    checkbutton_data_iq_2022.place(x=80, y=290)
    checkbutton_data_iq_2023.place(x=80, y=320)
    checkbutton_data_iq_2024.place(x=80, y=350)
    checkbutton_data_mok.place(x=210, y=140)
    checkbutton_cartera_judicial.place(x=380, y=140)
    checkbutton_glosa_anterior.place(x=80, y=60)
    
    
    ventana.mainloop()
    
    variables = globals().copy()
    for variable in variables:
        if variable != 'variables':
            del globals()[variable]
    
if __name__ == '__main__':
    main()


