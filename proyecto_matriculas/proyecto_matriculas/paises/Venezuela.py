import re
from paises.pais import Pais

class Venezuela(Pais):
    def __init__(self):
        super().__init__("Venezuela")
        # Códigos de estados y sus nombres
        self.estados = {
            "AM": "Amazonas",
            "AN": "Anzoátegui",
            "AR": "Aragua",
            "BA": "Barinas",
            "CA": "Carabobo",
            "DA": "Delta Amacuro",
            "FA": "Falcón",
            "GU": "Guárico",
            "LA": "La Guaira",
            "MI": "Miranda",
            "MO": "Monagas",
            "NE": "Nueva Esparta",
            "PO": "Portuguesa",
            "SU": "Sucre",
            "TA": "Táchira",
            "TR": "Trujillo",
            "YA": "Yaracuy",
            "ZA": "Zulia",
        }

    def validar_matricula(self, matricula):
        """
        Valida si una matrícula es válida en Venezuela.
        :param matricula: Matrícula a validar.
        :return: Tuple (bool, dict). El booleano indica si es válida, el dict contiene detalles.
        """
        # Patrones para diferentes tipos de matrícula
        patrones = {
            "Particular": r"^[A-Z]{2}\d{3}[A-Z]{2}$",  # Ejemplo: AB123CD
            "Público": r"^PT\d{3}[A-Z]{2}$",  # Ejemplo: PT123AB
            "Diplomático": r"^CD\d{3}$",  # Ejemplo: CD123
            "Oficial": r"^OA\d{3}[A-Z]{2}$",  # Ejemplo: OA123BC
            "Carga": r"^CA\d{3}[A-Z]{2}$",  # Ejemplo: CA123DE
        }

        for tipo, patron in patrones.items():
            if re.match(patron, matricula):
                # Determinar el estado de origen
                estado = "No aplica"
                codigo_estado = None

                if tipo in ["Particular", "Oficial", "Carga"]:
                    codigo_estado = matricula[:2]  # Tomar las dos primeras letras
                    estado = self.estados.get(codigo_estado, "Desconocido")

                return True, {
                    "matricula": matricula,
                    "tipo": tipo,
                    "estado": estado,
                    "codigo_estado": codigo_estado,
                    "servicio": tipo
                }

        return False, {}

    def derivar_matricula(self, partes):
        """
        Realiza una derivación gramatical de la matrícula.
        :param partes: Diccionario con los detalles de la matrícula.
        :return: Lista con los pasos de la derivación gramatical.
        """
        matricula = partes["matricula"]
        pasos = ["<matricula>", "<venezuela>"]

        if partes["tipo"] == "Diplomático":
            pasos.append("CD <numeros>")
            pasos.append(f"CD {matricula[2:]}")
        else:
            pasos.append("<codigo_estado> <numeros> <serie>")
            codigo_estado = matricula[:2]
            numeros = matricula[2:5]
            serie = matricula[5:]
            pasos.append(f"{codigo_estado} <numeros> <serie>")
            pasos.append(f"{codigo_estado} {numeros} <serie>")
            for i in range(len(serie)):
                pasos.append(f"{codigo_estado} {numeros} {serie[:i+1]}<serie>")
            pasos[-1] = pasos[-1].replace("<serie>", "")

        return pasos
