import pandas as pd
import re

class Colombia:
    def __init__(self, archivo_excel):
        """
        Inicializa la clase Colombia cargando los rangos de matrículas desde un archivo Excel.
        :param archivo_excel: Ruta al archivo Excel con los rangos de matrículas.
        """
        self.nombre = "Colombia"
        self.rangos_departamentos = self.cargar_rangos(archivo_excel)

    def cargar_rangos(self, archivo_excel):
        """
        Carga los rangos de matrículas desde un archivo Excel y los organiza por departamento y ciudad.
        :param archivo_excel: Ruta al archivo Excel.
        :return: Diccionario con los rangos organizados.
        """
        try:
            # Leer el archivo Excel
            data = pd.read_excel(archivo_excel, engine="openpyxl")
            rangos = {}

            # Procesar cada fila del archivo
            for _, row in data.iterrows():
                rango_inicial = str(row["RANGO"]).strip() if not pd.isna(row["RANGO"]) else None
                rango_final = str(row["Unnamed: 1"]).strip() if not pd.isna(row["Unnamed: 1"]) else None
                departamento = row["LOCALIZACION"] if not pd.isna(row["LOCALIZACION"]) else "Desconocido"
                ciudad = row["Unnamed: 3"] if not pd.isna(row["Unnamed: 3"]) else "No disponible"

                # Validar que los rangos sean válidos
                if rango_inicial and rango_final:
                    if departamento not in rangos:
                        rangos[departamento] = []
                    rangos[departamento].append((rango_inicial, rango_final, ciudad))

            return rangos
        except Exception as e:
            raise ValueError(f"Error al cargar los rangos desde el archivo {archivo_excel}: {e}")

    def validar_matricula(self, matricula):
        """
        Valida si una matrícula corresponde a un rango de Colombia.
        :param matricula: Matrícula a validar (ejemplo: 'ABC123').
        :return: Tuple (bool, dict). El booleano indica si es válida, el dict contiene detalles.
        """
        patron = r"^[A-Z]{3}\d{3}$"  # Patrón para validar el formato colombiano
        if re.match(patron, matricula):
            for departamento, rangos in self.rangos_departamentos.items():
                for inicio, fin, ciudad in rangos:
                    # Verificar si la matrícula está dentro del rango
                    if inicio <= matricula <= fin:
                        return True, {
                            "matricula": matricula,
                            "departamento": departamento,
                            "ciudad": ciudad
                        }
        return False, {}

    def derivar_matricula(self, partes):
        """
        Realiza una derivación gramatical de la matrícula.
        :param partes: Diccionario con los detalles de la matrícula.
        :return: Lista con los pasos de la derivación gramatical.
        """
        matricula = partes["matricula"]
        pasos = ["<matricula>", "<colombia>", "<prefijo><numeros>"]
        prefijo = matricula[:3]
        numeros = matricula[3:]
        pasos.append(f"{prefijo}<numeros>")
        for i in range(len(numeros)):
            pasos.append(f"{prefijo}{numeros[:i+1]}<numeros>")
        pasos[-1] = pasos[-1].replace("<numeros>", "")
        return pasos
