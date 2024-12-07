import re
from paises.pais import Pais

class Peru(Pais):
    def __init__(self):
        super().__init__("Perú")
        # Diccionario de zonas registrales con su primer carácter y departamentos
        self.regiones = {
            "P": ["Tumbes", "Piura"],
            "M": ["Lambayeque", "Cajamarca", "Amazonas"],
            "S": ["San Martín"],
            "L": ["Loreto"],
            "T": ["La Libertad"],
            "U": ["Ucayali"],
            "H": ["Ancash"],
            "W": ["Junín", "Huánuco", "Pasco"],
            "A": ["Lima"], "B": ["Lima"], "C": ["Lima"], "D": ["Lima"], "F": ["Lima"],
            "X": ["Cusco", "Apurímac", "Madre de Dios"],
            "Y": ["Ica", "Ayacucho", "Huancavelica"],
            "V": ["Arequipa"],
            "Z": ["Moquegua", "Tacna", "Puno"]
        }

    def validar_matricula(self, matricula):
        # Patrones para diferentes tipos de matrícula
        patrones = {
            "Particular": r"^[A-Z]{3}-\d{3}$",  # Ejemplo: ABC-123
            "Taxi": r"^T\d[A-Z]-\d{3}$",        # Ejemplo: T1A-123
            "Transporte Público": r"^C\d[A-Z]-\d{3}$",  # Ejemplo: C1A-123
            "Gubernamental": r"^EG\d-\d{3}$"   # Ejemplo: EG1-234
        }

        for tipo, patron in patrones.items():
            if re.match(patron, matricula):
                # Identificar la región con base en el primer carácter
                primer_caracter = matricula[0]
                region = self.regiones.get(primer_caracter, "Desconocida")
                return True, {
                    "matricula": matricula,
                    "tipo": tipo,
                    "region": region,
                    "departamentos": ", ".join(self.regiones.get(primer_caracter, ["Desconocida"]))
                }

        return False, {}

    def derivar_matricula(self, partes):
        # Derivación por la izquierda
        matricula = partes["matricula"]
        pasos = ["<matricula>", "<peru>"]

        if partes["tipo"] == "Gubernamental":
            pasos.append("EG<numeros>-<numeros>")
            pasos.append(f"EG{matricula[2]}-<numeros>")
        elif partes["tipo"] == "Taxi":
            pasos.append("T<numero><letra>-<numeros>")
            pasos.append(f"T{matricula[1]}{matricula[2]}-<numeros>")
        elif partes["tipo"] == "Transporte Público":
            pasos.append("C<numero><letra>-<numeros>")
            pasos.append(f"C{matricula[1]}{matricula[2]}-<numeros>")
        else:  # Particular
            pasos.append("<letras>-<numeros>")
            pasos.append(f"{matricula[:3]}-<numeros>")

        # Derivar números
        numeros = matricula.split('-')[-1]
        for i in range(len(numeros)):
            pasos.append(f"{matricula[:-len(numeros)]}{numeros[:i+1]}<numeros>")
        pasos[-1] = pasos[-1].replace("<numeros>", "")

        return pasos
