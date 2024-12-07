import re
from paises.pais import Pais

class Uruguay(Pais):
    def __init__(self):
        super().__init__("Uruguay")
        # Diccionario de códigos de departamentos y localidades
        self.regiones = {
            "AR": {"departamento": "Artigas", "localidad": ["Artigas"]},
            "BU": {"departamento": "Artigas", "localidad": ["Bella Unión"]},
            "TG": {"departamento": "Rocha", "localidad": ["Tomás Gomensoro"]},
            "BB": {"departamento": "Treinta y Tres", "localidad": ["Baltasar Brum"]},
            "CA": {"departamento": "Canelones", "localidad": ["Canelones", "Las Piedras", "Pando"]},
            # Añade más códigos según sea necesario...
        }

        # Patrones para diferentes tipos de vehículos
        self.patrones = {
            "Particular": r"^[A-Z]{3}\d{4}$",  # Ejemplo: ABC1234
            "Diplomático": r"^CD\d{3}$",  # Ejemplo: CD234
            "Transporte Público (Taxis)": r"^TX\d{4}$",  # Ejemplo: TX5678
            "Oficial": r"^CF\d{4}$",  # Ejemplo: CF7890
            "Motocicleta": r"^[A-Z]{2}\d{4}$",  # Ejemplo: MC3456
        }

    def validar_matricula(self, matricula):
        """
        Valida si una matrícula es válida en Uruguay.
        :param matricula: Matrícula a validar.
        :return: Tuple (bool, dict). El booleano indica si es válida, el dict contiene detalles.
        """
        for tipo, patron in self.patrones.items():
            if re.match(patron, matricula):
                # Determinar el departamento y localidad (si aplica)
                codigo_departamento = matricula[:2] if tipo in ["Particular", "Motocicleta"] else None
                departamento = "Desconocido"
                localidad = "No aplica"

                if codigo_departamento and codigo_departamento in self.regiones:
                    departamento = self.regiones[codigo_departamento]["departamento"]
                    localidades = self.regiones[codigo_departamento]["localidad"]
                    localidad = ", ".join(localidades)

                return True, {
                    "matricula": matricula,
                    "tipo": tipo,
                    "departamento": departamento,
                    "localidad": localidad
                }
        return False, {}

    def derivar_matricula(self, partes):
        """
        Realiza una derivación gramatical de la matrícula.
        :param partes: Diccionario con los detalles de la matrícula.
        :return: Lista con los pasos de la derivación gramatical.
        """
        matricula = partes["matricula"]
        pasos = ["<matricula>", "<uruguay>"]

        if partes["tipo"] in ["Particular", "Motocicleta"]:
            pasos.append("<codigo_departamento><numeros>")
            codigo_departamento = matricula[:2]
            numeros = matricula[2:]
            pasos.append(f"{codigo_departamento}<numeros>")
            for i in range(len(numeros)):
                pasos.append(f"{codigo_departamento}{numeros[:i+1]}<numeros>")
            pasos[-1] = pasos[-1].replace("<numeros>", "")
        elif partes["tipo"] == "Diplomático":
            pasos.append("CD<numeros>")
            pasos.append(f"CD{matricula[2:]}")
        elif partes["tipo"] in ["Transporte Público (Taxis)", "Oficial"]:
            pasos.append("<prefijo><numeros>")
            prefijo = matricula[:2]
            numeros = matricula[2:]
            pasos.append(f"{prefijo}<numeros>")
            for i in range(len(numeros)):
                pasos.append(f"{prefijo}{numeros[:i+1]}<numeros>")
            pasos[-1] = pasos[-1].replace("<numeros>", "")

        return pasos
