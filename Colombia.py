import tkinter as tk
from tkinter import messagebox, scrolledtext
import re

# Diccionario de rangos de prefijos para cada departamento
rangos_departamentos = {
    "Bogotá D.C.": ("BAA", "BZZ"),
    "Antioquia": ("FAA", "FZZ"),
    "Valle del Cauca": ("VAA", "VZZ"),
    "Atlántico": ("AAA", "AZZ"),
    "Santander": ("GAA", "GZZ"),
    "Cundinamarca": ("CAA", "CZZ"),
    "Bolívar": ("MAA", "MZZ"),
    "Boyacá": ("DAA", "DZZ"),
    "Caldas": ("EAA", "EZZ"),
    "Risaralda": ("RAA", "RZZ"),
    "Quindío": ("QAA", "QZZ"),
    "Nariño": ("NAA", "NZZ"),
    "Tolima": ("TAA", "TZZ"),
    "Huila": ("HAA", "HZZ"),
    "Magdalena": ("LAA", "LZZ"),
    "Cesar": ("KAA", "KZZ"),
    "Norte de Santander": ("JAA", "JZZ"),
    "Córdoba": ("OAA", "OZZ"),
    "Sucre": ("SAA", "SZZ"),
    "La Guajira": ("UAA", "UZZ"),
    "Meta": ("WAA", "WZZ"),
    "Cauca": ("YAA", "YZZ"),
    "Casanare": ("ZAA", "ZZZ"),
    "Arauca": ("XAA", "XZZ"),
    "Amazonas": ("IAA", "IZZ"),
    "Guainía": ("PAA", "PZZ"),
    "Guaviare": ("NAA", "NZZ"),
    "Putumayo": ("HAA", "HZZ"),
    "Vaupés": ("QAA", "QZZ"),
    "Vichada": ("TAA", "TZZ"),
    "San Andrés y Providencia": ("SAA", "SZZ")
}


# Función para análisis léxico
def analisis_lexico(matricula):
    patron = r"^[A-Z]{3}-\d{3}$"
    return bool(re.match(patron, matricula))


# Función para análisis sintáctico
def analisis_sintactico(matricula):
    prefijo = matricula[:3]
    for departamento, (inicio, fin) in rangos_departamentos.items():
        if inicio <= prefijo <= fin:
            return True, departamento
    return False, None


# Función para derivación por la izquierda
def derivacion_por_izquierda(prefijo, numeros):
    pasos = []
    produccion = "<matricula>"
    pasos.append(produccion)
    produccion = "<prefijo>-<numeros>"
    pasos.append(produccion)
    produccion = f"{prefijo}-<numeros>"
    pasos.append(produccion)
    for digito in numeros:
        produccion = produccion.replace("<numeros>", f"{digito}<numeros>", 1)
        pasos.append(produccion)
    pasos[-1] = pasos[-1].replace("<numeros>", "")
    return pasos


# Función principal para analizar matrícula
def analizar_matricula():
    matricula = entry_matricula.get().strip().upper()

    # Análisis léxico
    if not analisis_lexico(matricula):
        messagebox.showerror("Error", "Formato léxico inválido. Use LLL-###.")
        return

    # Análisis sintáctico
    prefijo = matricula[:3]
    numeros = matricula[4:]
    valido_sintactico, departamento = analisis_sintactico(matricula)

    if not valido_sintactico:
        messagebox.showerror("Error", "Prefijo no válido para ningún departamento.")
        return

    # Derivación
    derivacion = derivacion_por_izquierda(prefijo, numeros)

    # Mostrar resultados
    text_resultado.delete(1.0, tk.END)
    text_resultado.insert(tk.END, f"Matrícula: {matricula}\n")
    text_resultado.insert(tk.END, f"Departamento: {departamento}\n\n")
    text_resultado.insert(tk.END, "Derivación por la izquierda:\n")
    for paso in derivacion:
        text_resultado.insert(tk.END, f"{paso}\n")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Análisis de Matrículas Colombianas")
ventana.geometry("500x400")

# Etiqueta y entrada para matrícula
label_matricula = tk.Label(ventana, text="Ingrese la matrícula (formato LLL-###):")
label_matricula.pack(pady=10)
entry_matricula = tk.Entry(ventana, width=30)
entry_matricula.pack(pady=5)

# Botón para analizar
btn_analizar = tk.Button(ventana, text="Analizar Matrícula", command=analizar_matricula)
btn_analizar.pack(pady=10)

# Área de texto para mostrar resultados
text_resultado = scrolledtext.ScrolledText(ventana, width=50, height=15)
text_resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
